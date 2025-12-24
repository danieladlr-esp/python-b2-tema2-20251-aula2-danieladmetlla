"""
Enunciado:
Desarrolla un conjunto de funciones para realizar análisis estadístico sobre un conjunto de datos de calificaciones de
estudiantes utilizando Pandas. El objetivo es proporcionar una visión comprensiva del rendimiento de los estudiantes a
través del análisis de sus calificaciones almacenadas en un archivo CSV. Para ello, se compararán dos enfoques de
análisis descriptivo: uno mediante una función personalizada y otro utilizando la función describe de Pandas.

Las funciones a desarrollar son:
- Leer un archivo CSV y convertirlo en un DataFrame:
    read_csv_basic(file_path: str) -> pd.DataFrame
- Realizar una descripción estadística personalizada del DataFrame:
    custom_dataframe_describe(df: pd.DataFrame) -> pd.DataFrame
    Esta función debe calcular la media, mediana, desviación estándar, mínimo, máximo, y los cuartiles del DataFrame
    proporcionado.
- Utilizar la función describe de Pandas para obtener estadísticas descriptivas del DataFrame:
    pandas_dataframe_describe(df: pd.DataFrame) -> pd.DataFrame

Parámetros:
- file_path (str): Ruta del archivo CSV que contiene los datos de calificaciones.
- df (pd.DataFrame): DataFrame de pandas que contiene los datos.

Ejemplo:
    archivo_csv_path = 'data/grades.csv'
    dataframe = read_csv_basic(archivo_csv_path)

    print("Custom DataFrame:")
    print(custom_dataframe_describe(dataframe))

    print("\nDataFrame with Pandas:")
    print(pandas_dataframe_describe(dataframe))

Salida esperada:
- DataFrame que muestra la descripción estadística realizada manualmente de las calificaciones, incluyendo la media,
mediana, desviación estándar, mínimo, máximo, y los cuartiles para cada columna del conjunto de datos.
- DataFrame generado por la función describe de Pandas, que proporciona un resumen estadístico similar al anterior,
facilitando la comparación entre ambos enfoques.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import pytest
from ej2c2 import read_csv_basic, custom_dataframe_describe, pandas_dataframe_descrube

@pytest.fixture(scope="module")
def load_dataframe():
    current_dir = Path(_file_).parent
    FILE PATH = current_dir / "data/grades.csv"
    return read_csv_basic(FILE_PATH)

def read_csv_basic(load_dataFrame):
    assert not load_dataframe.empty, "The DataFrame should not be empty."
    expected_columns = ["Maths", "English", "Science"]
    assert all(
        column in load_dataframe.columns for column in expected_columns
    ), "DataFrame should have expected columns."

def custom_dataframe_describe(load_dataframe):
    result = custom_dataframe_describe(load_dataframe)
    expected_stats = [
        "count", 
        "mean",
        "median",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max",
    ]
    assert all(
        stat in result.index for stat in expected_stats
    ), "Custom describe should include all expected statistics."
    expected_mean_math = 48.216354
    assert np.isclose(
        result.loc["mean", "Maths"], expected_mean_math
    ), f"Expected mean for Maths should be {expected_mean_math}, got {result.loc['mean',
    expected_means = pd.Series(
        {
            "Hindi": 52.124361
            "English": 49.862010
            "Science": 48.686542
            "Maths": 48.216354
            "History": 49.240204
            "Geography": 49.603066
        }
    )
    assert_series_equal(
    result.loc["mean"],
    expected_means, 
    check_names=False,
    check_exact=False,
    rtol=le-5
    ),
def pandas_dataframe_describe(load_dataframe) 
   result = pandas_dataframe_describe(load_dataframe)
   expected_stats = ["count", "mean", "std", "min","25%", "50%", "75%", "max"]
   assert all(
       stat in result.index for stat in expected_stats
   ), "Pandas describe should include all default statistics."


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/grades.csv"
#     dataframe = read_csv_basic(FILE_PATH)

#     print("Custom Describe of the DataFrame:")
#     print(custom_dataframe_describe(dataframe), end="\n\n")

#     print("Pandas Describe of the DataFrame:")
#     print(pandas_dataframe_describe(dataframe))
