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
    
    elif opcion == "3":
        try:
            cedula = int(input("Cédula a modificar: "))
            
            print("\n¿Qué datos modificar?")
            print("1. Base de liquidación")
            print("2. Salario mínimo")
            print("3. Porcentaje de pensión")
            
            nuevo_campo = input("Opción (1-3): ")
            nuevo_valor = float(input("Nuevo valor: "))
            
            if nuevo_campo == "1":
                ControladorPension.ActualizarCampo(cedula, "base_settlement_income", nuevo_valor)
            elif nuevo_campo == "2":
                ControladorPension.ActualizarCampo(cedula, "current_legal_minimum_wage", nuevo_valor)
            elif nuevo_campo == "3":
                ControladorPension.ActualizarCampo(cedula, "pension_porcentage", nuevo_valor)
            else:
                print("Opción no válida")
                continue
                
            print("¡Dato actualizado!")
            
        except ValueError:
            print("Error: Ingrese valores numéricos")
        except Exception as e:
            print(f"Error: {e}")