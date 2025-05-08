import psycopg2

# Do not expose your Neon credentials to the browser

PGHOST='ep-aged-paper-a4fyzrj0-pooler.us-east-1.aws.neon.tech'
PGDATABASE='Pensi%C3%B3n'
PGUSER='Pensi%C3%B3n_owner'
PGPASSWORD='npg_AO6GnMBjt4Jk'

conexion = psycopg2.connect(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)

cursor = conexion.cursor()
cursor.execute("SELECT cedula, nombre FROM Usuarios")
resultado = cursor.fetchall()


print (resultado)


"""Este archivo no se donde va, o como se llama, lo hice pero no se donde ubicarlo"""