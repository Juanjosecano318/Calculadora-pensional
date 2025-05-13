import sys
sys.path.append("src")
from controller.pension_controller import *
from model.pension import *

while True:
    print("que deseas hacer, para seleccionar ponga el numero que corresponde")
    print("1. insertar datos")
    print("2. buscar")
    print("3. modificar")
    
    opcion = input()
    if opcion == "1":
        cedula = int(input("ingrese su cedula"))
        base_settlement_income = int(input("Ingrese la base de liquidacion:"))
        current_legal_minimum_wage = int(input("Ingrese su salario minimo legal vigente:"))
        pension_porcentage = int(input("Ingrese el porcentaje de pensión:"))
        ControladorPension.InsertarPension(cedula, base_settlement_income, current_legal_minimum_wage, pension_porcentage)
    
    if opcion == "2":
        cedula = int(input("ingrese su cedula para buscar"))
        resultado = ControladorPension.BuscarUsuarioCedula(cedula)
        print(resultado)
    
    if opcion == "3":
        try:
            cedula = int(input("Ingrese la cédula del registro a modificar: "))
            
            # Buscar el registro actual
            pension_actual = ControladorPension.BuscarUsuarioCedula(cedula)
            
            if not pension_actual:
                print("No existe un registro con esa cédula")
                continue
            
            # Mostrar datos actuales
            print("\nDatos actuales:")
            print(f"1. Base de liquidación: {pension_actual.base_settlement_income}")
            print(f"2. Salario mínimo legal: {pension_actual.current_legal_minimum_wage}")
            print(f"3. Porcentaje de pensión: {pension_actual.pension_porcentage}")
            
            # Seleccionar campo a modificar
            campo = input("\n¿Qué campo desea modificar? (1-3): ")
            
            # Crear nueva pensión con los datos modificados
            nueva_base = pension_actual.base_settlement_income
            nuevo_salario = pension_actual.current_legal_minimum_wage
            nuevo_porcentaje = pension_actual.pension_porcentage
            
            if campo == "1":
                nueva_base = float(input("Nueva base de liquidación: "))
            elif campo == "2":
                nuevo_salario = float(input("Nuevo salario mínimo legal: "))
            elif campo == "3":
                nuevo_porcentaje = float(input("Nuevo porcentaje de pensión: "))
            else:
                print("Opción no válida")
                continue
            
            # Crear objeto Pension con los datos actualizados
            pension_modificada = Pension(
                cedula=pension_actual.cedula,
                base_settlement_income=nueva_base,
                current_legal_minimum_wage=nuevo_salario,
                pension_porcentage=nuevo_porcentaje
            )
            
            # Actualizar en la base de datos usando el controlador
            ControladorPension.ActualizarPension(pension_modificada)
            print("¡Registro modificado correctamente!")
            
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
        except Exception as e:
            print(f"Error al modificar el registro: {str(e)}")
