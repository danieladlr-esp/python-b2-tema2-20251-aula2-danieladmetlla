"""
Enunciado:
Realiza un análisis de un conjunto de datos de calificaciones de ramen utilizando la clase RamenDataAnalyzer.
Esta clase deberá ser capaz de leer datos desde diferentes formatos de archivo (CSV, JSON, Excel, SQLite) y calcular la
media de las calificaciones.

Implementa la clase 'RamenDataAnalyzer' con los siguientes métodos:
1. Un método para leer datos desde un archivo CSV, read_csv().
2. Un método para leer datos desde un archivo JSON, read_json().
3. Un método para leer datos desde un archivo Excel, read_excel().
4. Un método para leer datos desde una base de datos SQLite, read_sqlite().
5. Un método para calcular la media de las calificaciones de los datos leídos, analyze().
6. Un método auxiliar para convertir valores a numéricos, manejando valores no numéricos, to_numeric().

Parámetros:
    - file_paths: diccionario con las rutas de los archivos en diferentes formatos.

La clase "RamenDataAnalyzer" debe recibir un diccionario con las rutas de los archivos en diferentes formatos y utilizar
Pandas para leer y procesar los datos.

Ejemplo:
    file_paths = {
        'csv': 'data/ramen-ratings.csv',
        'json': 'data/ramen-ratings.json',
        'xlsx': 'data/ramen-ratings.xlsx',
        'sqlite': 'data/ramen-ratings.db'
    }
    analyzer = RamenDataAnalyzer(file_paths)
    print(analyzer.analyze())

Salida esperada:
    Un diccionario donde las llaves son los formatos de archivo ('csv', 'json', 'xlsx', 'sqlite')
    y los valores son las medias de las calificaciones de cada formato.
"""

import pandas as pd
import sqlite3


class RamenDataAnalyzer:
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def to_numeric(self, s):
        return pd.to_numeric(s, errors='coerce')

    def read_csv(self):
        dataframe = pd.read_csv(self.file_paths['csv'])
        dataframe['Stars'] = self.to_numeric(dataframe['Stars'])
        return dataframe

    def read_json(self):
        dataframe = pd.read_json(self.file_paths['json'], lines=True)
        dataframe['Stars'] = self.to_numeric(dataframe['Stars'])
        return dataframe

    def read_excel(self):
        dataframe = pd.read_excel(self.file_paths['xlsx'])
        dataframe['Stars'] = self.to_numeric(dataframe['Stars'])
        return dataframe

    def read_sqlite(self):
        conn = sqlite3.connect(self.file_paths['sqlite'])
        dataframe = pd.read_sql("SELECT * FROM ramen_ratings", conn)
        dataframe['Stars'] = self.to_numeric(dataframe['Stars'])
        conn.close()
        return dataframe

    def analyze(self):
        mean_ratings = {}
        mean_ratings['csv'] = self.read_csv()['Stars'].mean()
        mean_ratings['json'] = self.read_json()['Stars'].mean()
        mean_ratings['xlsx'] = self.read_excel()['Stars'].mean()
        mean_ratings['sqlite'] = self.read_sqlite()['Stars'].mean()
        return mean_ratings

# Para probar el código, descomenta las siguientes líneas
# file_paths = {
#     'csv': 'data/ramen-ratings.csv',
#     'json': 'data/ramen-ratings.json',
#     'xlsx': 'data/ramen-ratings.xlsx',
#     'sqlite': 'data/ramen-ratings.db'
# }
#
# analyzer = RamenDataAnalyzer(file_paths)
# print(analyzer.analyze())
