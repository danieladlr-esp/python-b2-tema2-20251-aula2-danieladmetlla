"""
Enunciado:
Desarrolla un conjunto de funciones para la manipulación de datos utilizando Pandas. El objetivo es 
trabajar con un DataFrame de un archivo CSV que contiene información sobre calificaciones y realizar la selección 
de columnas por nombre e índice y filas que cumplan múltiples condiciones.

Las funciones y escenarios a desarrollar son:

1. Seleccionar columnas por nombre o índice y opcionalmente filas por rango:
    - `select_rows_and_columns(df: pd.DataFrame, columns: Union[List[str], List[int]], rows: Optional[slice] = None) -> pd.DataFrame`
      Esta función permite seleccionar columnas específicas por nombre o índice y opcionalmente filas por un rango especificado.
      Si no se especifica un rango de filas, se seleccionarán todas las filas por defecto.

2. Seleccionar filas que cumplan con una o múltiples condiciones:
    - `select_rows_with_conditions(df: pd.DataFrame, conditions: Union[str, List[str]]) -> pd.DataFrame`
      Permite seleccionar filas que cumplan con una o múltiples condiciones dadas en formato de cadena.

Parámetros:
    - df (pd.DataFrame): DataFrame original.
    - columns (Union[List[str], List[int]]): Nombres o índices de las columnas a seleccionar.
    - rows (Optional[slice]): Rango de filas a seleccionar, especificado como un objeto slice. Por defecto, selecciona todas las filas.
    - conditions (Union[str, List[str]]): Una o múltiples condiciones en formato de cadena.

Ejemplo:
    selected_columns_and_rows = select_rows_and_columns(df_grades, ['Name', 'Maths', 'History'], rows=slice(5, 10))
    selected_rows = select_rows_with_conditions(df_grades, ['English > 50', 'Maths >= 60', 'Geography > 55'])

Salida Esperada:
- DataFrame resultante después de seleccionar las columnas específicas por nombre e índice y opcionalmente filas por rango.
- DataFrame resultante después de seleccionar las filas que cumplen con las condiciones.
"""

from pathlib import Path
from typing import List, Union, Optional
import pandas as pd
import pytest
import select_rows_and_columns, select_rows_with_conditions
    
@pytest.fixture(scope="module")

def df_grades():
    current_dir = Path(_file_).parent
    FILE_PATH = current_dir / "data/grades.csv"
    return pd.read_csv(FILE_PATH)

def test_select_rows_and_columns_by_name(df_grades):
    result = select_rows_and_columns(df_grades, ["Name", "Maths", "History"])
    expected_columns = ["Name", "Maths", "History"]
    assert (
        List(result.columns) == expected_columns
    ), "Column names do not match the expected columns"
    
def test_select_rows_and_columns_by_index(df_grades):
    result = select_rows_and_columns(df_grades, [0, 1, 3])
    expected_columns = df_grades.columns[[0, 1, 3]].tolist()
    assert (
    list(result.columns) == expected_columns
    ), "Column index do not match the expected columns"

def select_rows_with_conditions_single(df_grades):
    result = select_rows_with_conditions(df_grades, "English > 50")
    assert not result.empty, "The DataFrame should not be empty"
    assert all(result["English"] > 50), "Not all rows meet the condition" 
    
def select_rows_with_conditions_multiple(df_grades):
    conditions = ["English > 50", "Maths >= 60", "Geography > 50")
    result = select_rows_with_conditions(df_grades, conditions)
    assert not result.empty, "The DataFrame should not be empty"
    assert (
        all(result["English"] > 50)
        and all(result["Maths"] >= 60)
        and all(result["Geography"] > 55)
    ), "Not all rows meet the conditions"

# Para probar el código, descomenta las siguientes líneas y asegúrate de tener un archivo CSV 'data/grades.csv'
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/grades.csv"
#     df_grades = pd.read_csv(FILE_PATH)
#     selected_columns_and_rows = select_rows_and_columns(
#         df_grades, ["Name", "Maths", "History"], rows=slice(5, 10)
#     )
#     selected_rows = select_rows_with_conditions(
#         df_grades, ["English > 50", "Maths >= 60", "Geography > 55"]
#     )
#     print("DataFrame Original:\n", df_grades.head())
#     print(
#         "DataFrame with Selected Columns and Rows:\n", selected_columns_and_rows.head()
#     )
#     print("DataFrame with Rows that Meet Conditions:\n", selected_rows.head())
