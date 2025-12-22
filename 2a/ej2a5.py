"""
Enunciado:
Explora el análisis de datos mediante la realización de una regresión lineal y la interpolación de un conjunto de datos.
Este ejercicio se centra en el uso de scipy.optimize para llevar a cabo una regresión lineal y en la aplicación de
scipy.interpolate para la interpolación de datos.

Implementa la función linear_regression_and_interpolation(data_x, data_y) que realice lo siguiente:
    - Regresión Lineal: Ajustar una regresión lineal a los datos proporcionados.
    - Interpolación: Crear una interpolación lineal de los mismos datos.

Adicionalmente, implementa la función plot_results(data_x, data_y, results) para graficar los datos originales,
la regresión lineal y la interpolación.

Parámetros:
    - data_x (List[float]): Lista de valores en el eje x.
    - data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    - results (Dict): Resultados de la regresión lineal e interpolación.

Ejemplo:
    - Entrada:
        data_x = np.linspace(0, 10, 100)
        data_y = 3 - data_x + 2 + np.random.normal(0, 0.5, 100) # Datos con tendencia lineal y algo de ruido
    - Ejecución:
        results = linear_regression_and_interpolation(data_x, data_y)
        plot_results(data_x, data_y, results)
    - Salida:
        Un gráfico mostrando los datos originales, la regresión lineal y la interpolación.
"""

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import typing as t
from ej2a5 import linear_regresion_and_interpolation
def test_linear_regression_results():
    data_x = np.linspace(0, 10, 100)
    ata_y = 3 * data_x + 2 + np.random.normal(0, 0.5, 100)
    results = linear_regression_and_interpolation(data_x, data_y)

    #Asegurarse de que los resultados contengan los componentes esperados
    assert "Linear_regression" in results
    assert "interpolated_data" in results

    #Verificar si la pendiente y la intersección estan en un rango esperado
    assert 2.5 < results["linear_regression"]["slope"] < 3.5
    assert 1.5 < results["linear_regression"]["intercept"] < 2.5

#Test para verificar la longitug de los datos interpolados
def test_interpolated_data_length():
    data_x = np_linspace(0, 10, 100)
    data_y = 3 * data_x + 2 + np.random.normal(0, 0.5, 100)
    results = linear_regression_and_interpolation(data_x, data_y)

    assert len(results["interpolated_data"]) == len(data_x


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# data_x = np.linspace(0, 10, 100)
# data_y = 3 * data_x + 2 + np.random.normal(0, 2, 100)
# results = linear_regression_and_interpolation(data_x, data_y)
# plot_results(data_x, data_y, results)
