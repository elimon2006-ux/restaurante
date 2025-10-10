import os
from flask import Flask, render_template_string
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # Leer la URL de la base de datos desde la variable de entorno de Render
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if not DATABASE_URL:
        return "ERROR: La variable DATABASE_URL no está configurada.", 500
    
    conn = None
    resultado = "ERROR: No se pudo establecer la conexión." # Valor por defecto en caso de fallo
    
    try:
        # Intenta conectar a Supabase usando la URL
        conn = psycopg2.connect(DATABASE_URL)
        
        # SI LA CONEXIÓN ES EXITOSA, CAMBIA EL MENSAJE
        resultado = "¡CONEXIÓN A SUPABASE EXITOSA! 🎉 (El servidor está vivo)."
        
        # --- CONSULTAS ELIMINADAS ---
        # cursor = conn.cursor()
        # cursor.execute("SELECT 1") 
        # cursor.fetchone() 
        # --- FIN DE CONSULTAS ---

    except Exception as e:
        # Esto capturará cualquier error de credenciales o de red
        resultado = f"ERROR DE CONEXIÓN CRÍTICO: Revisa tu DATABASE_URL. Detalle: {e}"
        
    finally:
        if conn:
            conn.close() # Cierra la conexión de forma segura

    # Muestra el resultado en una página simple
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Prueba de Conexión</title></head>
    <body>
        <h1>Prueba de Conexión a Supabase</h1>
        <p>Estado del servicio:</p>
        <p><strong>{resultado}</strong></p>
        <p>URL del Proyecto: https://restaurante-o4bj.onrender.com</p>
    </body>
    </html>
    """
    return render_template_string(html_content)