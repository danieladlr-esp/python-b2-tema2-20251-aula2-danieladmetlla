"""
Enunciado:
Desarrolla un conjunto de funciones para leer y procesar datos de archivos Excel utilizando Pandas, abordando
distintos escenarios comunes en el análisis de datos. Se proporciona un archivo Excel y se deberán completar las
funciones para leer y formatear los datos.

Las funciones y escenarios a desarrollar son:
    - Leer datos desde una hoja específica: read_excel_sheet(file_path) que lee todos los registros de la hoja Sheet1
    en el archivo Excel y devuelve un DataFrame de Pandas.
    - Leer y limpiar datos de la hoja Sheet2 con encabezados desplazados, filas y columnas adicionales:
    read_excel_custom_sheet(file_path) que lee la hoja, ajusta los encabezados de las columnas y omite las
    filas y columnas sin valor, adicional, evitar las filas al final de la hoja.

Parámetros:
    - file_path (str): Ruta al archivo Excel.

Cada función debe devolver un DataFrame de Pandas, permitiendo a los estudiantes ver el efecto de diferentes modos de
lectura de datos desde un archivo Excel.

Ejemplo:
    df_from_sheet1 = read_excel_sheet(excel_file_path)
    df_from_sheet2 = read_excel_custom_sheet(excel_file_path)

Salida esperada:
    Un DataFrame de Pandas para cada función.
"""

import pandas as pd

# Función para leer la primera hoja de un archivo Excel
def read_excel_sheet(file_path: str) -> pd.DataFrame:
    dataframe = pd.read_excel(file_path, sheet_name='Sheet1')
    return dataframe

# Función para leer y limpiar la segunda hoja de un archivo Excel
def read_excel_custom_sheet(file_path: str) -> pd.DataFrame:
    # Función para detectar columnas no vacías
    def is_not_empty_column(col):
        return col.dropna().any()

    dataframe = pd.read_excel(file_path, sheet_name='Sheet2', header=3, skipfooter=4)
    cols_to_use = [col for col in dataframe.columns if is_not_empty_column(dataframe[col])]
    dataframe = dataframe[cols_to_use]

    return dataframe

# Para probar el código, descomenta las siguientes líneas
excel_file_path = 'data/ej2b4/ramen-ratings.xlsx'

df_from_sheet1 = read_excel_sheet(excel_file_path)
df_from_sheet2 = read_excel_custom_sheet(excel_file_path)

# Mostrar la cantidad de registros y los nombres de las columnas
print(f"Registros en la hoja 1: {len(df_from_sheet1)}")
print(f"Nombres de columnas en la hoja 1: {df_from_sheet1.columns.tolist()}")
print(f"Registros en la hoja 2: {len(df_from_sheet2)}")
print(f"Nombres de columnas en la hoja 2: {df_from_sheet2.columns.tolist()}")
