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


def linear_regression_and_interpolation(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Dict[str, t.Any]:
    x = np.array(data_x)
    y = np.array(data_y)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    regression_line = slope * x + intercept
    r_squared = r_value ** 2
    interpolation_func = interpolate.interp1d(x, y, kind="linear", fill_value="extrapolate")
    interpolated_y = interpolation_func(x)
    results = {
        "regression_slope": slope,
        "regression_intercept": intercept,
        "regression_r2": r_squared,
        "regression_line": regression_line,
        "interpolation_func": interpolation_func
        "interpolated_y": interpolated_y
    }
    return results






def plot_results(data_x: t.List[float], data_y: t.List[float], results: t.Dict):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Crear figura y eje
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Convertir datos a arrays de NumPy
    x = np.array(data_x)
    y = np.array(data_y)
    
    # 1. Graficar datos originales
    ax.scatter(x, y, color='blue', alpha=0.6, s=50, label='Datos Originales')
    
    # 2. Graficar regresión lineal
    ax.plot(x, results['regression_line'], 
            color='red', 
            linewidth=3, 
            label=f'Regresión Lineal\n(y = {results["regression_slope"]:.2f}x + {results["regression_intercept"]:.2f})')
    
    # 3. Graficar interpolación
    ax.plot(x, results['interpolated_y'], 
            color='green', 
            linewidth=2, 
            linestyle='--',
            label='Interpolación Lineal')
    
    # Configurar título y etiquetas
    ax.set_title('Análisis de Datos: Regresión e Interpolación Lineal', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Variable X', fontsize=14)
    ax.set_ylabel('Variable Y', fontsize=14)
    
    # Configurar leyenda
    ax.legend(loc='best', fontsize=12, framealpha=0.9)
    
    # Agregar grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Añadir información estadística en el gráfico
    stats_text = f'R² = {results["regression_r2"]:.4f}\n'
    stats_text += f'Pendiente = {results["regression_slope"]:.4f}\n'
    stats_text += f'Intercepto = {results["regression_intercept"]:.4f}'
    
    # Colocar texto en una esquina
    ax.text(0.02, 0.98, stats_text, 
            transform=ax.transAxes, 
            fontsize=11,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Ajustar layout
    plt.tight_layout()
    
    # Mostrar gráfico
    plt.show()


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# data_x = np.linspace(0, 10, 100)
# data_y = 3 * data_x + 2 + np.random.normal(0, 2, 100)
# results = linear_regression_and_interpolation(data_x, data_y)
# plot_results(data_x, data_y, results)
