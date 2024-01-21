import pandas as pd
from ej2b2 import read_json_basic, read_json_with_orientation, read_json_and_normalize

# Suponiendo que los JSONs están en un directorio llamado 'data'
BASIC_JSON_PATH = 'data/ramen-ratings.json'
ORIENT_JSON_PATH = 'data/ej2b2/ramen-ratings-records.json'
NORMALIZE_JSON_PATH = 'data/ej2b2/ramen-ratings-nested.json'

def test_read_json_basic():
    df = read_json_basic(BASIC_JSON_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_read_json_with_orientation():
    df = read_json_with_orientation(ORIENT_JSON_PATH, orient='records')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_read_json_and_normalize():
    df = read_json_and_normalize(NORMALIZE_JSON_PATH, record_path=['data'])
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
