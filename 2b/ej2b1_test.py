import pandas as pd

from ej2b1 import read_csv, rename_columns, select_columns, convert_to_numeric, filter_by_condition, select_data

def test_read_csv():
    df = read_csv('data/ramen-ratings.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_rename_columns():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df = rename_columns(df, {'A': 'X', 'B': 'Y'})
    assert list(df.columns) == ['X', 'Y']

def test_select_columns():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
    df = select_columns(df, ['A', 'B'])
    assert list(df.columns) == ['A', 'B']

def test_convert_to_numeric():
    df = pd.DataFrame({'A': ['1', '2'], 'B': ['3', 'four']})
    df = convert_to_numeric(df, 'A')
    assert pd.api.types.is_numeric_dtype(df['A'])

def test_filter_by_condition():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [3, 2, 1]})
    df = filter_by_condition(df, 'A > 1')
    assert len(df) == 2

def test_select_data():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [3, 2, 1]})
    selected_df = select_data(df, 1)
    assert len(selected_df) == 1
    assert selected_df.iloc[0]['A'] == 2