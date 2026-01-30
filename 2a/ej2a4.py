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


def compare_monthly_sales(
    sales_year1: list, sales_year2: list, sales_year3: list, months: list
) -> t.Tuple[plt.Figure, plt.Axes, plt.Axes]:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    x_positions = np.arange(len(months))
    width = 0.35
    # Gráfico de barras para el primer año
    bars1 = ax1.bar(x_positions - width/2, sales_year1, width, 
                    label='Año 1 (2020)', color='skyblue', alpha=0.8)
    
    # Gráfico de barras para el segundo año
    bars2 = ax1.bar(x_positions + width/2, sales_year2, width, 
                    label='Año 2 (2021)', color='lightcoral', alpha=0.8)
    
    # Calcular ventas acumuladas para cada mes (suma de año1 y año2)
    cumulative_sales = [y1 + y2 for y1, y2 in zip(sales_year1, sales_year2)]
    
    # Crear eje Y secundario para las ventas acumuladas
    ax1_twin = ax1.twinx()
    
    # Gráfico de línea para ventas acumuladas
    line = ax1_twin.plot(x_positions, cumulative_sales, 'g-', 
                         marker='o', linewidth=2, markersize=6,
                         label='Ventas Acumuladas (2020+2021)')
    
    # Configurar el primer gráfico
    ax1.set_title('Comparación de Ventas Mensuales: 2020 vs 2021', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Meses', fontsize=12)
    ax1.set_ylabel('Ventas Mensuales', fontsize=12, color='black')
    ax1_twin.set_ylabel('Ventas Acumuladas', fontsize=12, color='green')
    
    # Configurar ejes X
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(months, rotation=45, ha='right')
    
    # Crear leyendas combinadas
    # Primero obtenemos las handles y labels de ambos ejes
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax1_twin.get_legend_handles_labels()
    
    # Combinamos las leyendas
    all_handles = handles1 + handles2
    all_labels = labels1 + labels2
    
    # Agregar leyenda combinada
    ax1.legend(all_handles, all_labels, loc='upper left', fontsize=10)
    
    # Añadir grid al gráfico principal
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Segundo gráfico: pastel para el tercer año
    # -----------------------------------------------------------------
    # Calcular porcentajes
    total_sales_year3 = sum(sales_year3)
    percentages = [(sale / total_sales_year3) * 100 for sale in sales_year3]
    
    # Crear etiquetas para el gráfico de pastel (mes + porcentaje)
    pie_labels = [f'{month}\n{perc:.1f}%' 
                  for month, perc in zip(months, percentages)]
    
    # Crear gráfico de pastel
    wedges, texts, autotexts = ax2.pie(sales_year3, labels=pie_labels, 
                                       autopct='%1.1f%%', startangle=90,
                                       textprops={'fontsize': 9})
    
    # Mejorar la apariencia de los textos
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax2.set_title('Distribución de Ventas Mensuales para 2022', 
                  fontsize=14, fontweight='bold')
    
    # Ajustar el layout para evitar superposición
    plt.tight_layout()
    
    return fig, ax1, ax2

    

# Para probar el código, descomenta las siguientes líneas
sales_2020 = np.random.randint(100, 500, 12)
sales_2021 = np.random.randint(100, 500, 12)
sales_2022 = np.random.randint(100, 500, 12)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


if __name__ == "__main__":
    fig, ax1, ax2 = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    plt.show()
    
