from flask import Flask, render_template, request

import sys
sys.path.append("src")

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
    cedula = request.args.get("cedula")  # en minúscula y más seguro
    ControladorUsuarios.BuscarUsuarioCedula(cedula)
    return render_template('resultado_busqueda.html', cedula=cedula)

# Puedes agregar aquí todas las demás rutas que ya tienes

if __name__ == '__main__':
    app.run(debug=True)
















