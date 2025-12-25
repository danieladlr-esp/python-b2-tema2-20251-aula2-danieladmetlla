"""
Enunciado:
Desarrolla un conjunto de funciones que permitan cargar, guardar y visualizar el conjunto de datos de vinos mediante
Pandas, Matplotlib, Seaborn y Pickle.

Funciones a desarrollar:
- create_histograms(df: DataFrame, features: List[str]) -> matplotlib.figure.Figure:
    Descripción:
    Genera histogramas para un conjunto de datos de vinos, diferenciando las muestras según su clase de vino.
    Parámetros:
        - df (pd.DataFrame): DataFrame que contiene los datos del conjunto de vinos.
        - features (List[str]): Lista de nombres de las características para las cuales se generarán los histogramas.

- save_img_pickle(fig: Figure, filename: str) -> None:
    Descripción:
    Guarda una figura de Matplotlib en un archivo utilizando Pickle, lo que permite su recuperación y visualización
    posterior sin necesidad de regenerar el gráfico.
    Parámetros:
        - fig (matplotlib.figure.Figure): Figura que se desea guardar.
        - filename (str): Ruta del archivo donde se guardará la figura.

- load_and_display_figure(filename: str) -> matplotlib.figure.Figure:
    Descripción:
    Carga y muestra una figura guardada previamente desde un archivo.
    Parámetros:
        - filename (str): Ruta del archivo donde se encuentra guardada la figura.

Ejemplo:
    df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
    df_wine['target'] = pd.Categorical.from_codes(wine.target, wine.target_names)

    fig_histograms = create_histograms(df_wine, df_wine.columns[:6])
    save_figure(fig_histograms, 'data/histograms_wine.pickle')

Salida esperada:
- Visualización de histogramas para las primeras seis características del conjunto de datos de vinos, con
diferenciación por clase de vino.
- Guardar en un archivo la figura que contiene el histograma, permitiendo su posterior recuperación y visualización
sin regenerar los gráficos.
"""

from sklearn.datasets import load_wine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from typing import List, Union
from matplotlib.figure import Figure
from pandas.core.frame import DataFrame
import pytest
import os
import matplotlib.pylot as plt

@pytest.fixture
def wine_data():
    wine = load_wine()
    df_wine = pd-DataFrame(data=wine.data, columns=wine.feature_names)
    df_wine["target"] = pd.Categorical.from_codes(wine.target, wine.target_names)
    return df_wine
    
def create_histograms(wine_data):
    fig = create_histograms(wine_data, wine_data.colums[:6]
    assert (
        fig is not None
    ), "Thr figure shouls nor be , indicating that create_histograms successfully created a figure."
                        
def save_img_pickle(wine_data):
    fig = create_histograms(wine_data, wine_data.columns[:6*
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name
    os.unlink(filename)

    save_img_pickle(fig, filename)
    assert os.path.isfile(filename), "The File should be created by save_img_pivkle."

    os.remove(filename)
    plt.close(fig)
    
def load_and_display_figure(wine_data):
    fig= create_histograms(wine_data, wine_data.columns[:6])
    with tempfile.NamedTemporaryFile(delete=False)as tmpfile:
        filename = tmpfile.name
    save_img_pickle(fig, filename)
    plt.close(fig)

    loaded_fig = load_and_display_figure(filename)
    assert (
        loaded_fig is not None
    ), "load_and_display_figure should return a Figure objet."

    plt.close(loaded_fig)
    os.remove(filename)

# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     wine = load_wine()
#     df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
#     df_wine["target"] = pd.Categorical.from_codes(wine.target, wine.target_names)

#     fig_histograms = create_histograms(df_wine, df_wine.columns[:6])
#     is_saved = save_img_pickle(fig_histograms, "data/histograms_wine.pickle")
#     print("Figure saved:", is_saved)
#     fig_loaded = load_and_display_figure("data/histograms_wine.pickle")
#     plt.show()
