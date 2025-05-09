import sys
sys.path.append( "src" )

import psycopg2
from model.pension import *

sys.path.append("")
import SecretConfig

class ControladorPension :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorPension.ObtenerCursor()
        
        cursor.execute("""create table if not exists Pensiones (
        cedula integer primary key,
        base_settlement_income real not null,
        current_legal_minimum_wage real not null,
        pension_porcentage real not null);""")
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorPension.ObtenerCursor()
        with open("sql/eliminar-pensiones.sql", "r") as file:
            cursor.execute(file.read())
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarPension(pension : Pension ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        cursor = ControladorPension.ObtenerCursor()
        cursor.execute("""
        INSERT INTO Pensiones (
            cedula,
            base_settlement_income,
            current_legal_minimum_wage,
            pension_porcentage
        ) VALUES (%s, %s, %s, %s)
        """, (
        pension.cedula,
        pension.base_settlement_income,
        pension.current_legal_minimum_wage,
        pension.pension_porcentage))

        cursor.connection.commit()


    def BuscarUsuarioCedula(cedula ):
        """ Trae un pension de la tabla de usuarios por la cedula """
        cursor = ControladorPension.ObtenerCursor()

        cursor.execute("""
        SELECT cedula, base_settlement_income,
        current_legal_minimum_wage, pension_porcentage
        FROM Pensiones WHERE cedula = %s;
        """, (cedula,))

        fila = cursor.fetchone()
        resultado = Pension(fila[0],fila[1],fila[2],fila[3])
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor