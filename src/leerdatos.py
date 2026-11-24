from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Importamos sqlite3 para poder crear y guardar datos en una base de datos SQLite.
import sqlite3

raiz = Path(__file__).parent.parent #Variable con la que salimos del archivo leerdatos.py y de la carpeta src.

archivo = raiz / "datos" / "población_extranjera_españa.xlsx" #Variable que usa raiz y entramos en la carpeta datos y en el archivo población_extrangera_españa.xlsx .

df = pd.read_excel(archivo, header=None) #Variable con la que leemos el archivo excel. Comando para que descarte los encabezados del archivo excel.


matriz = np.array ([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int) 
#Leemos los datos de la fila 8 y 10, desde B hasta BX. Le indicamos que los datos son números enteros.

np.set_printoptions(suppress=True, precision=0)

print ("MATRIZ DE DATOS:")

print (matriz) #Mostramos por pantalla todo el contenido de la matriz.

print("\nDimensiones: ", matriz.shape) #Mostramos por pantalla las dimensiones de la matriz.

anios = matriz[0]
poblacion = matriz[1]
#Extraemos de la matriz las dos filas como variables independientes.

# Creamos una tabla (DataFrame) sencilla uniendo los años y la población en dos columnas.
df_exportar = pd.DataFrame({
    "Año": anios,
    "Población": poblacion
})

# Definimos la ruta donde se guardará el archivo CSV y exportamos la tabla sin el índice de fila.
archivo_csv = raiz / "datos" / "poblacion_extranjera.csv"
df_exportar.to_csv(archivo_csv, index=False)

# Definimos la ruta de la base de datos SQLite y abrimos la conexión (si no existe, se crea sola).
archivo_db = raiz / "datos" / "poblacion_extranjera.db"
conexion = sqlite3.connect(archivo_db)

# Guardamos la tabla dentro de la base de datos con el nombre 'evolucion_poblacion' (reemplazandola si ya existe).
df_exportar.to_sql("evolucion_poblacion", conexion, if_exists="replace", index=False)

# Cerramos la conexión con la base de datos para guardar los cambios correctamente.
conexion.close()




print("\n========== Representación gráfica - Gráfico de barras ==========")

plt.figure(figsize=(10, 5))
plt.plot(anios, poblacion, marker="o", linestyle="-")
plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Número de personas")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#Imprimimos en el terminal una línea indicativa de que realizamos la representación gráfica
#Generamos el gráfico de barras utilizando matplotlib.pyplot


