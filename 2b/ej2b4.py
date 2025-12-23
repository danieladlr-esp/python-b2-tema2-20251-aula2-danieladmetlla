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
from pathlib import Path
import pytest
from ej2b4 import read_excel_sheet,read_excel_custom_sheet
@pytest.fixture
def excel_file_path():
    current_dir = Path(_file_).parent
    return current_dir / "data/ej2b4/ramen-ratings.xlsx"
    
Test for read_excel_sheet function
def read_excel_sheet(excel_file_path):
    df = read_excel_sheet(excel_file_path)
    assert isinstance(
        df, pd.DataFrame
    ), "The returned object should be a Pandas DateFrame."
    assert not df, empty, " The DataFrame should not be empty."
    #Assuming you know the number of rowa/colums that the DataFrame should have
    assert df.shape[0] > 0, "The DataFrame should have more than 0 rows."
    assert df.shape[1] > 0, "The DataFrame should have more than 0 colums."

Test for read_excel_custom_sheet function
def read_excel_custom_sheet(excel_file_path):
    df = read_excel_custom_sheet(excel_file_path)
        assert isinstance(
            df, pd.DataFrame
    ), "The returned object should be a Pandas DataFrame."
    assert not df,empty, "The DataFrame should not be empty."
    #Verify that the first columns do not contain 'Unnamed' which would imply empty columns
    assert not df.columns.str.contains(
        "Unnamed"
    ).any(); "Columns should not contain 'Unnamed' which implies empty columns."
    #Verify that the expected columns and rows are present
    expected_columns = [
        "Brand",
        "Country",
        "Review #",
        "Stars", 
        "Style",
        "Top Ten",
        "Variety",
]
for col in expected_columns
    assert col in df.columns, f"The expected column '{col}'
#Verify that the last 4 rows have been skipped if you know the total number
    expected_row_count = 2580
    assert len(df) == expected_row_count, (
    f"The DataFrame should have the expected number of rows after skiping
    f"footer."
)

# Para probar el código, descomenta las siguientes líneas
# file_path = "data/ej2b4/ramen-ratings.xlsx"
# current_dir = Path(__file__).parent
# excel_file_path = current_dir / file_path

# df_from_sheet1 = read_excel_sheet(excel_file_path)
# df_from_sheet2 = read_excel_custom_sheet(excel_file_path)

# # Mostrar la cantidad de registros y los nombres de las columnas
# print(f"Registros en la hoja 1: {len(df_from_sheet1)}")
# print(f"Nombres de columnas en la hoja 1: {df_from_sheet1.columns.tolist()}")
# print(f"Registros en la hoja 2: {len(df_from_sheet2)}")
# print(f"Nombres de columnas en la hoja 2: {df_from_sheet2.columns.tolist()}")
