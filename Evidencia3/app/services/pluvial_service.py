# app/services/pluvial_service.py
import pandas as pd
import random
import os
import matplotlib.pyplot as plt

def generar_datos_aleatorios():
    return [[random.randint(0, 100) for _ in range(31)] for _ in range(12)]

def cargar_datos_pluviales():
    ano = input("Ingrese el año de los datos pluviales: ")
    nombre_archivo = f'registroPluvial{ano}.csv'
    
    if os.path.exists(nombre_archivo):
        print(f"Cargando datos del archivo {nombre_archivo}...")
        df = pd.read_csv(nombre_archivo)
    else:
        print(f"El archivo {nombre_archivo} no existe. Generando datos aleatorios...")
        datos = generar_datos_aleatorios()
        df = pd.DataFrame(datos).T
        df.columns = [f'Mes {i+1}' for i in range(12)]
        df.to_csv(nombre_archivo)
    
    print(f"Datos del año {ano} cargados correctamente.")
    return df

def consultar_datos_pluviales():
    df = cargar_datos_pluviales()
    mes = int(input("Ingrese el mes a consultar (1-12): "))
    
    if 1 <= mes <= 12:
        print(df[f'Mes {mes}'])
    else:
        print("Mes no válido.")

def visualizar_datos_pluviales():
    df = cargar_datos_pluviales()
    
    print("\nElija el gráfico a visualizar:")
    print("1. Gráfico de Barras")
    print("2. Gráfico de Dispersión")
    print("3. Gráfico Circular")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        df.sum().plot(kind='bar', title='Cantidad total de lluvia por mes')
        plt.show()
    elif opcion == '2':
        # Corregimos esta parte
        dias = range(1, len(df.values.flatten()) + 1)
        plt.scatter(dias, df.values.flatten())
        plt.title('Distribución de lluvias a lo largo del año')
        plt.xlabel('Días')
        plt.ylabel('Cantidad de lluvia')
        plt.show()
    elif opcion == '3':
        df.sum().plot(kind='pie', autopct='%1.1f%%', title='Distribución de lluvias por mes')
        plt.show()
    else:
        print("Opción no válida.")
