from flask import Flask, render_template, request, Blueprint
import sys
sys.path.append("src")

from model.usuario import Usuario
from controller.usuarios_controller import ControladorUsuarios
from view.view_web.vista_usuario import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

@app.route("/")
def Home():
    return render_template("index.html")

@app.errorhandler(Exception)
def controler_errores(err):
    return "ocurrio un error con los datos ingresados: " + str(err)

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
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        ibl = float(request.form["ibl"])
        salario_minimo = float(request.form["salario_minimo"])
        porcentaje_pension = float(request.form["porcentaje_pension"])

        nuevo_usuario = Usuario(
            cedula=cedula,
            nombre=nombre,
            base_settlement_income=ibl,
            current_legal_minimum_wage=salario_minimo,
            pension_porcentage=porcentaje_pension
        )

        ControladorUsuarios.InsertarUsuario(nuevo_usuario)

    return render_template("formulario.html")

@app.route('/modificar_usuario/<cedula>', methods=["GET", "POST"])
def modificar_usuario(cedula):
    # Obtener el usuario actual desde la base de datos
    usuario = ControladorUsuarios.BuscarUsuarioCedula(cedula)

    if request.method == "POST":
        # Actualizar los atributos con los nuevos valores del formulario
        usuario.nombre = request.form["nombre"]
        usuario.base_settlement_income = float(request.form["ibl"])
        usuario.current_legal_minimum_wage = float(request.form["salario_minimo"])
        usuario.pension_porcentage = float(request.form["porcentaje_pension"])

        # Guardar cambios en la base de datos
        ControladorUsuarios.ActualizarCampo(cedula, "nombre", usuario.nombre)
        ControladorUsuarios.ActualizarCampo(cedula, "base_settlement_income", usuario.base_settlement_income)
        ControladorUsuarios.ActualizarCampo(cedula, "current_legal_minimum_wage", usuario.current_legal_minimum_wage)
        ControladorUsuarios.ActualizarCampo(cedula, "pension_porcentage", usuario.pension_porcentage)

        return render_template("resultado_busqueda.html", usuario=usuario)

    return render_template("modificar_usuario.html", usuario=usuario)

@app.route('/crear_tabla')
def crear_tablas():
    try:
        ControladorUsuarios.CrearTabla()
        return "<h1>Tablas creadas exitosamente</h1><a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1><a href='/'>Volver al inicio</a>"
if __name__ == '__main__':
    app.run(debug=True)
















