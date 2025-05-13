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
        cedula = int(input("ingrese su cedila para buscar"))
        resultado = ControladorPension.BuscarUsuarioCedula(cedula)
        print(resultado)
    
    if opcion == "3":
        ...
