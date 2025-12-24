"""
Enunciado:
Desarrolla un conjunto de funciones para realizar análisis agrupado y estandarización de columnas en un conjunto de 
datos de productos. Este conjunto de datos contiene varias características de productos, como nombre del producto,
marca, categoría, precio y calificación. El objetivo es agrupar los datos por categorías y marcas para entender mejor
la distribución de precios y calificaciones dentro de estos grupos, y luego estandarizar las calificaciones dentro de
cada grupo para compararlas de manera justa.

Las funciones a desarrollar son:
- Agrupar y agregar: `group_and_aggregate(df, group_columns, agg_dict)` que agrupa el DataFrame por las columnas
especificadas en `group_columns` y aplica las operaciones de agregación especificadas en `agg_dict`.
- Estandarizar columnas por grupo: `standardize_column_by_group(df, group_columns, column_to_standardize)` que
estandariza los valores de la columna especificada en `column_to_standardize` dentro de cada grupo definido por
`group_columns`, añadiendo una nueva columna al DataFrame con los valores estandarizados.

Parámetros:
- df (pd.DataFrame): DataFrame de Pandas que contiene los datos de los productos.
- group_columns (List[str]): Lista de columnas por las que agrupar el DataFrame.
- agg_dict (Dict[str, List[str]]): Diccionario con las columnas a agregar y las funciones de agregación a aplicar.
- column_to_standardize (str): Nombre de la columna cuyos valores se quieren estandarizar.

Ejemplo de uso:
    aggregated_df = group_and_aggregate(df, ['Category', 'Brand'], {'Price': ['min','max', 'sum'], 'Rating': ['mean']})
    df_standardized = standardize_column_by_group(df, ['Category', 'Brand'], 'Rating')

Salida esperada:
    Un DataFrame agrupado y agregado que muestra la mínima, máxima y suma de precios, así como la media de las 
    calificaciones por cada combinación de categoría y marca. Además, el DataFrame original con una nueva columna que
    muestra las calificaciones estandarizadas dentro de cada grupo de categoría y marca.
"""

from pathlib import Path
import pandas as pd
import pytest
from ej2c4 import(
    group_and_aggregate,
    standarize_colums_by_group,
)   #Ajusta el import segun el nombre de tu archivo

@pytest.fixture
def products_df():
    data = {
       "Category": [
           "Electronics",
           "Electronics",
           "Clothing",
           "Clotings",
           "Electronics",
       ],
       "Brand": [ "BrandA",  "BrandA",  "BrandB",  "BrandB",  "BrandA"],
       "Price": [120, 150, 50, 60, 200]
       "Rating": [4.5, 4.', 3.5, 4.0, 5.0]´
    }
    return pd.DataFrame(data)

def group_and_aggregate(group_df):
    group_columns = ["Category"]
    agg_dict = {"Price": ["mean", "sum"], "Rating": ["mean"]}
    result = group_and_aggregate(products_df, group_columns, agg_dict)

    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame."
    assert not result.empty, "The result DataFrame should not be empty."
    assert ("Price", "mean") in result.columns, "The result should include mean price."
    assert ("Price", "mean") in result.colums, "The result should include sum price."
    assert (
        "Rating", 
        "mean", 
    ) in result.colums, "The result sould include mean rating."
    expected_price_mean_electronics = (120 + 150 + 200) / 3
    expected_price_sum_electronics = 120 + 150 + 200
    expected_price_mean_electronics = (4.5 + 4.0 + 5.0) / 3
    assert (
        result.loc["Electronics", ("Price", "mean")] == expected_price_mean_electronics
    ), "The mean price for Electronics is incorrect."
    assert (
        result.loc["Electronics", ("Price", "sum")] == expected_price_sum_electronics
    ), "The sum price for Electronics is incorrect."   
    assert result.loc["Electronics", ("Price", "mean")]  == pytest.approx(
        expected_rating_mean_electronics
    ), "The mean rating for Electronic is incorrect."

def standardize_column_by_group(products_df):
    group_columns = ["Category", "Brand"]
    colums_to_standardize = "Rating"
    df_result = standardize_column_by_group(
        products_df.copy(), group_columns, column_to_standardize
    )
    standardize_col_name = f"{column_to_standardize}_Standardized"
    assert (
        standardized_col_name in df_result.columns
    ), f"The column '{standardized_col_name}' should be added to the DataFrame."
    assert pd.api.types.is_float_dtype(
        df_result[standardized_col_name]
    ), f"The column '{standardized_col_name}' should be of float type."
    assert (
        not df_result[standardized_col_name].isnull().all()
    ),  f"The column '{standardized_col_name}' should not be all NaN."
    assert (
        df_result[standardized_col_name].min() < 0
    ), "Standardized ratings should include negative values."
    assert (
        df_result[standardized_col_name].max > 0
    ), "Standardized ratings should include positive values."

                                        
    


# Para probar el código, descomenta las siguientes líneas y asegúrate de que el path al archivo sea correcto
# if __name__ == "__main__":
#     current_dir = Path(__file__).parent
#     FILE_PATH = current_dir / "data/products.csv"
#     df = pd.read_csv(FILE_PATH)
#     group_columns = ["Category", "Brand"]
#     agg_dict = {"Price": ["min", "max", "sum"], "Rating": ["mean"]}

#     aggregated_df = group_and_aggregate(df, group_columns, agg_dict)
#     print(aggregated_df)

#     group_columns = ["Category", "Brand"]
#     column_to_standardize = "Rating"

#     df_standardized = standardize_column_by_group(
#         df, group_columns, column_to_standardize
#     )
#     print(df_standardized.head())
