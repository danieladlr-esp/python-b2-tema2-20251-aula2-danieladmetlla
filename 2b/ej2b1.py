"""
Enunciado:
Desarrolla un conjunto de funciones para realizar operaciones de procesamiento de datos en un archivo CSV utilizando
Pandas y el paradigma de programación funcional. Este enfoque debe permitir el encadenamiento fluido de operaciones
utilizando la técnica de "pipes".

Las funciones a desarrollar son:
    1. Leer datos desde un archivo CSV: read_csv(file_path, **kwargs) que lee un archivo CSV y devuelve un DataFrame de
    Pandas. Debe permitir argumentos adicionales para configurar la lectura del CSV.
    2. Renombrar columnas del DataFrame: rename_columns(df, new_column_names) para cambiar los nombres de las columnas.
    3. Seleccionar columnas específicas del DataFrame: select_columns(df, column_names) para elegir ciertas columnas.
    4. Convertir columnas a valores numéricos: convert_to_numeric(df, column_name) que transforma una columna en valores
    numéricos.
    5. Filtrar datos basados en una condición específica: filter_by_condition(df, condition) para filtrar el DataFrame
    según una condición.
    6. Seleccionar datos con iloc: select_data(df, row_index=None) se utiliza para seleccionar filas específicas de un
    DataFrame. Si row_index es un número entero, devuelve un DataFrame con la fila correspondiente a ese índice. Si es
    un slice, devuelve las filas dentro del rango especificado. Si no se especifica row_index, devuelve el DataFrame
    completo.

Parámetros:
    file_path (str): Ruta del archivo CSV en 'read_csv'.
    new_column_names (dict): Diccionario para renombrar columnas en 'rename_columns'.
    column_names (list): Lista de nombres de columnas a seleccionar en 'select_columns'.
    column_name (str): Nombre de la columna a convertir a numérico en 'convert_to_numeric'.
    condition (str): Condición para filtrar datos en 'filter_by_condition'.
    row_index (int, slice): Índice de fila o rebanada de filas a seleccionar en 'select_data'.

Cada función debe aceptar un DataFrame como primer argumento y devolver un DataFrame modificado, facilitando su uso con
el método .pipe() de Pandas para encadenar operaciones.

Ejemplo:
    file_path = 'data/ramen-ratings.csv'

    df_preprocessed = (
        read_csv(file_path)
        .pipe(rename_columns, {'Review #': 'review_number', 'Brand': 'brand', 'Stars': 'rating'})
        .pipe(select_columns, ['review_number', 'brand', 'rating'])
        .pipe(convert_to_numeric, 'rating')
        .pipe(filter_by_condition, 'rating > 3')
    )

    print(select_data(df_preprocessed, slice(0, 5)))

Salida esperada:
    Un DataFrame de Pandas con las operaciones realizadas, incluyendo los datos filtrados según la condición
    especificada.
"""

import pandas as pd
import typing as t

def read_csv(file_path: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(file_path, **kwargs)

def rename_columns(df: pd.DataFrame, new_column_names: dict) -> pd.DataFrame:
    return df.rename(columns=new_column_names)

def select_columns(df: pd.DataFrame, column_names: list) -> pd.DataFrame:
    return df[column_names]

def convert_to_numeric(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df

def filter_by_condition(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    return df.query(condition)

def select_data(df: pd.DataFrame, row_index: t.Union[int, slice] = None) -> pd.DataFrame:
    if row_index is not None:
        if isinstance(row_index, int):
            return df.iloc[[row_index]]  # Útil para un índice entero
        else:
            return df.iloc[row_index]  # Útil para un slice
    else:
        return df


# Para probar el código, descomenta las siguientes líneas
# file_path = 'data/ramen-ratings.csv'
#
# df = (read_csv(file_path)
#       .pipe(rename_columns, {'Review #': 'review_number', 'Brand': 'brand', 'Stars': 'rating'})
#       .pipe(select_columns, ['review_number', 'brand', 'rating'])
#       .pipe(convert_to_numeric, 'rating')
#       .pipe(filter_by_condition, 'rating > 3'))
#
# print(select_data(df, slice(0, 5)))
