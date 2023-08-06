import os
import sqlite3
from datetime import datetime
from flask import Flask, redirect, render_template, request, send_from_directory

app = Flask(__name__)

conection = sqlite3.connect("./python_sqlite.db", check_same_thread=False)
cursor = conection.cursor()


public_dir = os.path.join("public")
app.config["CARPETA"] = public_dir


@app.route("/uploads/<nombre_foto>")
def uploads(nombre_foto):
    return send_from_directory(app.config["CARPETA"], nombre_foto)


@app.route("/")
def index():
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    return render_template("empleados/index.html", empleados=empleados)


@app.route("/create")
def create():
    return render_template("empleados/create.html")


@app.route("/store", methods=["POST"])
def storage():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    foto = request.files["foto"]

    now = datetime.now().strftime("%Y%H%M%S")

    if foto.filename != "":
        foto.save("public/" + now + foto.filename)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empleados(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre text,
          correo text,
          foto text
        );
        """
    )
    cursor.execute(
        f"""
        INSERT INTO empleados (nombre, correo, foto)
        VALUES ('{nombre}', '{correo}', '{now + foto.filename}');
        """
    )
    conection.commit()
    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):
    cursor.execute(f"SELECT * FROM empleados WHERE id = {id}")
    empleado = cursor.fetchone()
    return render_template("empleados/edit.html", empleado=empleado)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    foto = request.files["foto"]

    now = datetime.now().strftime("%Y%H%M%S")

    if foto.filename != "":
        foto.save("public/" + now + foto.filename)
        cursor.execute(f"SELECT foto FROM empleados WHERE id = {id}")
        file = cursor.fetchone()
        os.remove(os.path.join(app.config["CARPETA"], file[0]))
        cursor.execute(
            f"""
            UPDATE empleados SET foto = '{now}{foto.filename}'
            WHERE id = {id}
            """
        )

    cursor.execute(
        f"""
        UPDATE empleados SET nombre='{nombre}', correo='{correo}'
        WHERE id = {id}
        """
    )
    conection.commit()
    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute(f"SELECT foto FROM empleados WHERE id = {id}")
    file = cursor.fetchone()
    os.remove(os.path.join(app.config["CARPETA"], file[0]))
    cursor.execute(f"DELETE FROM empleados WHERE id = {id}")
    conection.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
