from ej2b1 import CSVDataProcessor
import pandas as pd

# Prueba para leer datos desde un archivo CSV
def test_read_csv():
    processor = CSVDataProcessor('data/ramen-ratings.csv')
    processor.read_csv()
    assert isinstance(processor.dataframe, pd.DataFrame)
    assert not processor.dataframe.empty

# Prueba para renombrar columnas del DataFrame
def test_rename_columns():
    processor = CSVDataProcessor('data/ramen-ratings.csv')
    processor.read_csv()
    processor.rename_columns({'Review #': 'review_number', 'Brand': 'brand', 'Stars': 'rating'})
    assert 'review_number' in processor.dataframe.columns

# Prueba para seleccionar columnas específicas del DataFrame
def test_select_columns():
    processor = CSVDataProcessor('data/ramen-ratings.csv')
    processor.read_csv()
    processor.select_columns(['Review #', 'Brand'])
    assert processor.dataframe.shape[1] == 2

# Prueba para convertir columnas a valores numéricos
def test_convert_to_numeric():
    processor = CSVDataProcessor('data/ramen-ratings.csv')
    processor.read_csv()
    processor.convert_to_numeric('Stars')
    assert pd.api.types.is_numeric_dtype(processor.dataframe['Stars'])

# Prueba para seleccionar datos usando iloc
def test_select_data():
    processor = CSVDataProcessor('data/ramen-ratings.csv')
    processor.read_csv()
    selected_data = processor.select_data(slice(0, 5))
    assert len(selected_data) == 5

# Prueba para filtrar datos basados en una condición específica
def test_filter_by_condition():
    processor = CSVDataProcessor('data/ramen-ratings.csv')
    processor.read_csv()
    processor.convert_to_numeric('Stars')
    processor.filter_by_condition('Stars > 3')
    assert all(processor.dataframe['Stars'] > 3)
