from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raiz = Path(__file__).parent.parent #Variable con la que salimos del archivo leerdatos.py y de la carpeta src.

archivo = raiz / "datos" / "población_extranjera_españa.xlsx" #Variable que usa raiz y entramos en la carpeta datos y en el archivo población_extrangera_españa.xlsx .

df = pd.read_excel(archivo, header=None) #Variable con la que leemos el archivo excel. Comando para que descarte los encabezados del archivo excel.


matriz = np.array ([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int) 
#Leemos los datos de la fila 8 y 10, desde B hasta BX. Le indicamos que los datos son números enteros.

print (matriz) #Mostramos por pantalla todo el contenido de la matriz.

print("\nDimensiones: ", matriz.shape) #Mostramos por pantalla las dimensiones de la matriz.

anios = matriz[0]
poblacion = matriz[1]
#Extraemos de la matriz las dos filas como variables independientes.


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


