from flask import Flask, render_template, request, redirect, url_for, session
from supabase import create_client, Client
from datetime import datetime
from dotenv import load_dotenv
import os

# ✅ Cargar variables de entorno desde .env
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Clave secreta de sesión
app.secret_key = os.getenv("SECRET_KEY", "clave_por_defecto_insegura")

# 🔧 Configuración de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Faltan variables SUPABASE_URL o SUPABASE_KEY en el archivo .env")

# Crear cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 🧪 Probar conexión a Supabase al iniciar (sin usar count(*))
try:
    # Obtener solo una fila como prueba
    test = supabase.table("cocinero").select("*").limit(1).execute()
    print("✅ Conexión exitosa a Supabase. Se detectó la tabla 'cocinero'.")
except Exception as e:
    print(f"❌ Error al conectar a Supabase: {e}")

# ------------------------
# 🏠 Página principal
# ------------------------
@app.route('/')
def index():
    if "user" in session:
        usuario = session["user"]
        return render_template("index.html", usuario=usuario)
    return redirect(url_for('login'))

# ------------------------
# 🔐 Login / Registro
# ------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id_input = request.form.get('id_trabajo')
        nombre = request.form.get('nombre')

        if not id_input or not nombre:
            return "⚠️ Faltan datos en el formulario."

        usuario_actual = None

        # Buscar usuario existente
        try:
            response = supabase.table('cocinero') \
                .select('*') \
                .eq('id_trabajador', id_input) \
                .eq('nombre', nombre) \
                .execute()
        except Exception as e:
            print(f"ERROR CRÍTICO (SELECT): {e}")
            return f"⚠️ Error de conexión a Supabase al buscar usuario: {e}"

        if response.data:
            usuario_actual = response.data[0]
            print(f"DEBUG: Usuario encontrado: {usuario_actual.get('nombre')}")
        else:
            # Verificar si el ID ya existe con otro nombre
            id_check = supabase.table('cocinero').select('nombre').eq('id_trabajador', id_input).execute()
            if id_check.data:
                return "⚠️ El ID de trabajo ya existe con otro nombre. Contacte al administrador."

            try:
                new_user_data = {
                    'id_trabajador': id_input,
                    'nombre': nombre,
                    'fecha_ingreso': datetime.now().isoformat().split('T')[0],
                    'turno': 'Sin Asignar',
                    'correo': f'temp_{id_input}_{datetime.now().strftime("%H%M%S")}@restaurante.com',
                    'especialidad': 'General',
                    'años_experiencia': 0
                }

                insert_response = supabase.table('cocinero').insert(new_user_data).execute()

                if insert_response.data:
                    usuario_actual = insert_response.data[0]
                    print(f"DEBUG: Nuevo usuario registrado: {usuario_actual.get('nombre')}")
                else:
                    return "⚠️ Error al registrar el nuevo usuario en Supabase."

            except Exception as e:
                print(f"ERROR CRÍTICO (INSERT): {e}")
                return f"⚠️ Error al registrar en Supabase. Revise RLS o esquema. Error: {e}"

        if usuario_actual:
            session['user'] = usuario_actual

            # Registrar sesión del cocinero
            try:
                supabase.table('Sesion_Cocinero').insert({
                    'id_cocinero': usuario_actual['id_trabajador'],
                    'fecha_login': datetime.now().isoformat(),
                    'estado': 'Activo'
                }).execute()
            except Exception as e:
                print(f"WARNING: No se pudo registrar la sesión. {e}")

            return redirect(url_for('index'))

        return "⚠️ Usuario no encontrado o datos incorrectos."

    return render_template('login.html')

# ------------------------
# 🚪 Cerrar sesión
# ------------------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# ------------------------
# 🚀 Ejecutar servidor Flask
# ------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
