import pandas as pd 

# -----------Create the frame and the values-------------

df = pd.DataFrame(data = {
						"Pais":['Mexico', 'Argentina', 'Espana', 'Colombia'],
						"Poblacion":[127212000, 45167000, 47099000, 48922000]}
				)



#print(df, "\n")

# -----------Ordenamos por columna----------------

#print(df.sort_values(["Poblacion"], ascending=False), "\n")


#print(df, "\n")

#df = df.sort_values(["Pais"], ascending=False)

#df.sort_values("Pais")

df["Superficie"] = [1964375, 2780400, 505944, 1142748]

df["Deporte"] = "Futbol"

#print(df, "\n")

# -------------Eliminar una columna----------------

df = df.drop(["Deporte"], axis=1)

print(df)


# -------------Eliminar multiples columnas---------------

#print(df.drop(["Poblacion", "Pais"], axis=1))
#print(df)
# print(df.drop([""]), axis=1) not valid

# ------agregar fila al final_------

cantidad_filas = len(df)
###########print(cantidad_filas)

df.loc[cantidad_filas] = ["Benezuela", 0, 916445]
#df.loc[0] = ["Benezuela", 0, 916445]
#print(df,"\n")

# ---------------ACTUALIZAR FILA---------

df.loc[4] = ["Venezuela", 0, 916445]

#print(df, "\n")

["Benezuela", 0, 916445]


# ---------------ACTUALIZAR CELDA---------

df.at[4, "Poblacion"] = 32423000
#print(df, "\n")

# ----------------ELIMINAR FILA-------------

#print(df.drop([3, 1, 0]), "\n")
#print(df, "\n")

########################################################################
##################---FILTRAR----####################################
#########################################################################


mas_de_46 = df[ df ['Poblacion'] > 46_000_000 ] 
#print(mas_de_46, "\n")

#print(df[ df["Pais"] != "Mexico"], "\n")

#print(df [df["Pais"] == "Mexico"], "\n")

doble_filtro = df[ (df["Poblacion"] > 46_000_000) & (df["Superficie"] < 600_000) ]
#print(doble_filtro, "\n")


nombres_mayor_6 = df[ df["Pais"].str.len() > 6]
#print(nombres_mayor_6, "\n")
#

"""Este es el proceso realizado en todos los casos, por
esta razón se requiere la sintaxis anidada"""
print("###################################\n")
arr = [False , True , False, True, True]
print (df[arr])






########################################################################
##################---OPERACIONES ENTRE COLUMNAS----####################################
#########################################################################


print(df[ df["Pais"] == "Colombia"] )

df.at[0, "Superficie"] = 1142748
df.at[3, "Superficie"] = 2780400
df.at[1, "Superficie"] = 1964375


df["habit_x_km2"] = (df["Poblacion"] / df["Superficie"]).astype(int)
print(df.sort_values("habit_x_km2", ascending=False), "\n")

# -----------OPERACION DEFINIDA--------------

def crear_codigo(name):
	name = name.upper()
	name = name[:4]
	return name

df["Codigo"] = df["Pais"].apply(crear_codigo)

print(df, "\n")


"-.-.-.-.--.-.-.-.-..-."
"to be continued... =>"
"-.-.-.-.--.-.-.-.-..-."


########################################################################
##################---JOIN TABLES----####################################
#########################################################################

def categoria(fila):
	pob = fila["Poblacion"]
	hab = fila["habit_x_km2"]

	if pob > 46000000:
		if hab < 50:
			return "A"
		else:
			return "B"
	return "C"

df["Categoria"] = df.apply(categoria, axis=1)
print(df, "\n")

def color(Codigo, Categoria):
	if Categoria == "A":
		return "Rojo"
	if Codigo == "ESPA":
		return "Verde"
	return "Azul"

df["Color"] = df.apply(lambda fila: color(fila["Codigo"], fila["Categoria"]), axis=1)
print(df, "\n")

##-----------------MAPEO-------------------------

df['mapeo_color'] = df['Color'].map({'Azul':0, 'Rojo':1, 'Verde':2}).astype(int)

#print(df)

# -----------------REORDENAR COLUMNAS----------

df = df[ ["Codigo", "Pais", "Poblacion", "Categoria", "Superficie", "habit_x_km2" ] ]

print(df)


#-------------------JOIN ENTRE TABLAS----------------


df_comida = pd.DataFrame(data = {
						"Comida" : ['Burritos', 'Milanesa', 'Tortilla', 'Sancocho', 'Arepa']},
						index = ['MEXI', 'ARGE', 'ESPA', 'COLO', 'VENE']
	)
print(df_comida," \n")

df_index = df.set_index('Codigo')
print(df_index, "\n")


result1 = pd.concat([df_index, df_comida], axis=1, sort=True)
print(result1,"\n")



# ------LEFT JOIN POR COLUMNA CLAVE "MERGE"------------------

df_factor = pd.DataFrame(data={'Categoria':["A","B","C"],
								'Factor':[12.5,103,0.001]
								})
print(df_factor,"\n")

result2 = pd.merge(df, df_factor, how="left", on=["Categoria"])
print(result2, "\n")

# -------ADICIONAR MULTIPLES FILAS DESDE OTRA TABLA "APPEND"------------

df_otros = pd.DataFrame(data = {
	'Pais':['Brasil', 'Chile'],
	'Poblacion':[210688000, 19241000],
	'Superficie':[8515770,56102]
	})

print(df_otros, "\n")

df = df.append(df_otros, ignore_index=True, sort=True)

print(df,"\n")

#---------AGRUPAR----------------

grupo2 = df.groupby(['Categoria']).size() # ¿Cuántos datos perteneces a dicha categoría?
print(grupo2, "\n")

grupo1 = df.groupby(['Categoria']).sum() # Suma todos los datos de los países con dicha clasificacion(todos los A, todos los...)
print(grupo1, "\n")

#---------AGRUPAR POR DOS VARIABLES Y SUMARIZAMOS----------------

print(result2, "\n")
tabla = result2[['Categoria', 'Factor']].groupby(['Categoria'], as_index=False).agg(['mean', 'count', 'sum'])
print(result2[['Categoria', 'Factor']])
print(tabla, "\n")

#---------PIVOTAR TABLAS----------------

tabla_t = pd.pivot_table(result2, index="Categoria", columns="Pais", values="Factor").fillna(0)
print(tabla_t," \n")

#---------TRANSPONER TABLAS----------------

df = df.T
print(df, "\n")
df = df.T
print(df)


########################################################################
##################---VISUALIZACIÓN----####################################
########################################################################
	
import matplotlib.pyplot as plt

#df[['Poblacion', 'Superficie']].plot.hist(bins=5, alpha=0.5)
#plt.show()

#df.set_index('Pais')['Poblacion'].plot(kind='bar')
#plt.show()

#df_old = df.drop([5,6])
#df_old.sort_values(by="Pais").set_index("Pais")["habit_x_km2"].plot(kind="area")
#plt.show()

"""df.set_index("Pais").plot.barh(stacked=True)
plt.show()

df.set_index('Pais')['Superficie'].plot.pie()
plt.show()"""

df.sort_values(by="Superficie").plot.scatter(x="habit_x_km2", y="Superficie")
plt.show()