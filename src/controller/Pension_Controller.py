import sys
sys.path.append( "src" )

import psycopg2
from model.Pension import *

sys.path.append("")
import SecretConfig

class ControladorPension :

    def CrearTabla(self):
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorPension().ObtenerCursor()

        cursor.execute("""create table Pension (
            cedula integer primary key,
            base_settlement_income real not null,
            current_legal_minimum_wage real not null,
            pension_porcentage real not null
        );""")
        cursor.connection.commit()

    def EliminarTabla(self):
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorPension().ObtenerCursor()

        cursor.execute("""drop table Pension""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarPension(self, pension : Pension ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        cursor = ControladorPension().ObtenerCursor()
        cursor.execute("""
        INSERT INTO Pension (
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


    def BuscarUsuarioCedula(self, cedula ):
        """ Trae un pension de la tabla de usuarios por la cedula """
        cursor = ControladorPension().ObtenerCursor()

        cursor.execute("""
        SELECT cedula, base_settlement_income,
        current_legal_minimum_wage, pension_porcentage
        FROM Pension WHERE cedula = %s;
        """, (cedula,))

        fila = cursor.fetchone()
        return fila

    def ObtenerCursor(self):
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor