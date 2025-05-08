import sys
sys.path.append( "src" )

import psycopg2

from model.Pension import Pension
import SecretConfig

class ControladorPension:

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorPension.ObtenerCursor()

        cursor.execute("""create table Usuarios (
    cedula integer primary key,
    nombre text not null,
    base_settlement_income real not null,
    current_legal_minimum_wage real not null,
    pension_porcentage real not null
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorPension.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarUsuario( usuario : Pension ):
        """ Recibe un a instancia de la clase Pension y la inserta en la tabla respectiva"""
        cursor = ControladorPension.ObtenerCursor()
        cursor.execute( f"""insert into usuarios (cedula, nombre, base_settlement_income,
                       current_legal_minimum_wage, pension_porcentage)
                        values ('{usuario.cedula}', '{usuario.nombre}', '{usuario.base_settlement_income}',  
                            '{usuario.current_legal_minimun_wage}', '{usuario.pension_porcentage}'""" )
                        

        cursor.connection.commit()

    def BuscarUsuarioCedula( cedula ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorPension.ObtenerCursor()

        cursor.execute(f"""select cedula, nombre, base_settlement_income, current_legal_minimum_wage, pension_porcentage)
        from usuarios where cedula = '{cedula}'""" )
        fila = cursor.fetchone()
        resultado = Pension( cedula=fila[0], nombre=fila[1], base_settlement=fila[2], current_legal_minimum_wage=fila[3], pension_porcentage=fila[4] )
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor