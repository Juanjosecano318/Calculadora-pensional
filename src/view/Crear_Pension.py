<<<<<<< HEAD
import sys
sys.path.append("src")

from model.pension import Pension
from controller.pension_controller import ControladorPension



# Crear una instancia del Modelo

tarjeta = Pension(cedula = "", nombre = "", base_settlement_income = "", current_legal_minimum_wage = "", pension_porcentage = "")

# Pedir al usuario, los datos para llenar la instancia
Pension.cedula = input("Ingrese el numero de cédula: ")
Pension.nombre = input( "Ingrese el nombre del usuario: ")
Pension.base_settlement_income = input("Ingrese el ibl: ")
Pension.current_legal_minimum = input( input("Ingrese el salario minimo legal del usuario:" ))
Pension.pension_porcentage = input( input("Ingrese el porcentaje de pensión: "))

# Llamar al controlador para que inserte en la BD
ControladorPension.Insertar( Pension )

=======
import sys
sys.path.append("src")

from model.Pension import Pension
from controller.Usuarios_Controller import ControladorPension



# Crear una instancia del Modelo

tarjeta = Pension(cedula = "", nombre = "", base_settlement_income = "", current_legal_minimum_wage = "", pension_porcentage = "")

# Pedir al usuario, los datos para llenar la instancia
Pension.cedula = input("Ingrese el numero de cédula: ")
Pension.nombre = input( "Ingrese el nombre del usuario: ")
Pension.base_settlement_income = input("Ingrese el ibl: ")
Pension.current_legal_minimum = input( input("Ingrese el salario minimo legal del usuario:" ))
Pension.pension_porcentage = input( input("Ingrese el porcentaje de pensión: "))

# Llamar al controlador para que inserte en la BD
ControladorPension.Insertar( Pension )

>>>>>>> a43afe1d20d40cd9a90d55b9c4659cfa8716d34b
print( "La pensión fue generada y insertada exitosamente!")