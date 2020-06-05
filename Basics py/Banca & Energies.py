# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:39:31 2018


@author: Andrés G
"""

# Banca vs Energy 

# -*- coding: utf-8 -*-

# Cargar la librería pandas para manejo de datos tabulares
import pandas as pd 

# Cargar la librería matplotlib para uso de gráficos
import matplotlib.pyplot as plt

# Definir los nombres de archivos a cargar
# Son tres datos de los índices BP500, DAX e Ibex 35 en formato csv
# Estos archivos tienen que estar en la misma carpeta que ejercicio1.py
# Estos archivos también se pueden abrir con excel


archivos = ['BBVA.csv', 'SAN.csv', 'GAS.csv','REP.csv']

# Definición del objeto dataframe, donde cargar los datos de los archivos CSV
empresas = pd.DataFrame()

# Recorrer la lista de archivos a cargar
for archivo in archivos:
#    Cargar un archivo en la variable df 
#    dropna elimina las filas con algún na
    df = pd.read_csv("empresas\\"+archivo).dropna()
    df["ticker"] = archivo.split(".")[0]
#    Añadir el dataframe cargado al dataframe global
    empresas = empresas.append(df)    
    
# Convertir la columna fecha de cadena a fecha
empresas["Fecha"] = pd.to_datetime(empresas["Fecha"])

# Eliminar estas columnas
#del empresas["Vol."]
#del empresas["% var."]

# Eliminar los puntos de separación de miles y cambiar las comas decimales
# a punto decimal anglosajón
for col in empresas.columns[1:5]:
    empresas[col] = empresas[col].str.replace(".", "").str.replace(",", ".").astype("float")

# Obtención de los valores de Santander separados del resto de índices
santd = empresas[(empresas["ticker"] == "SAN") & (empresas["Fecha"].dt.year == 2016)]

# Obtención de los datos de BBVA separados del resto de índices
bbva = empresas[(empresas["ticker"] == "BBVA") & (empresas["Fecha"].dt.year == 2016)]

# Obtención de los datos de BBVA separados del resto de índices
gas = empresas[(empresas["ticker"] == "GAS") & (empresas["Fecha"].dt.year == 2016)]

# Obtención de los datos de BBVA separados del resto de índices
rep = empresas[(empresas["ticker"] == "REP") & (empresas["Fecha"].dt.year == 2016)]

# Asegurar que los datos están ordenados por fecha
bbva = bbva.sort_values(by="Fecha")
santd = santd.sort_values(by="Fecha")
gas = gas.sort_values(by="Fecha")
rep = rep.sort_values(by="Fecha")

# Establecemos la columna Fecha como índice para que se pinten automáticamente
# en el eje de las x
bbva = bbva.set_index("Fecha")
santd= santd.set_index("Fecha")
gas = gas.set_index("Fecha")
rep=  rep.set_index("Fecha")


# Pintar los datos de cierre de IBEX 35 y BP500 en la misma gráfica
plt.plot(bbva["Último"])
plt.plot(santd["Último"])
plt.plot(gas["Último"])
plt.plot(rep["Último"])
plt.show()

# Crear un dataframe con una tabla pivotada de índices
# Escribir en la consola pivot.head() para ver la forma de este dataframe
pivot = empresas.pivot_table(index=["Fecha"], columns=["ticker"], 
                            values=["Último", "Apertura", "Máximo", "Mínimo" ]).dropna()

# Generar gráfico de los datos de cierre para los tres índices para el año 2016
# Es la misma gráfica que la anterior, pero sin extraer directamente los datos 
# de cada índice
pivot[pivot.index.year == 2016]["Último"][["BBVA", "SAN","GAS","REP"]].plot()


# Crear un dataframe las medias móviles de los índices
# El tamaño de la ventana es 50
rollingw = pivot.rolling(50).mean();rollingw
rollingw.plot()

# Para las primeras n filas, siendo n el tamaño de la ventana, 
# la función rolling nos devuelve NA's
# Con dropna se descartan estas filas
# Para ver esta tabla, escribir rollingw.head() en la consola.
rollingw = rollingw.dropna()

# Realizar una rolling window para la desviación típica eliminando los NA
std = pivot.rolling(50).std().dropna();std
std.plot()
# Creación de una tabla con varias funciones estadísticas. 
# En este caso: la media, la desviación típica, el mínimo y el máximo
agg = pivot.agg(["mean", "std", "min", "max"]);agg

# -*- coding: utf-8 -*-
"""
#Se puedenejecutar en la consola interactiva para explorar las variables creadas

"""
