
# 🍽️ **Sistema Web de Restaurante — Flask + Supabase + PostgreSQL**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.5-blue?logo=postgresql)](https://www.postgresql.org/)
[![Supabase](https://img.shields.io/badge/Supabase-2025-green?logo=supabase)](https://supabase.com/)

Este proyecto es una aplicación web completa para la gestión de un restaurante, permitiendo registrar clientes, ver el menú, agregar pedidos y administrarlos de forma sencilla.
Está desarrollado usando Python (Flask) en el backend, HTML + CSS en el frontend, y Supabase (PostgreSQL) como base de datos.

---

# 🎯 **Objetivos del Proyecto**

* Registro e inicio de sesión de clientes
* Visualización del menú de platillos
* Gestión completa de pedidos (agregar, modificar, eliminar)
* Confirmación de pedidos y cálculo de totales
* Panel de usuario (dashboard) para seguimiento de pedidos

---

# 🖼 **Capturas de Pantalla**

### 1. Página de Inicio 

<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/2fa55aba-7fc4-460d-b199-9a4f230c11b5" />

### 2. Login

<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/e3c1d228-2f91-4c86-8c5f-c48ccda1678a" />

### 3. Registro de Clientes

<img width="1919" height="877" alt="image" src="https://github.com/user-attachments/assets/7da68f99-cba9-4307-bc5c-50d492365f25" />
<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/3b8a7cb3-fb43-481b-8d44-c30613dc982a" />

### 4. Menú de Platillos

<img width="1914" height="882" alt="image" src="https://github.com/user-attachments/assets/a12bddca-3eb0-4930-ab84-b1d0b53ade3c" />

### 5. Carrito de Pedidos

<img width="1919" height="877" alt="image" src="https://github.com/user-attachments/assets/773f63ed-801c-4979-adbe-6b2a705a9b44" />


### 6. Dashboard del Usuario

<img width="1919" height="877" alt="image" src="https://github.com/user-attachments/assets/ba077b20-949c-4c45-a521-46909d01f6ce" />

> 🔹 Puedes reemplazar los enlaces de placeholder con capturas reales de tu aplicación.

---

# 🧱 **Tecnologías Utilizadas**

* **Python (Flask)**: Backend web, manejo de rutas y sesiones
* **HTML / CSS**: Interfaz visual (`static/style.css`)
* **Jinja2**: Plantillas dinámicas
* **PostgreSQL (Supabase)**: Base de datos relacional
* **dotenv**: Manejo de variables de entorno (`.env`)

---

# 📁 **Estructura del Proyecto**

```
restaurante/
│
├── static/
│   └── style.css             # Estilos personalizados
│
├── templates/
│   ├── index.html            # Página principal / login
│   ├── register.html         # Registro de clientes
│   ├── menu.html             # Menú de platillos
│   ├── mi_pedido.html        # Carrito de pedidos
│   └── dashboard.html        # Panel de usuario
│
├── .gitignore                # Archivos ignorados por Git
├── app.py                    # Aplicación Flask
├── .env                      # Variables de entorno
├── requirements.txt          # Dependencias
└── README.md                 # Documentación
```

**Archivo `.gitignore` sugerido:**

```
__pycache__/
*.pyc
*.pyo
*.env
venv/
*.sqlite3
```

---

# 🧾 **Modelo de Base de Datos**

### 🧑 **Clientes**

| Campo          | Tipo      |
| -------------- | --------- |
| id_cliente     | SERIAL PK |
| nombre         | VARCHAR   |
| correo         | VARCHAR   |
| telefono       | VARCHAR   |
| contrasena     | VARCHAR   |
| calle          | VARCHAR   |
| numero         | VARCHAR   |
| colonia        | VARCHAR   |
| ciudad         | VARCHAR   |
| fecha_registro | TIMESTAMP |

### 🍽️ **Platillos**

| Campo       | Tipo      |
| ----------- | --------- |
| id_platillo | SERIAL PK |
| nombre      | VARCHAR   |
| precio      | NUMERIC   |
| categoria   | VARCHAR   |
| descripcion | VARCHAR   |

### 🧾 **Pedidos**

| Campo       | Tipo       |
| ----------- | ---------- |
| id_pedido   | SERIAL PK  |
| id_cliente  | INTEGER FK |
| total       | NUMERIC    |
| tipo_pedido | VARCHAR    |
| fecha       | TIMESTAMP  |

---

# 🔧 **Flujo de la Aplicación**

1. Cliente inicia sesión (`/`) o se registra (`/register`)
2. Accede al menú (`/menu`) y selecciona platillos
3. Agrega platillos al carrito (`/agregar_pedido`)
4. Visualiza y modifica el pedido (`/mi_pedido`)
5. Confirma el pedido, que se registra en la base de datos (`/confirmar_pedido`)
6. Puede cerrar sesión (`/logout`)

---

# 🧪 **Cómo Ejecutar Localmente**

```bash
# Clonar el repositorio
git clone https://github.com/elimon2006-ux/restaurante_vulnerable.git
cd restaurante_vulnerable

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
DATABASE_URL=postgresql://usuario:password@host:port/dbname
SECRET_KEY=clave-secreta

# Ejecutar aplicación
python app.py
```

Abrir navegador en `http://127.0.0.1:5000/`

---

# 🎨 **Funcionalidades Implementadas**

* Login y registro de clientes
* Menú dinámico de platillos
* Agregar, modificar y eliminar items del pedido
* Confirmación de pedidos y cálculo de totales
* Dashboard de usuario
* Interfaz sencilla y responsive

---

# 🪪 **Licencia**

Proyecto educativo. Libre para estudiar, modificar y mejorar.


