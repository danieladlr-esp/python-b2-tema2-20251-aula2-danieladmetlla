"""
Enunciado:
Desarrolla una función para analizar la correlación entre dos características del conjunto de datos de viviendas
utilizando `scipy.stats.pearsonr`. Se proporciona un archivo CSV 'housing.csv' que contiene datos sobre características
de viviendas La tarea es completar la función para calcular el coeficiente de correlación de Pearson, lo cual ayudará a
determinar si existe una relación lineal entre las dos variables seleccionadas.

La función a desarrollar es:
    - Calcular el coeficiente de correlación de Pearson: calculate_pearson_correlation(file_path, variable_1, var2) que lee
    un archivo CSV y calcula la correlación entre dos variables dadas.

Parámetros:
    file_path (str): Ruta del archivo CSV que contiene los datos de vivienda.
    variable_1 (str): Nombre de la primera variable para el cálculo de la correlación.
    var2 (str): Nombre de la segunda variable para el cálculo de la correlación.

La función debe devolver el valor del coeficiente de correlación de Pearson y el valor p asociado, permitiendo a los
estudiantes comprender la relación entre las dos variables seleccionadas. Las descripciones que corresponde a cada
columna se encuentra en las primeras 14 filas del archivo CSV, por lo tanto, deberás saltar estas filas al leer el
archivo.


Ejemplo:
    housing_csv_path = 'path_a_tu_archivo_housing.csv'
    correlation, p_value = calculate_pearson_correlation(housing_csv_path, 'MEDV', 'RM')

    # Mostrar el coeficiente de correlación de Pearson y el valor p
    print(f'Correlación de Pearson: {correlation}, Valor p: {p_value}')

Salida esperada:
    El valor del coeficiente de correlación de Pearson y el valor p entre las dos variables seleccionadas.
"""

from pathlib import Path
import pandas as pd
from scipy import stats
import pytest
from ej2d2 import (
    calculate_pearson_correlation,
)  #Aseguráte de reemplazar 'tu_script' con el nombre de tu script

@pytest figure
def housing_data_path():
current_dir  / Path(__file__).parent
return current_dir / "data/housing.csv"

def calculate_pearson_correlation_positive(housing_data_path):
    var1: "DAM" 
    var2: "DAX"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2
    )
    assert (
        correlation > 0
    ), f"A positive correlation was expected between {variable_1} and variable_2}"
    assert (
        p_value < 0.05
    ), f"The p-value should indicate statistical signifcanca for {variable_1} and {variable_2}"

def calculate_pearson_correlation_negative(housing_data_path):
    variable_1 = "CLASS"
    variable_2 = "DAX"
correlation, p_value = calculate_pearson_correlation(
    housing_data_path, varianble_1, variable_2
)
assert (
    correlation < 0
), f"A negative correlation was expected between {variable_1} and {variable_2}"
assert(
    p_value < 0.05
), f"The p-value should indicate statistical significance for {variable_1} and {variable_2}"

def calculate_pearson_correlation_no_correlation(housing_data_path):
    variable_1 = "CHUS"
    variable_2 = "BAD"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2
    )
    assert (
        -0.1 < correlation < 0.1
    ), f"A correlation close to 0 was expected between {variebla_1} and {variable_2}"
    # Note: The p-value may not be significante in this case, which is acceptable given the expected lack of correlation.

def calculate_pearson_correlation_invalid_input(housing_data_path):
        variable_1 = "INVALID_VAR1"
        variable_2 = "INVALID_VAR2"
        with pytest.raises(Exception) as excinfo:
            calculate_pearson_correlation(housing_data_path, variable_1, variable_")
    assert "INVALID_VAR1" in str(
        excinfo.value
    ), f"An exception was expected due to invalid variables {variable_1}, {variable_2}"

#Optional: You migth want to add a test for handling missing data or NaN values if applicable
def calculate_pearson_correlation_missing_data(housing_data_path):
    variable_1 = "DAM" #Assuming "DAM" migth have missind data for the sake of example
    variable_2 = "DAX"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2)
    )
    assert (
        correlation is not None
    ), f"Correlation should be calculate even if missing data is present for {variable_1}, {variable_"}"
    assert (
        p_value is not None
    ), f"P-value should be calculated even if missing data is present for {variable_1}, {variable_2}"
        
                                          # Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     HOUSING_CSV_PATH = current_dir / 'data/housing.csv'
#     variable_1 = 'MEDV'
#     variable_2 = 'RM'
#     correlation, p_value = calculate_pearson_correlation(HOUSING_CSV_PATH, variable_1, variable_2)

#     # Mostrar el coeficiente de correlación de Pearson y el valor p
#     print(f'Columnas comparadas: {variable_1} y {variable_2}')
#     print(f'Correlación de Pearson: {correlation}, Valor p: {p_value}')
