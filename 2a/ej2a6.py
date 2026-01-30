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


def gaussian(x: float, amplitude: float, mean: float, stddev: float) -> float:
    
    return amplitude * np.exp(-((x - mean) ** 2) / (2 * stddev ** 2))

def gaussian_fit_and_integration(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Tuple[t.Tuple[float], float]:
    x = np.array(data_x)
    y = np.array(data_y)
    # 1. ESTIMACIONES INICIALES para los parámetros de la gaussiana
    amplitude_guess = np.max(y)  # La amplitud es aproximadamente el valor máximo
    mean_guess = x[np.argmax(y)]  # La media está cerca del punto con valor máximo
    stddev_guess = (np.max(x) - np.min(x)) / 4  # Estimación del ancho
    
    initial_guess = [amplitude_guess, mean_guess, stddev_guess]
    
    # 2. AJUSTE DE CURVA usando curve_fit
    try:
        # curve_fit ajusta la función gaussiana a los datos
        params, params_covariance = optimize.curve_fit(
            gaussian, x, y, p0=initial_guess, maxfev=5000
        )
        
        # Desempaquetar parámetros ajustados
        amplitude_fit, mean_fit, stddev_fit = params
        
    except Exception as e:
        print(f"Error en el ajuste de curva: {e}")
        # Si falla el ajuste, usar las estimaciones iniciales
        amplitude_fit, mean_fit, stddev_fit = initial_guess
    
    # 3. INTEGRACIÓN NUMÉRICA de la gaussiana ajustada
    try:
        # Definir la gaussiana ajustada como función lambda para integrar
        fitted_gaussian = lambda x_val: gaussian(x_val, amplitude_fit, mean_fit, stddev_fit)
        
        # Calcular la integral sobre el rango de los datos
        integral_value, integral_error = integrate.quad(
            fitted_gaussian,  # Función a integrar
            np.min(x),        # Límite inferior
            np.max(x),        # Límite superior
            epsabs=1e-6,      # Tolerancia absoluta de error
            epsrel=1e-6       # Tolerancia relativa de error
        )
        
        print(f"Error estimado en la integral: {integral_error:.2e}")
        
    except Exception as e:
        print(f"Error en la integración: {e}")
        integral_value = 0.0
    
    # 4. RETORNAR RESULTADOS
    gaussian_params = (float(amplitude_fit), float(mean_fit), float(stddev_fit))
    
    return gaussian_params, float(integral_value)



def plot_gaussian_fit(
    data_x: t.List[float], data_y: t.List[float], gaussian_params: t.Tuple[float]
):
    x = np.array(data_x)
    y = np.array(data_y)
    
    # Extraer parámetros gaussianos
    amplitude, mean, stddev = gaussian_params
    
    # Crear figura y eje
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 1. Graficar datos originales
    ax.scatter(x, y, color='blue', alpha=0.6, s=40, 
               label='Datos Originales', zorder=5)
    
    # 2. Crear curva gaussiana ajustada para graficar
    # Usar más puntos para una curva suave
    x_smooth = np.linspace(np.min(x), np.max(x), 500)
    y_fit = gaussian(x_smooth, amplitude, mean, stddev)
    
    # Graficar curva ajustada
    ax.plot(x_smooth, y_fit, color='red', linewidth=3, 
            label='Curva Gaussiana Ajustada', zorder=4)
    
    # 3. Marcar parámetros importantes
    # Línea vertical en la media
    ax.axvline(x=mean, color='green', linestyle='--', alpha=0.7, 
               label=f'Media (μ) = {mean:.2f}', zorder=3)
    
    # Línea horizontal en la amplitud
    ax.axhline(y=amplitude, color='purple', linestyle=':', alpha=0.7, 
               label=f'Amplitud = {amplitude:.2f}', zorder=3)
    
    # 4. Configurar título y etiquetas
    ax.set_title('Ajuste Gaussiano de Datos', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Variable X', fontsize=14)
    ax.set_ylabel('Variable Y', fontsize=14)
    
    # 5. Agregar información de parámetros en el gráfico
    params_text = f'Parámetros Ajustados:\n'
    params_text += f'Amplitud (A) = {amplitude:.3f}\n'
    params_text += f'Media (μ) = {mean:.3f}\n'
    params_text += f'Desv. Est. (σ) = {stddev:.3f}\n'
    params_text += f'Ancho FWHM = {2.355*stddev:.3f}'
    
    # Colocar texto en una esquina
    ax.text(0.02, 0.98, params_text, 
            transform=ax.transAxes, 
            fontsize=11,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
    
    # 6. Configurar leyenda
    ax.legend(loc='best', fontsize=11, framealpha=0.9)
    
    # 7. Agregar grid
    ax.grid(True, alpha=0.3, linestyle='--', zorder=1)
    
    # 8. Ajustar límites del eje Y para mejor visualización
    y_max = max(np.max(y), amplitude * 1.1)
    ax.set_ylim(bottom=0, top=y_max)
    
    # 9. Ajustar layout
    plt.tight_layout()
    
    # 10. Mostrar gráfico
    plt.show()

    


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# data_x = np.linspace(-5, 5, 100)
# data_y = 3 * np.exp(-(data_x - 1) ** 2 / (2 * 1.5 ** 2)) + np.random.normal(0, 0.2, 100)
# gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
# print("Integral de la curva gaussiana ajustada:", integral)
# plot_gaussian_fit(data_x, data_y, gaussian_params)
