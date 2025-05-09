
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
    

if __name__ == "__main__":
    unittest.main()