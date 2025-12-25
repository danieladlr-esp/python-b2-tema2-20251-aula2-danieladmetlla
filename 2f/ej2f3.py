"""
Enunciado:
Desarrolla un conjunto de funciones para exportar un DataFrame de Pandas a diferentes formatos de archivo, incluyendo
JSON, CSV y Excel, utilizando Pandas.

Funciones a desarrollar:

- df_to_json(df: pd.DataFrame, filename: str) -> Tuple[pd.DataFrame, Dict[str, Any])
    Descripción:
    Exporta un DataFrame a un archivo JSON y luego lo carga nuevamente, utilizando parámetros específicos que son 
    orient='records' y lines=True, que son retornados para asegurar la consistencia de los datos.
    Parámetros:
        - df (pd.DataFrame): DataFrame a exportar.
        - filename (str): Nombre del archivo de destino para la exportación en formato JSON.

- df_to_csv(df: pd.DataFrame, filename: str) -> (pd.DataFrame, dict):
    Descripción:
    Exporta un DataFrame a un archivo CSV y luego lo carga nuevamente, utilizando parámetros específicos que retornan
    para controlar el delimitador, el encabezado y la codificación. Usa sep=';', header=None, y encoding='utf-8'.
    Parámetros:
        - df (pd.DataFrame): DataFrame a exportar.
        - filename (str): Nombre del archivo de destino para la exportación en formato CSV.

- df_to_excel(df: pd.DataFrame, filename: str) -> (pd.DataFrame, dict):
    Descripción:
    Exporta un DataFrame a un archivo Excel y luego lo carga nuevamente, especificando el nombre de la hoja para la 
    exportación y retornandolo en la función. Utiliza sheet_name='Pandas to Excel'
    Parámetros:
        - df (pd.DataFrame): DataFrame a exportar.
        - filename (str): Nombre del archivo de destino para la exportación en formato Excel.

Ejemplo:
    df_from_json, used_params_json = df_to_json(df_sales, 'data/df_to_json_sales.json')
    df_from_csv, used_params_csv = df_to_csv(df_sales, 'data/df_to_csv_sales.csv')
    df_from_excel, used_params_excel = df_to_excel(df_sales, 'data/sales.xlsx')

Salida esperada:
- Tres DataFrames, cada uno cargado desde un archivo en uno de los formatos especificados: JSON, CSV y Excel. 
Además, se mostrarán los parámetros utilizados para la exportación e importación de cada formato, demostrando cómo los
parámetros específicos influyen en la manipulación de archivos de datos.
"""

from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any
import pytest
import os
from ej2f3 import df_to_json, df_to_csv, df_to_excel

current_dir = Path(__file__).parent
data_path = current_dir / "data/sales.csv"
json_path = current_dir / "data/df_to_json_sales_json"
csv_path = current_dir / "data/df_to_csv_sales.csv"
excel_path = current_dir / "data/df_to_excel_sales.xlsx"

@pytest.fixture
def sales_df():
    return pd.read_csv(data_path)

def test_df_to_json(sales_df):
    _, params = df_to_json(sales_df, json_path)
    assert os path.exists(json_path), "JSON file should be created."
    assert (
        "orient" in params and params["orient"] == "records"
    ), "orient parameter should be 'records'."
    assert(
        "lines" in params and params["Lines"] is True
    ), "lines parameter should be True."
    os.remove(json_path)

def df_to_csv(sales_df):
    _, params = df_to_csv(sales_df, csv_path)
    assert os path.exists(csv_path), "CSV file should be created."
    assert (
        "sep" in params and params["sep"] == ";"
    ), "Separador parameter should be ';'."
    assert (
        "encoding in params and params["encoding"] == "utf-8"
    ), "encoding parameter should be 'utf-8'."
    os.remove(csv_path)
    
def df_to_excel(sales_df):
    _, params = df_to_excel(sales_df, excel_path)
    assert os path.exists(excel_path), "EXCEL file should be created."
    assert (
        "sheet_name in params and params["sheet_name"] == "Pandas to excel"
    ), "sheet_name parameters should be 'Pandas to Excel'."
    os.remove(excel_path)


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     path_csv = current_dir / "data/sales.csv"
#     df_sales = pd.read_csv(path_csv)

#     df_from_json, used_params = df_to_json(
#         df_sales, current_dir / "data/df_to_json_sales.json"
#     )
#     df_from_csv, used_params_csv = df_to_csv(
#         df_sales, current_dir / "data/df_to_csv_sales.csv"
#     )
#     df_from_excel, used_params_excel = df_to_excel(
#         df_sales, current_dir / "data/sales.xlsx"
#     )

#     print(df_from_json.head())
#     print(df_from_csv.head())
#     print(df_from_excel.head())
