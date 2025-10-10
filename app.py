import os
from flask import Flask, render_template_string
import psycopg2

app = Flask(__name__)

# La URL completa de Supabase se lee desde la Variable de Entorno
DATABASE_URL = os.environ.get('DATABASE_URL')

@app.route('/')
def index():
    if not DATABASE_URL:
        return "ERROR: La variable DATABASE_URL no está configurada.", 500
    
    conn = None
    resultado = "Conexión a Base de Datos Exitosa!"
    
    try:
        # Intenta conectar a Supabase usando la URL
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
        # Ejemplo: Consulta el nombre del trabajador con id=1 (debe existir)
        cursor.execute("SELECT nombre FROM Trabajador WHERE id_trabajador = 1")
        trabajador = cursor.fetchone()
        
        if trabajador:
            resultado = f"¡Bienvenido! Trabajador de prueba: {trabajador[0]}."
        else:
            resultado = "Conexión Exitosa. No se encontraron trabajadores (id=1) en la base de datos."

    except Exception as e:
        resultado = f"Error al conectar o consultar la BD: {e}"
        
    finally:
        if conn:
            conn.close()

    # Muestra el resultado en una página simple
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>App Restaurante</title></head>
    <body>
        <h1>Sistema de Pedidos del Restaurante</h1>
        <p>Estado de la base de datos (Supabase):</p>
        <p><strong>{resultado}</strong></p>
        <p>¡El siguiente paso es crear la interfaz de usuario para los pedidos!</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    # Nota: Render usará gunicorn, no el servidor de desarrollo de Flask
    app.run(debug=True)