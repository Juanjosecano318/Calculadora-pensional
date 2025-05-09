<<<<<<< HEAD
import sys
sys.path.append("src")

from model.usuario import Usuario
from controller.pension_controller import ControladorPension


# Crear una instancia del Modelo
calculadora = Usuario( cedula = "", nombre = "", base_settlement_income = "", 
                    current_legal_minimum_wage = "", pension_porcentage = "")


# Pedir al usuario los datos para llenar la instancia
Usuario.cedula = input("Ingrese la cédula del usuario: ")
Usuario.nombre = input("Ingrese el nombre del usuario: ")
Usuario.base_settlement_income = input(input("Ingrese el ingreso base de liquidación: "))
Usuario.current_legal_minimum_wage = input(input("Ingrese el salario mínimo legal vigente: "))
Usuario.pension_percentage = input(input("Ingrese el porcentaje de pensión: "))

# Llamar al controlador para que inserte en la BD
ControladorPension.InsertarUsuario(Usuario)

print("El usuario fue insertado exitosamente!")
=======
import sys
sys.path.append("src")

from model.Usuario import Usuario
from controller.Pension_Controller import ControladorUsuarios


# Crear una instancia del Modelo
calculadora = Usuario( cedula = "", nombre = "", base_settlement_income = "", 
                      current_legal_minimum_wage = "", pension_porcentage = "")


# Pedir al usuario los datos para llenar la instancia
Usuario.cedula = input("Ingrese la cédula del usuario: ")
Usuario.nombre = input("Ingrese el nombre del usuario: ")
Usuario.base_settlement_income = input(input("Ingrese el ingreso base de liquidación: "))
Usuario.current_legal_minimum_wage = input(input("Ingrese el salario mínimo legal vigente: "))
Usuario.pension_percentage = input(input("Ingrese el porcentaje de pensión: "))

# Llamar al controlador para que inserte en la BD
ControladorUsuarios.InsertarUsuario(Usuario)

print("El usuario fue insertado exitosamente!")
>>>>>>> a43afe1d20d40cd9a90d55b9c4659cfa8716d34b
