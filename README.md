## Nombres de los creadores del repositorio: 
- Kevin Mateo Gomez Diez
- Sara Rojas Martínez

## Nombres, segunda entrega:
- Heiver David Ruales Luna
- Mariana Lopera Correa

#Nombres entrega 5 
-juan jose cano giraldo
-juan pablo tafur 
Aplicacion web render:
https://calculadora-pensional-6mn0.onrender.com

# Calculadora-pensional
En este repositorio se podrá encontrar toda la información acerca de la calculadora pensional, este proyecto tiene como objetivo proporcionar una herramienta intuitiva y eficiente para calcular la pensión y simulaciones personalizas para cada usuario. 

Entrevista sobre las pensiones: https://drive.google.com/file/d/1enmZgatAiFyT37SUNeuEhobB0pi-XEJx/view?usp=sharing

El cálculo de la pensión se basa en el Ingreso Base de Liquidación (IBL) y la tasa de reemplazo, que depende del número de semanas cotizadas y del IBL en relación con el Salario Mínimo Legal Vigente.

## Arquitectura:
El proyecto tiene una estructura donde todos los archivos estan separados por carpetas las cuales son: model, view\console y test. Además, hay un archivo .gitignore el cual a la hora de hacer los commits y los pushs va a ignorar las carpetas con nombre __pycache__.
También, se agregó un archivo de excel el cual tiene la información de los casos de prueba de la calculadora pensional. 

## Instrucciones para ejecutar las pruebas unitarias:
* Se ingresa a la carpeta test
* Luego, se ingresa al archivo Pension_Calculate_Test.py
* Y por último, se ejecuta el código

## Instrucciones para ejecutar la interfaz de Consola:
* Se ingresa a la carpeta view\console
* Se accede a la carpeta console
* Se ingresa al archivo Pension_Console.py
* Se ejecuta el código
* Se ingresa el valor del ibl
* Despues, se ingresa el valor del porcentaje de pensión
* Luego, se ingresa el valor del salario mínimo legal vigente
* Y por ultimo se muestra el valor total de la pensión

## Entradas:
* Base de liquidación
* Porcentaje de pensión
* Salario minimo legal vigente

## Proceso:
* Se ejecuta el archivo Pension_Console.py para iniciar la ejecución
* Se ingresan los valores pedidos
* El programa convierte los valores a floats
* Se calcula la tasa de remplazo
* Se multiplica el ingreso de base de liquidación por la tasa de remplazo

## Salidas:
* Se muestra el total de la pensión mensual

## Como ejecutar desde consola/terminal:
e clona el proyecto luego ingresa a la carpeta raiz (calculadora-pensional), desde la terminal usando el comando "cd" y se pone la ruta en donde se guardo la carpeta raiz, la ruta se obtine copiando la direccion desde la carpeta raiz, y desde la teminal se ejecuta el siguiente comando:
```
py src\view\console\Pension_Console.py
```

## Como ejecutar las pruebas (test) desde la teminal:
Se clona el proyecto luego ingresa a la carpeta raiz (calculadora-pensional), desde la terminal usando el comando "cd" y se pone la ruta en donde se guardo la carpeta raiz, la ruta se obtine copiando la direccion desde la carpeta raiz, y desde la teminal se ejecuta el siguiente comando:
```
py test\Pension_Calculate_Test.py
```

## Instrucciones para ejecutar la interfaz gráfica (GUI):
Asegúrate de tener instalado el framework Kivy. Si no lo tienes, instálalo con el siguiente comando:
```
pip install kivy
```
Luego, sigue estos pasos:
1. Clona el repositorio y navega a la carpeta raíz del proyecto (calculadora-pensional) desde la terminal.
2. Desde la terminal, ejecuta el siguiente comando para abrir la interfaz gráfica:
```
py src/view/gui/pension_gui.py
```
Se abrirá una ventana en la que deberás ingresar:

- El Ingreso Base de Liquidación (IBL).

- El Porcentaje de pensión que aplicarás al IBL.

- El Salario Mínimo Mensual Legal Vigente (SMMLV) (este se autocompleta con el valor por defecto de $1,300,000, por lo que no es necesario modificarlo).

Haz clic en "Calcular" para obtener el valor estimado de la pensión mensual.


También puedes usar el botón "Limpiar" para reiniciar los campos o "Ayuda" para ver una explicación detallada del funcionamiento de la calculadora.



## Prerrequisitos para la conexión con la base de datos:

Instale el paquete psycopg2 con:
```
pip install psycopg2
```

Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso

En el archivo SecretConfig.py establezca los valores que se necesitan para poder hacer la conexión con la base de datos.

Antes de ejecutar la aplicación por primera vez, debe correr las pruebas unitarias, para que se creen las tablas en la base de datos

Por seguridad, agrega `SecretConfig.py` a tu archivo `.gitignore` para evitar subirlo al repositorio:

Ejemplo:
```
.gitignore
SecretConfig.py
```

- Recuerde poner en un archivo de python los datos de conexion y guardar como SecretConfig.py

PGHOST='PONGA EL HOST DE LA BD AQUI'

PGDATABASE='PONGA EL NOMBRE DE LA BD AQUI'

PGUSER='PONGA EL USUARIO AQUI'

PGPASSWORD='PONGA LA CONTRASEÑA AQUI'

PGPORT=5432

---

## Instrucciones para ejecutar la aplicación localmente y con una base de datos en blanco

1. **Clona el repositorio** en tu máquina local:
   ```
   git clone <URL_DEL_REPOSITORIO>
   ```

2. **Instala las dependencias necesarias** (por ejemplo, Flask, psycopg2, Kivy si usas la interfaz gráfica):
   ```
   pip install -r requirements.txt
   ```

3. **Configura la base de datos:**
   - Asegúrate de tener una instancia de PostgreSQL corriendo.
   - Crea una base de datos vacía para la aplicación.
   - Configura tus credenciales de conexión en el archivo `SecretConfig.py` según las instrucciones del README.

4. **Crea las tablas necesarias en la base de datos:**
   - Ejecuta la aplicación y accede a la ruta `/crear_tabla` o utiliza la funcionalidad correspondiente para crear las tablas desde la interfaz web.
   - Alternativamente, puedes ejecutar las pruebas unitarias para que las tablas se creen automáticamente.

5. **Ejecuta la aplicación:**
   - Para la interfaz de consola:
     ```
     py src\view\console\Pension_Console.py
     ```
   - Para la interfaz gráfica (GUI):
     ```
     py src/view/gui/pension_gui.py
     ```
   - Para la interfaz web (Flask):
     ```
     py src/view/view_web/app.py
     ```

6. **Accede a la aplicación** desde tu navegador en la dirección que indique Flask (por defecto, http://127.0.0.1:5000/).

7. **La aplicación estará lista para usarse con una base de datos en blanco.** Puedes comenzar a registrar usuarios y realizar cálculos de pensión desde cero.

---


