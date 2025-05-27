from flask import Blueprint, render_template, request, redirect
from controller.usuarios_controller import ControladorUsuarios
from model.usuario import Usuario

plano = Blueprint('vista_usuario', __name__)

@plano.route("/")
def Home():
    return render_template("index.html")

@plano.route('/formulario', methods=["GET", "POST"])
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
        return redirect('/formulario')
    
    return render_template("formulario.html")

@plano.route('/buscar')
def buscar():
    return render_template("buscar.html")

@plano.route('/resultado_busqueda') 
def resultado_busqueda():
    cedula_param = request.args.get("cedula")
    usuario = ControladorUsuarios.BuscarUsuarioCedula(cedula_param)
    return render_template("resultado_busqueda.html", usuario=usuario)

@plano.route('/modificar_usuario/<cedula>', methods=["GET", "POST"]) 
def modificar_usuario(cedula):
    usuario = ControladorUsuarios.BuscarUsuarioCedula(cedula)
    if request.method == "POST":
        usuario.nombre = request.form["nombre"]
        usuario.base_settlement_income = float(request.form["ibl"])
        usuario.current_legal_minimum_wage = float(request.form["salario_minimo"])
        usuario.pension_porcentage = float(request.form["porcentaje_pension"])

        ControladorUsuarios.ActualizarCampo(cedula, "nombre", usuario.nombre)
        ControladorUsuarios.ActualizarCampo(cedula, "base_settlement_income", usuario.base_settlement_income)
        ControladorUsuarios.ActualizarCampo(cedula, "current_legal_minimum_wage", usuario.current_legal_minimum_wage)
        ControladorUsuarios.ActualizarCampo(cedula, "pension_porcentage", usuario.pension_porcentage)

        return render_template("resultado_busqueda.html", usuario=usuario)
    
    return render_template("modificar_usuario.html", usuario=usuario)

@plano.route('/crear_tabla')
def crear_tablas():
    try:
        ControladorUsuarios.CrearTabla()
        return "<h1>Tabla de usuarios creada exitosamente</h1><a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1><a href='/'>Volver al inicio</a>"
    
@plano.errorhandler(Exception)
def controler_errores(err):
    return f"Ocurrió un error con los datos ingresados: {str(err)}"