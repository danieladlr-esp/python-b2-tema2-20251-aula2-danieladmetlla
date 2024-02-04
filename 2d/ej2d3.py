"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de regresión lineal entre el número promedio
de habitaciones por vivienda (RM) y el valor medio de las viviendas ocupadas por sus propietarios (MEDV) en el conjunto
de datos de viviendas, utilizando `scipy.stats.linregress` y `matplotlib` para la visualización. El archivo CSV
'housing.csv' contiene datos relevantes para este análisis.

Las funciones a desarrollar son:
1. Realizar análisis de regresión lineal: `calculate_linear_regression(file_path: str, variable_1: str, variable_2: str)
que lee un archivo CSV y realiza una regresión lineal entre dos variables dadas, devolviendo la pendiente, la
intersección, el valor r, el valor p y el error estándar de la pendiente.
2. Graficar la regresión lineal y los puntos de datos: `plot_linear_regression(file_path: str, variable_1: str,
variable_2: str, slope: float, intercept: float)` que utiliza `matplotlib` para visualizar la línea de regresión lineal
junto con los puntos de datos de las dos variables seleccionadas.

Parámetros:
    file_path (str): Ruta del archivo CSV que contiene los datos de vivienda.
    variable_1 (str): Nombre de la primera variable para el análisis de regresión (e.g., 'RM').
    variable_2 (str): Nombre de la segunda variable para el análisis de regresión (e.g., 'MEDV').
    slope (float): Pendiente de la línea de regresión lineal.
    intercept (float): Intersección de la línea de regresión lineal con el eje y.

Ejemplo de uso:
    slope, intercept, r_value, p_value, std_err = calculate_linear_regression(housing_csv_path, 'RM', 'MEDV')
    plot_linear_regression(housing_csv_path, 'RM', 'MEDV', slope, intercept)

Salida esperada:
    Una gráfica que muestra tanto los puntos de datos de RM vs MEDV como la línea de regresión lineal calculada.
"""

from typing import Tuple
import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


def perform_linear_regression(data: pd.DataFrame, variable_1: str, variable_2: str) -> Tuple[float, float, float, float, float]:
    slope, intercept, r_value, p_value, std_err = linregress(data[variable_1], data[variable_2])
    return slope, intercept, r_value, p_value, std_err


def plot_regression_line(data: pd.DataFrame, variable_1: str, variable_2: str, slope: float, intercept: float,
                         return_fig_ax_test=False):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data[variable_1], data[variable_2], alpha=0.5, label='Datos')
    ax.plot(data[variable_1], slope * data[variable_1] + intercept, color='red', label='Línea de regresión')
    ax.set_xlabel(variable_1)
    ax.set_ylabel(variable_2)
    ax.set_title(f'Linear Regression between {variable_1} and {variable_2}')
    ax.legend()

    if return_fig_ax_test:
        return fig, ax
    else:
        plt.show()


# Para probar el código, descomenta este código
# file_path = './data/housing.csv'
# variable_1 = 'RM'
# variable_2 = 'MEDV'
# data = pd.read_csv(file_path, skiprows=14)
#
# slope, intercept, r_value, p_value, std_err = perform_linear_regression(data, variable_1, variable_2)
#
# print(f'Análisis de Regresión Lineal entre {variable_1} y {variable_2}:')
# print(f'Pendiente: {slope}, Intersección: {intercept}, Valor r: {r_value}, Valor p: {p_value},'
#       f'Error estándar: {std_err}')
#
# # Graficar la línea de regresión
# fig, ax = plot_regression_line(data, variable_1, variable_2, slope, intercept, return_fig_ax_test=False)
