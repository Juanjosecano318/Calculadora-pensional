import sys
sys.path.append("src")

from model.Usuario import Usuario
from controller.Usuarios_Controller import ControladorUsuarios

try:
    cedula = input("Ingrese la cedula del usuario que desea buscar: ")
    usuario_buscado = ControladorUsuarios.BuscarUsuario( cedula )
    print(  f"Usuario encontrado : {usuario_buscado.nombre} {usuario_buscado.cedula}" )
except Exception as err:
    print("Error : " )
    print( str( err ) )