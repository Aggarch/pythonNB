# -*- coding: utf-8 -*-

"""

Para optimizar las campañas de captación, fidelización y promoción, el dpto. de
marketing ha identificado tres perfiles diferenciados localizados en tres áreas
geográficas distintas hacia los que puede dirigir campañas especializadas, ya
que reúnen características comunes.

La primera área se corresponde a las zonas de East Heber, West Braulioville,
North Elva y Friesenmouth, y el dpto. de marketing quiere dirigir una campaña
de captación de personas con ingresos.

La segunda área se corresponde con las zonas de South Arieltown, New Adolphus y
Port Hayleeside, y el dpto. de marketing pretende dirigir una campaña de 
fidelización de clientes que hayan tenido un gasto superior a 2000 unidades 
monetarias.

La tercera área se corresponde con las zonas de West Skye, North Reta y 
Mikeview, y el dpto. de marketing pretende dirigir una campaña de promoción
de productos enfocada a gente mayor de veinticinco años.

Resolver, al menos, una de las tres áreas descritas en el problema.

"""


import pandas as pd

columnas = ["nombre_completo", "telefono1", "telefono2", "ciudad", "email"]

estados_laborales = ["Cuenta Ajena", "Cuenta Propia", "No Empleado", 
                     "Jubilado", "Estudiante" ]

area1 = ['East Heber','West Braulioville', 'North Elva', 'Friesenmouth']
area2 = ['South Arieltown', 'New Adolphus', 'Port Hayleeside']
area3 = ['West Skye', 'North Reta', 'Mikeview']


# Obtener los datos del excel y del archivo csv
clientes = pd.read_excel("bdd.xlsx", sheetname="clientes")
productos= pd.read_excel("bdd.xlsx", sheetname="productos")
consumos = pd.read_excel("bdd.xlsx", sheetname="consumos")

encuestas = pd.read_csv("encuestas.csv")

# Convertir a fechas
clientes["fecha_nacimiento"] = pd.to_datetime(clientes["fecha_nacimiento"])
encuestas["fecha_nacimiento"] = pd.to_datetime(encuestas["fecha_nacimiento"])

# Homogeneizar los nombres
clientes["nombre_completo"] = clientes["nombre"] + " " + clientes["apellidos"]

# Crear bdd con clientes y consumos
#bdd = consumos.merge(clientes, how="left", left_on="cliente", right_on="id")
#del bdd["id"]

# Añadir a bdd los productos consumidos por los clientes
#bdd = bdd.merge(productos, how="left", left_on="producto", right_on="id")
#del bdd["id"]


# Renombrar columnas
#bdd = bdd.rename(columns={
#                              "cliente": "id_cliente", 
#                              "producto": "id_producto", 
#                              "fecha": "fecha_consumo",                              
#                              "nombre": "producto"
#                              })


# Calcular los importes


#  Generar columna con el nombre completo para compatilibidad con encuestas

################ Filtro para el área 1
################ USAR SOLO TABLA DE ENCUESTAS

# Filtrar por área
#grupo1 = 

# Filtrar por interés > 7


# filtrar por "Cuenta Ajena", "Cuenta Propia", "Jubilado"
#target_g1 = 


# Volcar a excel grupo1.xlsx
# grupo1.to_excel("grupo1.xlsx")



################ Filtro para el área 2
################ USAR SOLO TABLA BDD

# Filtrar por área
#grupo2 = 

# Obtener los importes por cliente
#grupo2["importes"] = 

# Filtrar importes > 2000


# Devolver el nombre a columna 
#importes = importes.reset_index()

# Obtener lista de clientes que hayan consumido más


# Dejar solo las columnas a volcar



# Volcar a excel grupo2.xlsx


################ Filtro para el área 3
################ USAR TANTO LA TABLA BDD COMO ENCUESTAS

# Filtrar por área
#grupo3 = 
#encuestas3 = 


# Quedarse solo con los mayores de 25


# En las encuestas, además, quedarse con quien tenga un interés mayor que 7


# Dejar solo las columnas a volcar


# Concatenar grupo3 y encuestas3


# Volcar a excel grupo3.xlsx





