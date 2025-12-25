"""
Enunciado:
Desarrolla un conjunto de funciones para analizar datos estadísticos de un conjunto de calificaciones utilizando
`scipy.stats`. Se proporciona un archivo CSV con calificaciones de estudiantes y se deberán completar las funciones
para calcular diferentes momentos estadísticos de las calificaciones.

Las funciones y estadísticas a desarrollar son:
    - Calcular el primer momento (media): calculate_mean(file_path) que lee un archivo CSV y calcula la media de las
    calificaciones.
    - Calcular el segundo momento (varianza): calculate_variance(file_path) que calcula la varianza de las
    calificaciones para entender su dispersión.
    - Calcular el tercer momento (asimetría): calculate_skewness(file_path) para evaluar la asimetría de la
    distribución de las calificaciones.
    - Calcular el cuarto momento (curtosis): calculate_kurtosis(file_path) para medir la forma de la distribución de
    las calificaciones, en particular su picudez.

Parámetros:
    file_path (str): Ruta del archivo CSV que contiene las calificaciones.

Cada función debe devolver el valor del momento estadístico calculado, permitiendo a los estudiantes comprender la
distribución de las calificaciones.

Ejemplo:
    mean = calculate_mean(calificaciones_csv_path)
    variance = calculate_variance(calificaciones_csv_path)
    skewness = calculate_skewness(calificaciones_csv_path)
    kurtosis = calculate_kurtosis(calificaciones_csv_path)

Salida esperada:
    Los valores de la media, varianza, asimetría y curtosis de las calificaciones.
"""

from pathlib import Path
import pandas as pd
from scipy import stats
import pytest 
from ej2d1 import (
    calculate_mean,
    calculate_variance,
    calculate_skewness,
    calculate_kurtosis,
)

@pytest.fixture
def loaded_data():
    current_dir = Path(__file__).parent
    return current_dir / "data/calificaciones.csv"
    
def calculate_mean(loaded_data):
    assert calculate_mean(loaded_data) == pytest.approx(
        80.3, 0.1
    ), "Mean calculation failed"

def calculate_variance(loaded_data):
    assert calculate_variance(loaded_data) == pytest.approx(
        92.3, 0.1
), "Variance calculation failed"
    
def calculate_skewness(loaded_data):
    assert calculate_skewness(loaded_data) == pytest.approx(
        -0.12, 0.1 
), "Skewness calculation failed"

def calculate_kurtosis(loaded_data):
    assert calculate_kurtosis(loaded_data) == pytest.approx(
        -0.14, 0.1
), "Kurtosis calculation failed"

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / 'data/calificaciones.csv'
#     mean = calculate_mean(FILE_PATH)
#     variance = calculate_variance(FILE_PATH)
#     skewness = calculate_skewness(FILE_PATH)
#     kurtosis = calculate_kurtosis(FILE_PATH)

#     # Mostrar los resultados calculados
#     print(f'Media: {mean}, Varianza: {variance}, Asimetría: {skewness}, Curtosis: {kurtosis}')
