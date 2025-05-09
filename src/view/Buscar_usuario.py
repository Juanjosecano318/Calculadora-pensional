<<<<<<< HEAD
import sys
sys.path.append("src")

from model.usuario import Usuario
from controller.usuarios_controller import ControladorUsuarios

try:
    cedula = input("Ingrese la cedula del usuario que desea buscar: ")
    usuario_buscado = ControladorUsuarios.BuscarUsuario( cedula )
    print(  f"Usuario encontrado : {usuario_buscado.nombre} {usuario_buscado.cedula}" )
except Exception as err:
    print("Error : " )
=======
import sys
sys.path.append("src")

from model.Usuario import Usuario
from controller.Pension_Controller import ControladorUsuarios

try:
    cedula = input("Ingrese la cedula del usuario que desea buscar: ")
    usuario_buscado = ControladorUsuarios.BuscarUsuario( cedula )
    print(  f"Usuario encontrado : {usuario_buscado.nombre} {usuario_buscado.cedula}" )
except Exception as err:
    print("Error : " )
>>>>>>> a43afe1d20d40cd9a90d55b9c4659cfa8716d34b
    print( str( err ) )