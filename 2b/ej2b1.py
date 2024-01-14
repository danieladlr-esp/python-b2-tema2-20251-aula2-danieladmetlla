"""
Enunciado:
Desarrolla una clase llamada `CSVDataProcessor` para realizar varias operaciones de procesamiento de datos en un archivo
CSV.

La clase deberá ser capaz de realizar las siguientes tareas:
1. Leer datos desde un archivo CSV, `read_csv()`.
2. Renombrar columnas del DataFrame, `rename_columns(new_column_names)`.
3. Seleccionar columnas específicas del DataFrame, `select_columns(column_names)`.
4. Convertir columnas a valores numéricos, `convert_to_numeric(column_name)`.
5. Seleccionar datos usando iloc, `select_data(row_index=None)`.
6. Filtrar datos basados en una condición específica, `filter_by_condition(condition)`.

Parámetros:
    - file_path (str): Ruta del archivo CSV.
    - new_column_names (dict): Un diccionario para renombrar columnas.
    - column_names (list): Lista de nombres de columnas para seleccionar.
    - column_name (str): Nombre de la columna a convertir a numérico.
    - condition (str): Condición para filtrar datos en formato de cadena.

La clase `CSVDataProcessor` debe utilizar Pandas para leer y procesar los datos del CSV.

Ejemplo:
    file_path = 'data/ramen-ratings.csv'
    processor = CSVDataProcessor(file_path)
    processor.read_csv()
    processor.rename_columns({'Review #': 'review_number', 'Brand': 'brand', 'Stars': 'rating'})
    processor.select_columns(['review_number', 'brand', 'rating'])
    processor.convert_to_numeric('rating')
    processor.filter_by_condition('rating > 3')
    print(processor.select_data())

Salida esperada:
    Un DataFrame de Pandas con las operaciones realizadas, incluyendo los datos filtrados según la condición
    especificada.
"""

import pandas as pd

class CSVDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dataframe = None

    def read_csv(self):
        self.dataframe = pd.read_csv(self.file_path)

    def rename_columns(self, new_column_names):
        self.dataframe.rename(columns=new_column_names, inplace=True)

    def select_columns(self, column_names):
        self.dataframe = self.dataframe[column_names]

    def convert_to_numeric(self, column_name):
        self.dataframe[column_name] = pd.to_numeric(self.dataframe[column_name], errors='coerce')

    def filter_by_condition(self, condition):
        self.dataframe = self.dataframe.query(condition)

    def select_data(self, row_index=None) -> pd.DataFrame:
        if row_index is not None:
            return self.dataframe.iloc[row_index]
        else:
            return self.dataframe


# Para probar el código, descomenta las siguientes líneas
# file_path = 'data/ramen-ratings.csv'
# processor = CSVDataProcessor(file_path)
# processor.read_csv()
# processor.rename_columns({'Review #': 'review_number', 'Brand': 'brand', 'Stars': 'rating'})
# processor.select_columns(['review_number', 'brand', 'rating'])
# processor.convert_to_numeric('rating')
# processor.filter_by_condition('rating > 3')
# print(processor.select_data(slice(0, 5)))
