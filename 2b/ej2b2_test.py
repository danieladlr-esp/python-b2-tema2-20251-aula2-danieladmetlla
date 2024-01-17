import sqlite3
import pandas as pd
from pandas.testing import assert_frame_equal

from ej2b2 import to_numeric, read_csv, read_json, read_excel, read_sqlite, analyze

def test_to_numeric():
    assert to_numeric("3.5") == 3.5
    assert pd.isna(to_numeric("not_a_number"))


def test_read_csv():
    df = read_csv('data/ramen-ratings.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert pd.api.types.is_numeric_dtype(df['Stars'])


def test_read_json():
    df = read_json('data/ramen-ratings.json')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert pd.api.types.is_numeric_dtype(df['Stars'])


def test_read_excel():
    df = read_excel('data/ramen-ratings.xlsx')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert pd.api.types.is_numeric_dtype(df['Stars'])


def test_read_sqlite():
    # Crear una base de datos SQLite de prueba
    conn = sqlite3.connect(':memory:')
    test_data = pd.DataFrame({'Brand': ['Brand A', 'Brand B'], 'Stars': [4.5, 3.5]})
    test_data.to_sql('ramen_ratings', conn, index=False)

    # Probar la función read_sqlite
    df = read_sqlite(':memory:')
    assert_frame_equal(df, test_data)

    conn.close()


def test_analyze():
    file_paths = {
        'csv': 'data/ramen-ratings.csv',
        'json': 'data/ramen-ratings.json',
        'xlsx': 'data/ramen-ratings.xlsx',
        'sqlite': 'data/ramen-ratings.db'
    }
    result = analyze(file_paths)
    assert isinstance(result, dict)
    assert all(isinstance(value, float) for value in result.values())
