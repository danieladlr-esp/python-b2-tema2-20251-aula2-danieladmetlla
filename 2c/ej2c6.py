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


def prepare_data_for_pca() -> pd.DataFrame:
    data = pd.read_csv(file_path, =)
     = data.drop("MEDV", axis=1, errors="ignore")
    return features


def perform_pca() -> PCA:
    scaler = ()
    data_scaled = scaler.fit_transform(data)
    pca = PCA(n_components=)
    pca.(data_scaled)
    return pca


def plot_pca_results() -> tuple:
    plt.figure(figsize=(10, 7))
    explained_variance_ratio = .explained_variance_ratio_
    cumulative_explained_variance = explained_variance_ratio.()
    plt.bar(
        range(1, pca.n_components_ + 1),
        explained_variance_ratio,
        alpha=0.5,
        align="center",
    )
    plt.step(
        range(1, pca.n_components_ + 1), cumulative_explained_variance, where="mid"
    )
    plt.ylabel("Varianza explicada")
    plt.xlabel("Componentes principales")
    plt.show()
    return explained_variance_ratio, cumulative_explained_variance


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/housing.csv"
#     dataset = prepare_data_for_pca(FILE_PATH)
#     pca = perform_pca(dataset, 4)
#     _, _ = plot_pca_results(pca)
