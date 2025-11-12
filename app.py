from flask import Flask, render_template, request, redirect, url_for, session
from supabase import create_client, Client
from datetime import datetime
import os

app = Flask(__name__)
# ¡IMPORTANTE! Cambia esta clave en producción
app.secret_key = os.getenv("SECRET_KEY", "clave_super_secreta") 

# 🔧 Configuración de Supabase
# Asegúrate de reemplazar "TU_API_KEY" con la clave de tu proyecto
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cwyjhnxowglgqbqzshyd.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN3dmpobnhvd2dsZ3FicXpzaHlkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxMDE0NTQsImV4cCI6MjA3NTY3NzQ1NH0.lbW8TGXa7_WFoFeWE6Vfgt3kl2SdnyFt3Dv_vhgw1Qw") 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# 🏠 Página principal
@app.route('/')
def index():
    if "user" in session:
        usuario = session["user"]
        # Nota: 'id_trabajador' es el campo correcto de la DB
        return render_template("index.html", usuario=usuario) 
    return redirect(url_for('login'))


# 🔐 Login y Registro (Si no existe, se registra como nuevo cocinero)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Nota: El input se llama 'id_trabajo', pero la columna es 'id_trabajador'
        id_trabajador = request.form['id_trabajo']
        nombre = request.form['nombre']
        
        usuario_actual = None

        # 1. Buscar en tabla "cocinero"
        response = supabase.table('cocinero').select('*').eq('id_trabajador', id_trabajador).eq('nombre', nombre).execute()
        
        if response.data:
            # Caso A: El usuario ya existe, lo usamos.
            usuario_actual = response.data[0]
        else:
            # Caso B: El usuario NO existe, intentamos registrarlo.
            
            # Chequeo extra para IDs duplicados
            id_check = supabase.table('cocinero').select('nombre').eq('id_trabajador', id_trabajador).execute()
            if id_check.data:
                return "⚠️ El ID de trabajo ya existe con otro nombre o datos. Contacte al administrador."

            try:
                # Proveemos valores NOT NULL requeridos por tu esquema SQL:
                new_user_data = {
                    'id_trabajador': id_trabajador,
                    'nombre': nombre,
                    'fecha_ingreso': datetime.now().isoformat().split('T')[0],
                    'turno': 'Sin Asignar', 
                    # Añadimos marca de tiempo al correo para asegurar unicidad:
                    'correo': f'temp_{id_trabajador}_{datetime.now().strftime("%H%M%S")}@restaurante.com', 
                    'especialidad': 'General',
                    'años_experiencia': 0
                }
                
                insert_response = supabase.table('cocinero').insert(new_user_data).execute()
                
                if insert_response.data:
                    usuario_actual = insert_response.data[0]
                else:
                    return "⚠️ Error al registrar el nuevo usuario en Supabase."

            except Exception as e:
                print(f"ERROR: Falló el INSERT en Cocinero: {e}")
                return f"⚠️ Error de Supabase al registrar. Error: {e}"


        # Si tenemos un usuario (encontrado o recién creado)
        if usuario_actual:
            session['user'] = usuario_actual

            # 2. Registrar el inicio en la tabla de sesiones (Sesion_Cocinero)
            # NOTA: Esta tabla debe existir en Supabase (ver NOTAS.md)
            try:
                supabase.table('Sesion_Cocinero').insert({
                    'id_cocinero': usuario_actual['id_trabajador'], 
                    'fecha_login': datetime.now().isoformat(),
                    'estado': 'Activo'
                }).execute()
            except Exception as e:
                print(f"ERROR: Falló el registro en Sesion_Cocinero: {e}")
                # El login continua aunque falle el registro de sesión
            
            return redirect(url_for('index'))
        
        # Fallback
        return "⚠️ Datos incorrectos o usuario no encontrado/registrado."

    return render_template('login.html')


# 🚪 Cerrar sesión
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)