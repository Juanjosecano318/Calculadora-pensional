import sys
sys.path.append( "src" )
import psycopg2
from model.usuario import *
sys.path.append("")
import SecretConfig
class ControladorUsuarios:

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        with open("sql/crear-usuarios.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorUsuarios.ObtenerCursor()
        with open("sql/eliminar-usuarios.sql", "r") as file:
            cursor.execute(file.read())
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarUsuario(usuario : Usuario):
        """ Recibe un a instancia de la clase Pension y la inserta en la tabla respectiva"""
        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute("""
        INSERT INTO Usuarios (
            cedula, nombre, base_settlement_income,
            current_legal_minimum_wage, pension_porcentage
        ) VALUES (%s, %s, %s, %s, %s)
        """, (
        usuario.cedula,
        usuario.nombre,
        usuario.base_settlement_income,
        usuario.current_legal_minimum_wage,
        usuario.pension_porcentage))
        
        cursor.connection.commit()

    def BuscarUsuarioCedula( cedula ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute(f"""
        SELECT cedula, nombre, base_settlement_income, current_legal_minimum_wage, pension_porcentage
        FROM Usuarios WHERE cedula = '{cedula}' """)
        fila = cursor.fetchone()
        return fila

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor