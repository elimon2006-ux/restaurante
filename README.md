# 🍽️ **Sistema Web de Restaurante — Flask + Supabase + PostgreSQL + SQLAlchemy (ORM)**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.5-blue?logo=postgresql)](https://www.postgresql.org/)
[![Supabase](https://img.shields.io/badge/Supabase-2025-green?logo=supabase)](https://supabase.com/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQL_SQLAlchemy-red)](https://www.sqlalchemy.org/)

Este proyecto es una **aplicación web completa para la gestión de un restaurante**, que permite registrar clientes, iniciar sesión, visualizar el menú, agregar pedidos y administrarlos de forma sencilla.

Está desarrollado con **Flask** en el backend, **HTML + CSS + Jinja2** en el frontend y **Supabase (PostgreSQL)** como base de datos. Para el acceso a datos se utiliza **SQLAlchemy (ORM)**, principalmente en el módulo de **login y registro de clientes**.

---

# 🎯 **Objetivos del Proyecto**

* Registro e inicio de sesión de clientes
* Uso de ORM (SQLAlchemy) para el manejo de usuarios
* Visualización del menú de platillos por categorías
* Gestión completa de pedidos (carrito)
* Confirmación de pedidos y cálculo automático de totales
* Panel de usuario (dashboard)

---

# 🖼 **Capturas de Pantalla**

### 1. Página de Inicio

<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/acc0bc9e-596e-44e7-a424-a7ae6c686204" />

### 2. Login

<img width="1919" height="877" alt="image" src="https://github.com/user-attachments/assets/01f6ee20-fc81-4ac6-af35-09292140a7b9" />


### 3. Registro de Clientes

<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/ebf1e82c-39ab-40df-8832-1b7be2f68617" />
<img width="1919" height="879" alt="image" src="https://github.com/user-attachments/assets/8f5d03da-f842-4860-bc2d-01dd898440ff" />


### 4. Menú de Platillos

<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/c72ed1d7-dedc-4be9-905b-57a0620cc50b" />

### Se divide en 4 categorias
* TACOS
* COMIDA CASERA
* BEBIDAS
* POSTRES

### 5. Carrito de Pedidos

<img width="1919" height="872" alt="image" src="https://github.com/user-attachments/assets/3370829c-275e-449a-b2fe-16e9c4d95735" />

### 6. Dashboard del Usuario

<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/27f70cf3-a0bb-4638-a266-1a0652423700" />


---

# 🧱 **Tecnologías Utilizadas**

* **Python + Flask**: Backend web y manejo de rutas
* **SQLAlchemy (ORM)**: Acceso a base de datos usando modelos
* **PostgreSQL (Supabase)**: Base de datos relacional
* **HTML / CSS**: Interfaz visual
* **Jinja2**: Plantillas dinámicas
* **dotenv**: Variables de entorno

---

# 📁 **Estructura del Proyecto**

```
mi_restaurante/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # Rutas Flask
│   ├── database.py        # Conexión ORM (SQLAlchemy)
│   ├── models.py          # Modelos ORM
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── menu.html
│       ├── mi_pedido.html
│       └── dashboard.html
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🧾 **Base de Datos y ORM**

La base de datos está en **PostgreSQL (Supabase)** y el acceso se realiza mediante **SQLAlchemy**.

### Ejemplo de modelo ORM (Cliente)

```python
class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    correo = Column(String(100), unique=True)
    telefono = Column(String(15))
    contrasena = Column(String(200))
    calle = Column(String(50))
    numero = Column(String(10))
    colonia = Column(String(50))
    ciudad = Column(String(50))
```

🔹 **ORM se usa principalmente en:**

* Registro de clientes
* Login
* Dashboard

🔹 **SQL directo se mantiene para:**

* Menú
* Pedidos
* Consultas complejas

---

# 🔧 **Flujo de la Aplicación**

1. Registro de cliente (ORM)
2. Login (ORM)
3. Acceso al menú solo con sesión iniciada
4. Agregar platillos al carrito
5. Confirmar pedido
6. Visualizar datos del usuario en dashboard
7. Cerrar sesión

---

# 🧪 **Ejecución Local**

```bash
git clone https://github.com/elimon2006-ux/restaurante.git
cd mi_restaurante

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# .env
DATABASE_URL=postgresql://user:password@host:5432/postgres
SECRET_KEY=clave_secreta

python -m app.main
```

Abrir en: `http://127.0.0.1:5000/`

---

# 🎨 **Funcionalidades Implementadas**

* Login y registro de clientes
* Menú dinámico de platillos
* Agregar, modificar y eliminar items del pedido
* Confirmación de pedidos y cálculo de totales
* Dashboard de usuario
* Interfaz sencilla y responsive

---

# 🔐 **Seguridad y Buenas Prácticas (Aplicación NO Vulnerable)**

Este proyecto **no es una página vulnerable**, ya que implementa múltiples medidas de seguridad a nivel backend y base de datos:

### ✅ Autenticación segura

* Contraseñas **encriptadas** usando `werkzeug.security.generate_password_hash`
* Verificación segura con `check_password_hash`
* Nunca se almacenan contraseñas en texto plano

### ✅ Protección contra SQL Injection

* Uso de **ORM (SQLAlchemy)** para consultas críticas como login y registro
* El ORM genera consultas parametrizadas automáticamente
* No se concatenan strings SQL manualmente

### ✅ Manejo seguro de sesiones

* Uso de `Flask session` con `SECRET_KEY`
* Acceso a rutas protegidas solo si el usuario inició sesión
* Cierre de sesión correcto (`session.clear()`)

### ✅ Validaciones de datos

* Restricciones en la base de datos (PRIMARY KEY, UNIQUE, CHECK, FOREIGN KEY)
* Validación de existencia de correo antes del registro
* Manejo de errores y mensajes flash

### ✅ Protección de credenciales

* Uso de archivo `.env` (no versionado)
* Variables sensibles fuera del código fuente

### ✅ Separación de responsabilidades

* ORM solo para datos críticos (clientes)
* Supabase usado únicamente para datos públicos (menú)
* Estructura modular (`models.py`, `database.py`, `main.py`)

### 🔒 Resultado

Este sistema cumple con principios básicos de **seguridad web**, evitando:

* SQL Injection
* Exposición de contraseñas
* Acceso no autorizado
* Manipulación directa de datos

---

# 🪪 **Licencia**

Proyecto educativo — libre para estudiar, modificar y mejorar.
