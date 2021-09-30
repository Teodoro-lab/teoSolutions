import sqlite3
from faker import Faker

#########################################
############---BEGIN---##################
#########################################
"""
Cursor es un método de conexión
Para ejecutar sentencias SQL primero se establece
una conexión y luego se crea un objeto cursor
utilizando el objeto de conexión
"""

#con = sqlite3.connect('mydatabase.db')

#cursorObj = con.cursor()

# Ahora usamos el método execute para consulta sql

#########################################
############---CREATE DB---##############
#########################################

"""
Cuando haces la conexión se crea un archivo de 
base de datos, se guarda en el disco, también se puede
crear una base de datos en RAM
usando 

# :memory:

con la función de conexión

"""

from sqlite3 import Error

def sql_connection():

	try:
		con = sqlite3.connect('mydatabase.db') #':memory:'#

		print("Conection is established: Data base is created")

		return con

	except Error:

		print(Error)

	#finally:

	#	con.close() # Cerrar conexión es opcional pero es una buena 
					# practica de programación porque liberas la 
					# memoria de los recuros no utilizados

################################################################################################################################################
########################################################---CREATE TABLES---#####################################################################
################################################################################################################################################

"""
Para crear la tabla se emplea el metodo
execute() y se considera:

1- Se crea el objeto conexión
2-El objeto cursos se crea 
utilizando el objeto conexíón
3-Usando el objeto del cursor, 
se ejecuta el método execute con la
consulta CREATE TABLE como parametro
"""


def sql_table(con): # Crea el objeto cursor

	cursorObj = con.cursor()

	cursorObj.execute("""CREATE TABLE employes
							(id integer PRIMARY KEY, 
							name text, 
							salary real, 
							department text, 
							position text, 
							hireDate text
					)""")

	con.commit() # Guarda todos los cambios
 
#con = sql_connection()

#sql_table(con)


#con = sqlite3.connect('mydatabase.db')
#cursorObj = con.cursor()

def jonh():
	cursorObj.execute("""INSERT INTO employes VALUES(
							1, 
							'John', 
							700, 
							'HR', 
							'Manager', 
							'2017-01-04'
					)""")
	con.commit()

entities = (2, "Quilombo", 1500, "Development", "QA", "2019-04-03")

def insertENTITIES():
	cursorObj.execute("""INSERT INTO employes(
						id, 
						name, 
						salary, 
						department, 
						position, 
						hireDate) 
						VALUES(?, ?, ?, ?, ?, ?)""", entities)
	con.commit()

def sandunga("""

_|_|_|_|_|	_|_|_|_|	_|_|_|_|		_|_|_|_|_|		_|		_|		_|		_|
	_|		_|			_|	  _|	 	_|						_|_|	_|
	_|		_|_|_|		_|    _|		_|				_|		_|  _|	_|		_|
	_|		_|			_|	  _|		_|   _|_|_      _|		_|    _|_|		_|
	_|		_|			_|    _|		_|	    _|		_|		_|      _|		_|
	_|		_|_|_|_|	_|_|_|_|		_|_|_|_|_|		_|		_|		_|		_|

""")



import random
arrSalary = [1000, 2000, 1750, 1800, 5000, 1000, 2050]
arrDepartment = ["Sales", "HR", "Producion", "Marketing", "Development", "Systems", "Administration", "Executives"]
#arrPosition = ["Slave", "notSoSlave", "boss"]


fake = Faker()
for i in range(5, 10):
	entities = (i, fake.name(), arrSalary[random.randint(0, len(arrSalary) - 1)], arrDepartment[random.randint(0, len(arrDepartment) - 1)], fake.job(), fake.date())
	#insertENTITIES()

	#con.commit()



################################################################################################################################################
########################################################---UPDATE TABLES---#####################################################################
################################################################################################################################################


#conexion = sqlite3.connect('mydatabase.db')

def sql_update(con):
	cursorObj = conexion.cursor()

	cursorObj.execute("UPDATE employes SET name = 'Rogers' WHERE id = 3")

	conexion.commit()

#sql_update(conexion) #Se hace update a través del objeto que conecta con la base

################################################################################################################################################
########################################################---SELECT---#####################################################################
################################################################################################################################################


# SELECCIONAR TODOS LOS ELEMENTOS

# cursorObj.execute('SELECT * FROM employees')

# select column1, column2 from tables_name

# cursorObj.execute('SELECT id, name FROM employees')

## PARA OBTENER TODOS LOS DATOS DE UNA BASE DE DATOS EJECUTAMOS LA SENTENCIA SELECT
## Y LUEGO USAREMOS EL METODO fetchall() DEL OBJETO CURSOR PARA ALMACENAR LOS VALORES
## EN UNA CARIBALE

#conexion = sqlite3.connect('mydatabase.db')


def sql_fetch(con):
	cursor = conexion.cursor()

	cursor.execute('SELECT id, name FROM employes')

	rows = cursor.fetchall()

	for row in rows:
		print(row)

#sql_fetch(conexion)

"""
cursor = conexion.cursor()

cursor.execute('SELECT id, name FROM employes')

[print(row) for row in cursor.fetchall()]
"""

"""
cursor = conexion.cursor()

cursor.execute('SELECT id, name FROM employes WHERE salary > 1800')

[print(row) for row in cursor.fetchall()]

"""

################################################################################################################################################
########################################################---ROWCOUNT---#####################################################################
################################################################################################################################################


