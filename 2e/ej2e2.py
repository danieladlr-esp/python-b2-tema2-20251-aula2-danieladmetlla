"""
Enunciado:
Desarrolla un conjunto de funciones para entrenar un modelo de clasificación y visualizar tanto las fronteras de
decisión como la matriz de confusión, utilizando bibliotecas como Matplotlib, Numpy, y Scikit-learn.

Funciones a desarrollar:
    - create_meshgrid(X, resolution=0.02) -> (np.ndarray, np.ndarray)
     Descripción: 
     Genera un mallado (meshgrid) a partir de los datos de entrada X. Este mallado se utiliza luego para visualizar
     las fronteras de decisión del modelo. 
     Parámetros: 
        X (np.ndarray): Datos de entrada. resolution (float): Resolución del mallado.

    - plot_decision_boundaries(ax, X, y, classifier, resolution=0.02) -> matplotlib.axes._axes.Ax
     Descripción: 
     Utiliza el mallado creado por create_meshgrid y colorea las regiones según las predicciones del clasificador.
     Parámetros: 
        ax (matplotlib.axes._axes.Ax): Eje donde se dibujará.
        X (np.ndarray): Datos de entrada. 
        y (np.ndarray): Etiquetas verdaderas.
        classifier: Modelo clasificador entrenado.
        resolution (float): Resolución del mallado.

    - plot_confusion_matrix(ax, y_true, y_pred, classes) -> matplotlib.axes._axes.Ax
    Descripción:
    Genera y visualiza la matriz de confusión para evaluar el rendimiento del modelo clasificador, mostrando las
    instancias correctamente y erróneamente clasificadas entre las diferentes clases. 
    Parámetros:
        ax (matplotlib.axes._axes.Ax): Eje donde se dibujará. y_true 
        (np.ndarray): Etiquetas verdaderas. y_pred 
        (np.ndarray): Etiquetas predichas. classes 
        (List[str]): Nombres de las clases.

    - train_and_visualize(X, y) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray, classifier)
    Descripción:
    Entrena un clasificador k-NN con los datos de entrenamiento 'X' y 'y', y devuelve los conjuntos de entrenamiento
    y prueba, junto con el clasificador entrenado. El parámetro de 'weights' debe ser 'uniform' y el de 'metric' será
    'minkowski'.
    Parámetros:
        X (np.ndarray): Datos de entrada
        y (np.ndarray): Etiquetas

Ejemplo:
    X_train, X_test, y_train, y_test, classifier = train_and_visualize(X, y)

Salida Esperada:
- Una visualización de las áreas donde el modelo predice cada clase, mostrando la habilidad del clasificador para
separar las clases.
- Una matriz de confusión que resume las predicciones correctas e incorrectas, permitiéndote evaluar cuán bien funciona
el modelo.
"""


from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pytest
from ej2e2 import (
    create_meshgrid, 
    plot_decision_boundaries, 
    plot_decision_matrix,
    train_and_visualize, 
)

def create_meshgrid():
    X = np.array([[1, 2], [3, 4], [5, 6]]
    xx1, xx2 = create_meshgrid(X)
    assert xx1.shape == xx2.shape, "Meshgrid arrays should have the same shape"
    assert (
        xx1.min() < X[:, 0].min()
    ), "Meshgrid x1 min should be less than X[:, 0].min()"
    assert (
        xx2.min() < X[:, 1].min()
    ), "Meshgrid x2 min should be less than X[:, 1].min()"


def plot_decision_boundaries():
    iris = load_iris()
    X = iris.data[:, :2]
    y = iris.target
    fig, ax = plt.subplots()
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X, y)
    ax = plot_decision_boundaries(ax, X, y, classifier)
    assert ax, "plot_decision_boundaries should return a matplotlib axis"
    assert (
        len(ax.collections) > 0
    ), "plot_decision_boundaries should add colecctions to the axis"

def plot_confusion_matrix():
    fig, ax = plt.subplots()
    y_true = np.array([0, 1, 2, 2, 1])
    y_pred = np.array([0, 1, 2, 1, 1])
    classes = ["class 0", "class 1", "class 2"]
    ax = plot_confusion_matrix(ax, y_true, y_pred, classes)
    assert ax, "plot_confusion_matrix should return a matplotlib axis"
    assert len(ax.texts) > 0, "Confusion metrix should contain text amotations"
    assert (
        ax.get_title() == "Confusion Matrix"
    ), "plot_confusion_matrix should set the correct title"

def train_and_visualize():
    iris = load_iris()
    X = iris.data[:, :2]
    y = iris.target
    X_train, X_test, y_train, y_test, classifier = train_and_visualize(X, y)
    assert len (X_train) > 0, "X_train should not be empty"
    assert len (X_test) > 0, "X_test should not be empty"
    assert len (y_train) > 0, "y_train should not be empty"
    assert len (y_test) > 0, "y_test should not be empty"
    assert len (np.unique(classifier.predict(X_test))) <= len(
        np.unique(y)
    ), "Predicted classes should not exceed the actual classes"
    


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     iris = datasets.load_iris()
#     X = iris.data[:, :2]
#     y = iris.target

#     X_train, X_test, y_train, y_test, classifier = train_and_visualize(X, y)

#     fig, axs = plt.subplots(1, 2, figsize=(12, 5))
#     plot_decision_boundaries(axs[0], X_train, y_train, classifier)
#     plot_confusion_matrix(
#         axs[1], y_test, classifier.predict(X_test), classes=iris.target_names
#     )

#     plt.tight_layout()
#     plt.show()
