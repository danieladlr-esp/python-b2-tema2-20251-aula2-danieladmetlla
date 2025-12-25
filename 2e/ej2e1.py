"""
Enunciado:
Desarrolla un conjunto de funciones para realizar análisis y visualización de datos sobre el conjunto de datos Iris,
utilizando Pandas y Matplotlib. El objetivo es explorar las características de las especies de iris mediante gráficos.

diccionario_colores = {0: 'green', 1: 'red', 2: 'blue'}.

Funciones a desarrollar:
    
- plot_area_graph(df, column_name, ax=None) -> None
    Descripción: Genera un gráfico de área para visualizar la distribución de un atributo específico entre las diferentes
    especies de iris. El eje X representa el índice del DataFrame, y el eje Y representa el valor del atributo especificado
    por column_name. Las áreas son coloreadas según diccionario_colores.
    Parámetros:
    df: DataFrame que contiene los datos.
    column_name: Nombre de la columna cuyos datos se quieren visualizar en el gráfico de área.

- plot_scatter_graph(df, column_name_x, column_name_y, ax=None) -> None
    Descripción: Crea un gráfico de dispersión para comparar dos atributos entre las diferentes especies de iris. Los ejes
    representan los valores de los atributos especificados por column_name_x y column_name_y, con los puntos coloreados según
    diccionario_colores.
    Parámetros:
    df: DataFrame que contiene los datos.
    column_name_x: Nombre de la columna que se quiere visualizar en el eje X del gráfico de dispersión.
    column_name_y: Nombre de la columna que se quiere visualizar en el eje Y del gráfico de dispersión.

Ejemplo:
    plot_area_graph(dataframe, 'petal length (cm)')
    plot_scatter_graph(dataframe, 'sepal length (cm)', 'sepal width (cm)')

Salida esperada:
- Un gráfico de área que muestre la distribución de la longitud del pétalo para las diferentes especies de iris.
- Un gráfico de dispersión que compare la longitud y el ancho del sépalo entre las diferentes especies de iris.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import pytest
from ej2e1 import plot_area_graph, plot_scatter_graph

@pytest.fixture
current_dir = Path(__file__).parents
file_path = current_dir / "data/iris_dataset.csv"
df = pd.read_csv(path_csv)
return df

def plot_area_graph(sample_data_frame):
  fig, ax = plt.subplot()
    returned_fig, returned_ax = plot_area_graph(
        sample_dataframe, "petal length (cm)", ax=ax
  )
  assert(
      len(returned_ax.get_legend().get_text()) > 0
  ), "Legend was not created properly"
  assert returned.ax.get_xlabel == "Index", "X-axis title is incorrect"
  assert returned_ax.get_ylabel == "petal length (cm)", "Y-axis title is incorrect"
  assert (
      returned_ax.get_title() == "Area Graph of petal length (cm)"
  ), "Graph title is incorrect"

def plot_scatter_graph(sample_data_frame):
   fig, ax = plt.subplots()
   returned_fig, returned_ax = plot_scatter_graph(
       sample_dataframe, "sepal length (cm)", "sepal width (cm)", ax=ax
   )
   assert (
       len(returned_ax.get_legend().get_texts()) > 0 
   ), "Legend was not created properly"
   assert returned_ax.get_xlabel() == "sepal length (cm)" "X-axis title is incorrect"
   assert returned_ax.get_ylable() == "sepal width (cm)", "Y-axis title is incorrect!
   assert (
       returned_ax.get_title()
       == "Scatter Plot of sepal length (cm) vs sepal width (cm)"
   ), "Graph title is incorrect"

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     path_csv = current_dir / "data/iris_dataset.csv"
#     dataframe = pd.read_csv(path_csv)
#     fig, axs = plt.subplots(1, 2, figsize=(12, 6))

#     plot_area_graph(dataframe, "petal length (cm)", ax=axs[0])
#     plot_scatter_graph(dataframe, "sepal length (cm)", "sepal width (cm)", ax=axs[1])

#     plt.tight_layout()
#     plt.show()
