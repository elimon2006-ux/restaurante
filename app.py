import os
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    # Leer la URL de la base de datos desde la variable de entorno de Render
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if not DATABASE_URL:
        return "ERROR: La variable DATABASE_URL no está configurada.", 500
    
    conn = None
    # Valores por defecto para la plantilla HTML (Trabajador 1)
    nombre_t1 = "N/A"
    turno_t1 = "N/A"
    
    # Valores por defecto para la plantilla HTML (Trabajador 2)
    nombre_t2 = "N/A"
    turno_t2 = "N/A"
    
    estado_conexion = "ERROR"
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        estado_conexion = "CONEXIÓN EXITOSA, LEYENDO DATOS..."
        
        # ----------------------------------------------------
        # 1. CONSULTA PARA EL TRABAJADOR ID = 1
        # ----------------------------------------------------
        cursor.execute("SELECT nombre, turno FROM trabajador WHERE id_trabajador = 1")
        resultado_t1 = cursor.fetchone() 
        
        if resultado_t1:
            nombre_t1 = resultado_t1[0]
            turno_t1 = resultado_t1[1]
        
        # ----------------------------------------------------
        # 2. CONSULTA PARA EL TRABAJADOR ID = 2
        # ----------------------------------------------------
        cursor.execute("SELECT nombre, turno FROM trabajador WHERE id_trabajador = 2")
        resultado_t2 = cursor.fetchone()
        
        if resultado_t2:
            nombre_t2 = resultado_t2[0]
            turno_t2 = resultado_t2[1]
        
        # Finaliza la conexión con éxito si ambas consultas se ejecutaron.
        estado_conexion = "CONEXIÓN Y LECTURA DE DATOS EXITOSA. 🎉"

    except Exception as e:
        estado_conexion = f"ERROR DE CONEXIÓN CRÍTICO: {e}"
        
    finally:
        if conn:
            conn.close() 

    # -----------------------------------------------------------------
    # PARTE CLAVE: Retornar la plantilla HTML (templates/index.html)
    # Pasando 4 variables de datos
    # -----------------------------------------------------------------
    return render_template('index.html', 
                           nombre1=nombre_t1,
                           turno1=turno_t1,
                           nombre2=nombre_t2,
                           turno2=turno_t2,
                           estado=estado_conexion)