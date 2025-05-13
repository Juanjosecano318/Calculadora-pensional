
import unittest
import sys
sys.path.append("src")
from controller.pension_controller import ControladorPension
from model.pension import *

class TestPension(unittest.TestCase):

    def setUpClass():
        ControladorPension.EliminarTabla()
        ControladorPension.CrearTabla()
    
    def test_insert_1(self):
        pension = Pension(15000257, 1500000, 2000000, 65)
        ControladorPension.InsertarPension(pension)
        buscar_cedula = ControladorPension.BuscarUsuarioCedula(pension.cedula)
        self.assertTrue(buscar_cedula.EsIgual(pension))

    def test_insert_2(self):
        pension = Pension(
            78956321, 3000000, 1423500, 85
        )
        ControladorPension.InsertarPension (pension)
        buscar_cedula = ControladorPension.BuscarUsuarioCedula (pension.cedula)
        self.assertTrue (buscar_cedula.EsIgual(pension))

    def test_insert_3(self):
        pension = Pension(
            78965152, 5000000, 11500000, 75.5
        )
        ControladorPension.InsertarPension (pension)
        buscar_cedula = ControladorPension.BuscarUsuarioCedula(pension.cedula)
        self.assertTrue (buscar_cedula.EsIgual(pension))
    
    def test_modificar_1(self):
        pension_original = Pension(40404040, 1200000, 1300000, 60)
        ControladorPension.InsertarPension(pension_original)

        # Simula modificación reinicializando la tabla y reinserta con nuevos valores
        ControladorPension.EliminarTabla()
        ControladorPension.CrearTabla()
        pension_modificada = Pension(40404040, 1500000, 1300000, 65)
        ControladorPension.InsertarPension(pension_modificada)

        resultado = ControladorPension.BuscarUsuarioCedula(40404040)
        self.assertTrue(resultado.EsIgual(pension_modificada))

    def test_modificar_2(self):
        pension_original = Pension(50505050, 2000000, 1400000, 70)
        ControladorPension.InsertarPension(pension_original)

        ControladorPension.EliminarTabla()
        ControladorPension.CrearTabla()
        pension_modificada = Pension(50505050, 2200000, 1400000, 75)
        ControladorPension.InsertarPension(pension_modificada)

        resultado = ControladorPension.BuscarUsuarioCedula(50505050)
        self.assertTrue(resultado.EsIgual(pension_modificada))

    def test_modificar_3(self):
        pension_original = Pension(60606060, 1800000, 1350000, 68)
        ControladorPension.InsertarPension(pension_original)

        ControladorPension.EliminarTabla()
        ControladorPension.CrearTabla()
        pension_modificada = Pension(60606060, 2000000, 1350000, 70)
        ControladorPension.InsertarPension(pension_modificada)

        resultado = ControladorPension.BuscarUsuarioCedula(60606060)
        self.assertTrue(resultado.EsIgual(pension_modificada))
    
    def test_buscar_1(self):
        cedula = 15000257
        esperada = Pension(cedula, 1500000, 2000000, 65)
        ControladorPension.InsertarPension(esperada)
        resultado = ControladorPension.BuscarUsuarioCedula(cedula)
        self.assertTrue(resultado.EsIgual(esperada))
    
    def test_buscar_2(self):
        cedula = 78956321
        esperada = Pension(cedula, 3000000, 1423500, 85)
        ControladorPension.InsertarPension(esperada)
        resultado = ControladorPension.BuscarUsuarioCedula(cedula)
        self.assertTrue(resultado.EsIgual(esperada))
    
    def test_buscar_3(self):
        cedula = 78965152
        esperada = Pension(cedula, 5000000, 11500000, 75.5)
        ControladorPension.InsertarPension(esperada)
        resultado = ControladorPension.BuscarUsuarioCedula(cedula)
        self.assertTrue(resultado.EsIgual(esperada))
        
if __name__ == "__main__":
    unittest.main()