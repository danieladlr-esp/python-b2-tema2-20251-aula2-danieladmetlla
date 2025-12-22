"""
Enunciado:
Desarrolla la función enhanced_compare_monthly_sales para visualizar y analizar datos de ventas de tres años distintos
utilizando la biblioteca Matplotlib. Esta función debe crear gráficos para comparar las ventas mensuales de dos años y
mostrar la distribución de las ventas de un tercer año.

Detalles de la Implementación:

    Gráfico de Barras y Líneas:
        Crea un gráfico de barras para comparar las ventas mensuales de los dos primeros años.
        Superpone un gráfico de líneas en el mismo eje para mostrar las ventas acumuladas de estos dos años.
        Utiliza ejes gemelos para manejar las escalas de los gráficos de barras y líneas adecuadamente.

    Gráfico de Pastel en Subfigura:
        Presenta las ventas del tercer año en un gráfico de pastel en una subfigura separada, mostrando la distribución
        porcentual de las ventas por mes.

Parámetros de la Función:
    sales_year1 (List[int]): Lista de ventas mensuales para el primer año.
    sales_year2 (List[int]): Lista de ventas mensuales para el segundo año.
    sales_year3 (List[int]): Lista de ventas mensuales para el tercer año.
    months (List[str]): Lista de nombres de los meses.

Especificaciones de los Gráficos:
    Gráfico de Barras y Líneas:
        Título: "Comparación de Ventas Mensuales: 2020 vs 2021"
        Ejes:
            Eje X: Nombres de los meses.
            Eje Y izquierdo: Ventas mensuales.
            Eje Y derecho: Ventas acumuladas.
        Leyendas para diferenciar cada año y las ventas acumuladas.

    Gráfico de Pastel:
        Título: "Distribución de Ventas Mensuales para 2022"
        Etiquetas para cada segmento del pastel, mostrando el porcentaje de ventas por mes.

Ejemplo:
    Entrada:
        sales_2020 = [120, 150, 180, 200, ...] # Ventas para cada mes en 2020
        sales_2021 = [130, 160, 170, 210, ...] # Ventas para cada mes en 2021
        sales_2022 = [140, 155, 175, 190, ...] # Ventas para cada mes en 2022
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    Ejecución:
        enhanced_compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    Salida:
        Dos gráficos dentro de la misma figura, uno combinando barras y líneas para 2020 y 2021, y otro en forma de
        pastel para 2022.
"""

import matplotlib.pyplot as plt
import numpy as np
import typing as t


def test_enhanced_compare_monthly_sales_creates_figure_and_axes():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12) 
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, ax1, ax2 = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    assert fig is not None, "The function should create a Matplotlib figure"
    assert ax1 is not None, "The function should create the first Matplotlib axis"
    assert ax2 is not None, "The function should create the second Matplotlib axis"

Test para verificar las características específicas de ax1 (Gráfico de barras y líneas)
def test_ax1_features():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12) 
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  
    _,ax1, _ = compare_monthly_sales(sales_2020, sales 2022, months) 
    assert (
        ax1.titlle.get_text() == "Monthly Sales Comparison: 2020 vs 2021"
    ), "The tittle of ax1 should be correct"
    assert (
        len(ax1.patches) == 24 
    ), "There should be 24 bars in the bar chart (12 for each year)"

#Test para verificar las características específicas de ax2(Gráfico de pastel)
def test_ax2_features():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12) 
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]  
_, _, ax2 = compare_monthly_sales(sales 2020, sales 2021, sales_2022, months)
    assert (
    ax2.tittle.get_text() == "2022 Monthly Sales Distribution"
    assert (
    len(ax2.patches) == 12
), "There should be 12 segments in the pie chart (one for each month

#Test adicional para verificar si la longitud de los datos y las etiquetas coinciden
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12)
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]      
    assert len(sales_2020) == len(
        months
    ), "Length of sales data and month labels must match for the first year"
    assert len(sales_2021) == len(
        months
    ), "Length of sales data and mont labels must match for the second year" 
    assert len(sales_2022) == len(   
        months
    ), "Length of sales data month labels must match for the third year"

    
# Para probar el código, descomenta las siguientes líneas
# sales_2020 = np.random.randint(100, 500, 12)
# sales_2021 = np.random.randint(100, 500, 12)
# sales_2022 = np.random.randint(100, 500, 12)
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# if __name__ == "__main__":
#     fig, ax1, ax2 = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
#     plt.show()
