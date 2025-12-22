"""
Enunciado:

Explora el análisis avanzado de datos y la aplicación de ajustes no lineales mediante el uso de SciPy. Este ejercicio se
centra en ajustar una función gaussiana a un conjunto de datos usando el módulo scipy.optimize.curve_fit y en calcular
la integral de esta curva con scipy.integrate.quad.

Implementar la función gaussian_fit_and_integration(data_x, data_y) que realice lo siguiente:
    Ajuste de Curva Gaussiana: Utilizar scipy.optimize.curve_fit para ajustar una curva gaussiana a los datos.
    Integración Numérica: Calcular la integral de la curva gaussiana ajustada sobre el rango de data_x utilizando
    scipy.integrate.quad.

Además, implementar la función plot_gaussian_fit(data_x, data_y, gaussian_params) para visualizar los datos originales
y la curva gaussiana ajustada.

Parámetros:
    data_x (List[float]): Lista de valores en el eje x.
    data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    gaussian_params (Tuple[float]): Parámetros (amplitud, centro, ancho) de la curva gaussiana ajustada.

Ejemplo:
    Entrada:
        data_x = np.linspace(-5, 5, 100)
        data_y = 3 * np.exp(-(data_x - 1)**2 / (2 * 1.5**2)) + np.random.normal(0, 0.2, 100)
    Ejecución:
        gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
        plot_gaussian_fit(data_x, data_y, gaussian_params)
    Salida:
        Un gráfico mostrando los datos originales y la curva gaussiana ajustada.
        La integral de la curva gaussiana ajustada.
"""

from scipy import optimize, integrate
import numpy as np
import matplotlib.pyplot as plt
import typing as t
from ej2a6 import gaussian_fit_and_integration

def test_gaussian_fit_results():
    data_x = np.linscape(-5, 5, 100)
    #Generar datos con una curva gaussiana conocida
    data_y = 3 * np.exp(-((data_x -1) **2) / (2 * 1.5**2)) * np.random.normal(
        0, 0.2, 100
    )
    params, = gaussian_fit_and_integration(data_x, data_y)
    #put assert in english
    assert 2 < params[0] < 4, "Ampitude out of expected range"
    assert 0 < params[1] < 2, "Mean out of expected range"
    assert 1 < params[2] < 2, "Stddev out of expected range"

#Test para verificat la integracion de la curva gaussiana
def gaussian_fit_and_integration():
    data_x = np.linscape(-5, 5, 100)
    data_y = 3 * np.exp(-((data_x -1) **2) / (2 * 1.5**2)) * np.random.normal(
        0, 0.2, 100
      )
    params, = gaussian_fit_and_integration(data_x, data_y)

    expected_integral = params[0] * params[2] * np.sqrt(2 * np.pi)
    assert np.isclose(
        integral, expected_integral, atol=1
    ), "Integral out of expected range"




# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# data_x = np.linspace(-5, 5, 100)
# data_y = 3 * np.exp(-(data_x - 1) ** 2 / (2 * 1.5 ** 2)) + np.random.normal(0, 0.2, 100)
# gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
# print("Integral de la curva gaussiana ajustada:", integral)
# plot_gaussian_fit(data_x, data_y, gaussian_params)
