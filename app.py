from flask import Flask, render_template, request

import sys
sys.path.append("src")

from model.usuario import Usuario

from controller.usuarios_controller import ControladorUsuarios

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route('/buscar')
def buscar():
    return render_template("buscar.html")

@app.route('/resultado_busqueda')
def resultado_busqueda():
    cedula_param = request.args["cedula"]
    usuario = ControladorUsuarios.BuscarUsuarioCedula(cedula_param)

    return render_template('resultado_busqueda.html', usuario=usuario)


@app.route("/formulario", methods=["GET", "POST"])
def insertar_usuario():
    if request.method == "POST":
        # Tomar los datos del formulario
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        ibl = float(request.form["ibl"])
        salario_minimo = float(request.form["salario_minimo"])
        porcentaje_pension = float(request.form["porcentaje_pension"])

        # Crear un objeto Usuario
        nuevo_usuario = Usuario(
            cedula=cedula,
            nombre=nombre,
            base_settlement_income=ibl,
            current_legal_minimum_wage=salario_minimo,
            pension_porcentage=porcentaje_pension
        )

        # Insertar en la base de datos
        ControladorUsuarios.InsertarUsuario(nuevo_usuario)

    return render_template("formulario.html")

if __name__ == '__main__':
    app.run(debug=True)
















