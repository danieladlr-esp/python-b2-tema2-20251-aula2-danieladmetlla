import pandas as pd
from ej2b1 import read_csv_basic, read_csv_header_issue, read_csv_multi_index, read_csv_custom_separator

# Rutas de los archivos CSV para las pruebas
BASIC_CSV_PATH = 'data/ramen-ratings.csv'
HEADER_ISSUE_CSV_PATH = 'data/ej2b1/ramen_ratings_with_header_issue.csv'
MULTI_INDEX_CSV_PATH = 'data/ej2b1/ramen_ratings_multi_index.csv'
SEMICOLON_CSV_PATH = 'data/ej2b1/ramen_ratings_decimal_comma.csv'

def test_read_csv_basic():
    df = read_csv_basic(BASIC_CSV_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_read_csv_header_issue():
    df = read_csv_header_issue(HEADER_ISSUE_CSV_PATH, header_row=3)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert 'Brand' in df.columns  # Verificar si la columna 'Brand' está presente

def test_read_csv_multi_index():
    df = read_csv_multi_index(MULTI_INDEX_CSV_PATH, index_cols=['Brand', 'Style'])
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(df.index, pd.MultiIndex)  # Comprobar si el índice es un MultiIndex

def test_read_csv_custom_separator():
    df = read_csv_custom_separator(SEMICOLON_CSV_PATH, separator=';', decimal=',')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    # Comprobar que 'Stars' se ha convertido correctamente a float
    # Nota: Asegúrate de que 'Stars' es el nombre correcto de la columna de interés
    assert df['Stars'].dtype == float or df['Stars'].dtype == 'float64'
