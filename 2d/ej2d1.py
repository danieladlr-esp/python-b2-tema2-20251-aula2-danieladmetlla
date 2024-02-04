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

import pandas as pd
from scipy import stats

def calculate_mean(file_path: str) -> float:
    data = pd.read_csv(file_path)
    return data['Calificaciones'].mean()

def calculate_variance(file_path: str) -> float:
    data = pd.read_csv(file_path)
    return data['Calificaciones'].var()

def calculate_skewness(file_path: str) -> float:
    data = pd.read_csv(file_path)
    return stats.skew(data['Calificaciones'])

def calculate_kurtosis(file_path: str) -> float:
    data = pd.read_csv(file_path)
    return stats.kurtosis(data['Calificaciones'])


# Para probar el código, descomenta las siguientes líneas
# calificaciones_csv_path = './data/calificaciones.csv'
# mean = calculate_mean(calificaciones_csv_path)
# variance = calculate_variance(calificaciones_csv_path)
# skewness = calculate_skewness(calificaciones_csv_path)
# kurtosis = calculate_kurtosis(calificaciones_csv_path)
#
# # Mostrar los resultados calculados
# print(f'Media: {mean}, Varianza: {variance}, Asimetría: {skewness}, Curtosis: {kurtosis}')
