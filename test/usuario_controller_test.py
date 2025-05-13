import unittest
import sys
sys.path.append("src")
from controller.usuarios_controller import ControladorUsuarios
from model.usuario import *

class TestUsuarios(unittest.TestCase):

    def setUpClass():
        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()
    
    def test_insert_1(self):
        usuario = Usuario(15000257, "Juan Perez", 1500000, 2000000, 65)
        ControladorUsuarios.InsertarUsuario(usuario)
        buscar_cedula = ControladorUsuarios.BuscarUsuarioCedula(usuario.cedula)
        self.assertTrue(buscar_cedula.EsIgual(usuario))

    def test_insert_2(self):
        usuario = Usuario(
            78956321, "Maria Gomez", 3000000, 1423500, 85
        )
        ControladorUsuarios.InsertarUsuario(usuario)
        buscar_cedula = ControladorUsuarios.BuscarUsuarioCedula(usuario.cedula)
        self.assertTrue(buscar_cedula.EsIgual(usuario))

    def test_insert_3(self):
        usuario = Usuario(
            78965152, "Carlos Ruiz", 5000000, 11500000, 75.5
        )
        ControladorUsuarios.InsertarUsuario(usuario)
        buscar_cedula = ControladorUsuarios.BuscarUsuarioCedula(usuario.cedula)
        self.assertTrue(buscar_cedula.EsIgual(usuario))
    
    def test_modificar_1(self):
        usuario_original = Usuario(40404040, "Ana Torres", 1200000, 1300000, 60)
        ControladorUsuarios.InsertarUsuario(usuario_original)

        # Simula modificación reinicializando la tabla y reinserta con nuevos valores
        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()
        usuario_modificado = Usuario(40404040, "Ana Torres Modificado", 1500000, 1300000, 65)
        ControladorUsuarios.InsertarUsuario(usuario_modificado)

        resultado = ControladorUsuarios.BuscarUsuarioCedula(40404040)
        self.assertTrue(resultado.EsIgual(usuario_modificado))

    def test_modificar_2(self):
        usuario_original = Usuario(50505050, "Pedro Sanchez", 2000000, 1400000, 70)
        ControladorUsuarios.InsertarUsuario(usuario_original)

        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()
        usuario_modificado = Usuario(50505050, "Pedro Sanchez Actualizado", 2200000, 1400000, 75)
        ControladorUsuarios.InsertarUsuario(usuario_modificado)

        resultado = ControladorUsuarios.BuscarUsuarioCedula(50505050)
        self.assertTrue(resultado.EsIgual(usuario_modificado))

    def test_modificar_3(self):
        usuario_original = Usuario(60606060, "Luisa Fernandez", 1800000, 1350000, 68)
        ControladorUsuarios.InsertarUsuario(usuario_original)

        ControladorUsuarios.EliminarTabla()
        ControladorUsuarios.CrearTabla()
        usuario_modificado = Usuario(60606060, "Luisa Fernandez Nueva", 2000000, 1350000, 70)
        ControladorUsuarios.InsertarUsuario(usuario_modificado)

        resultado = ControladorUsuarios.BuscarUsuarioCedula(60606060)
        self.assertTrue(resultado.EsIgual(usuario_modificado))
    
    def test_buscar_1(self):
        cedula = 15000257
        esperado = Usuario(cedula, "Juan Perez Buscar", 1500000, 2000000, 65)
        ControladorUsuarios.InsertarUsuario(esperado)
        resultado = ControladorUsuarios.BuscarUsuarioCedula(cedula)
        self.assertTrue(resultado.EsIgual(esperado))
    
    def test_buscar_2(self):
        cedula = 78956321
        esperado = Usuario(cedula, "Maria Gomez Buscar", 3000000, 1423500, 85)
        ControladorUsuarios.InsertarUsuario(esperado)
        resultado = ControladorUsuarios.BuscarUsuarioCedula(cedula)
        self.assertTrue(resultado.EsIgual(esperado))
    
    def test_buscar_3(self):
        cedula = 78965152
        esperado = Usuario(cedula, "Carlos Ruiz Buscar", 5000000, 11500000, 75.5)
        ControladorUsuarios.InsertarUsuario(esperado)
        resultado = ControladorUsuarios.BuscarUsuarioCedula(cedula)
        self.assertTrue(resultado.EsIgual(esperado))
        
if __name__ == "__main__":
    unittest.main()