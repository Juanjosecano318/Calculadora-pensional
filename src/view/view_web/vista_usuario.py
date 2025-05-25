from flask import Blueprint, render_template, request

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

@blueprint.route("/index")  # Esta ruta ya no entra en conflicto
def vista_usuarios():
    return render_template("index.html")