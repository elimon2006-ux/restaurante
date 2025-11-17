from flask import Flask, render_template, request, redirect, session, url_for, flash
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Conexión a Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------- ROUTES ----------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        contrasena = request.form["contrasena"]
        calle = request.form["calle"]
        numero = request.form["numero"]
        colonia = request.form["colonia"]
        ciudad = request.form["ciudad"]

        # Guardar en Supabase
        supabase.table("clientes").insert({
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "contrasena": contrasena,
            "calle": calle,
            "numero": numero,
            "colonia": colonia,
            "ciudad": ciudad
        }).execute()

        flash("Registro exitoso. Ahora inicia sesión.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        contrasena = request.form["contrasena"]

        # Verificar credenciales
        user = (
            supabase.table("clientes")
            .select("*")
            .eq("correo", correo)
            .eq("contrasena", contrasena)
            .execute()
        )

        if len(user.data) == 1:
            session["user"] = user.data[0]
            return redirect(url_for("dashboard"))
        else:
            flash("Credenciales incorrectas", "danger")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# RUN
if __name__ == "__main__":
    app.run(debug=True)
