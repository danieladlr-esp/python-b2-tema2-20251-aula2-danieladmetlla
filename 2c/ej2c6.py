"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de componentes principales (PCA) utilizando
`sklearn.decomposition.PCA` en el conjunto de datos de viviendas. Este conjunto de datos contiene varias características
de viviendas en áreas suburbanas de Boston, y el objetivo es reducir la dimensionalidad de los datos para identificar
las principales componentes que explican la mayor parte de la varianza en el conjunto de datos.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_pca(file_path: str)` que lee el archivo CSV y prepara los datos eliminando
cualquier característica no numérica. Se debe saltar las primeras 14 filas del archivo CSV, que contienen información
adicional sobre el conjunto de datos.
2. Realizar PCA: `perform_pca(data, n_components: int)` que realiza PCA en los datos preparados, reduciendo a
`n_components` número de dimensiones, en este caso a 4 dimensiones.
3. Visualizar los resultados: `plot_pca_results(pca)` que visualiza los resultados de PCA, incluyendo la varianza
explicada por cada componente principal.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de viviendas.
    n_components (int): Número de componentes principales a retener en el análisis PCA.

Ejemplo de uso:
    pca = perform_pca(data, 4)
    plot_pca_results(pca)

Salida esperada:
    Una visualización de la varianza explicada por los componentes principales y, opcionalmente, una transformación de
    los datos originales proyectada en las principales componentes.
"""

from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pytest
from ej2c6 import prepare_data_for_pca, perform_pca

@pytest.fixture
def sample_data_path():
    current_dir = Path(_file_).parent
    FILE_PATH = current_dir / "data/housing.csv"
    return FILE_PATH
    
def prepare_data_for_pca(sample_data_path):
    data = prepare_data_for_pca(sample_data_path)
    assert not data.empty, "The data should not be empty"
    assert (
        "MEDV" not in data.columns
    ), "The target variable should not be included in the data"

def perform_pca(sample_data_path):
    data = prepare_data_for_pca(sample_data_path)
    pca = perform_pca(data, n-components=4)
    assert isinstance(pca, PCA), "The returned object should be an instance of PCA" 
    assert pca.n_components_ == 4, "The number of principal components should be 4"

def plot_pca_results(pca_result):
    """
   #Gráfica el resultado de un PCA con dos componentes principales
   :param pca_result: array o matriz con al menos 2 columnas (PC1, PC2)
   """
        plt.figure()
        plt.scatter(pca_result[:, 0], pca_result:, 1])
        plt.xlabel("PC1")
        plt.ylabel(PC2")
        plt.tittle(PCA: Result)
        plt.show

        
        plt.figure()
        plt.scatter(pca_result[:, 2], pca_result:, 3])
        plt.xlabel("PC3")
        plt.ylabel(PC4")
        plt.tittle(PCA Result)
        plt.show
                   
# Para probar el código, descomenta las siguientes líne# if __name__ == "__main__":
# current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/housing.csv"
#     dataset = prepare_data_for_pca(FILE_PATH)
#     pca = perform_pca(dataset, 4)
#     _, _ = plot_pca_results(pca)
