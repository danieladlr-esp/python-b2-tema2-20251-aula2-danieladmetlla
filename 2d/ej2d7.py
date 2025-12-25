"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de clustering utilizando
`sklearn.cluster.KMeans` en el conjunto de datos de crédito alemán. Este conjunto de datos contiene varias
características financieras y personales de los solicitantes de crédito, y el objetivo es agrupar a los solicitantes
en k clusters basados en sus características para identificar patrones y perfiles de riesgo.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_clustering(file_path: str)` que lee el archivo CSV y prepara los datos para
   el clustering, realizando cualquier limpieza o preprocesamiento necesario.
2. Realizar el clustering con KMeans: `perform_kmeans_clustering(data, n_clusters: int)` que aplica el algoritmo KMeans
   a los datos preparados, utilizando un número específico de clusters.
3. Visualizar los resultados: `visualize_clusters(data, labels, is_testing_execution)` que visualiza los resultados del
   clustering, idealmente utilizando una reducción de dimensionalidad para representar los datos en 2D o 3D si es
   posible.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de crédito alemán.
    n_clusters (int): Número de clusters a utilizar en el análisis KMeans.

Ejemplo:
    data = prepare_data_for_clustering('./data/german_credit_data.csv')
    labels = perform_kmeans_clustering(data, 5)
    visualize_clusters(data, labels, is_testing_execution)

Salida esperada:
    Una visualización de los clusters formados por el análisis KMeans, mostrando cómo se agrupan los solicitantes de
    crédito según sus características.
"""

from pathlib import Path
from typing import Tuple
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pytest
from ej2d7 import (
   prepare_data_for_clustering, 
   perform_kmeans_clustering, 
   visualize_clusters,
)

@pytest.fixture
def german_credit_data_path():
   current_dir = Path(__file__).parent
   file_path = current_dir / "data/german_credit.csv"
   return file_path
  
def prepare_data_for_clustering(german_credit_data_path):
   data_scaled = prepare_data_for_clustering(german_credit_data_path) 
   assert data_scaled.mean(axis=0).all() == pytest.approx(
      1, abs=1e-6
   ), "The data should have a standard deviation of 1

def perform_kmeans_clustering(german_credit_data_path):
      data_scaled = prepare_data_for_clustering(german_credit_data_path)
      n_clusters = 5
      labels = perform_kmeans_clustering(data_scaled, n_clusters)
      assert len(labels) > 0, "The labels should not be empty"
      assert (
         len(set(labels)) ==n_clusters
      ), The number of unique labels should match the number of clusters"
   
def visualize_clusters(german_credit_data_path)
     data_scaled = prepare_data_for_clustering(german_credit_data_path)
     n_clusters = 5
     labels = perform_kmeans_clustering(data_scaled, n_clusters)
     data_reduced, fig, ax = visualize_cllusters(data_scaled, labels, True)
     assert data_reduced.shape[1] == 2, "The data should be reduced to 2 dimensions"

# Para probar el código, desconmenta las siguientes líneas
# if __name__ == '__main__':
#     current_dir = Path(__file__).parent
#     file_path = current_dir / 'data/german_credit_data.csv'
#     data = prepare_data_for_clustering(file_path)
#     labels = perform_kmeans_clustering(data, 5)
#     data_reduced, fig, ax = visualize_clusters(data, labels, False)
