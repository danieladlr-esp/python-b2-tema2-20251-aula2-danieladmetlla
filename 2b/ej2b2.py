"""
Enunciado:
Realiza un análisis de un conjunto de datos de calificaciones de ramen utilizando un conjunto de funciones. Estas
funciones deberán ser capaces de leer datos desde diferentes formatos de archivo (CSV, JSON, Excel, SQLite) y calcular
la media de las calificaciones.

Implementa las siguientes funciones:
    read_csv(file_path): Función para leer datos desde un archivo CSV.
    read_json(file_path): Función para leer datos desde un archivo JSON.
    read_excel(file_path): Función para leer datos desde un archivo Excel.
    read_sqlite(file_path): Función para leer datos desde una base de datos SQLite.
    analyze(file_paths): Función para calcular la media de las calificaciones de los datos leídos de todos los formatos.
    to_numeric(string_number): Función auxiliar para convertir valores a numéricos, manejando valores no numéricos.

Parámetros:
    file_paths: diccionario con las rutas de los archivos en diferentes formatos.

Las funciones deben utilizar Pandas para leer y procesar los datos de los diferentes formatos de archivo y calcular la
media de las calificaciones.

Ejemplo:
    file_paths = {
        'csv': 'data/ramen-ratings.csv',
        'json': 'data/ramen-ratings.json',
        'xlsx': 'data/ramen-ratings.xlsx',
        'sqlite': 'data/ramen-ratings.db'
    }

    print(analyze(file_paths))


Salida esperada:
    Un diccionario donde las llaves son los formatos de archivo ('csv', 'json', 'xlsx', 'sqlite')
    y los valores son las medias de las calificaciones de cada formato.
"""

import pandas as pd
import sqlite3
import typing as t

def to_numeric(string_number: str) -> t.Union[float, int, None]:
    return pd.to_numeric(string_number, errors='coerce')

def read_csv(file_path: str) -> pd.DataFrame:
    dataframe = pd.read_csv(file_path)
    dataframe['Stars'] = to_numeric(dataframe['Stars'])
    return dataframe

def read_json(file_path: str) -> pd.DataFrame:
    dataframe = pd.read_json(file_path, lines=True)
    dataframe['Stars'] = to_numeric(dataframe['Stars'])
    return dataframe

def read_excel(file_path: str) -> pd.DataFrame:
    dataframe = pd.read_excel(file_path)
    dataframe['Stars'] = to_numeric(dataframe['Stars'])
    return dataframe

def read_sqlite(file_path: str) -> pd.DataFrame:
    conn = sqlite3.connect(file_path)
    dataframe = pd.read_sql("SELECT * FROM ramen_ratings", conn)
    dataframe['Stars'] = to_numeric(dataframe['Stars'])
    conn.close()
    return dataframe

def analyze(file_paths: dict) -> dict:
    mean_ratings = {
        'csv': read_csv(file_paths['csv'])['Stars'].mean(),
        'json': read_json(file_paths['json'])['Stars'].mean(),
        'xlsx': read_excel(file_paths['xlsx'])['Stars'].mean(),
        'sqlite': read_sqlite(file_paths['sqlite'])['Stars'].mean()
    }
    return mean_ratings

# Para probar el código, descomenta las siguientes líneas
file_paths = {
    'csv': 'data/ramen-ratings.csv',
    'json': 'data/ramen-ratings.json',
    'xlsx': 'data/ramen-ratings.xlsx',
    'sqlite': 'data/ramen-ratings.db'
}

print(analyze(file_paths))
