import pandas as pd

# Supongamos que este es tu script con las funciones definidas
from ej2b3 import read_population_data, get_table_by_match, count_tables

def test_read_population_data():
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    tables = read_population_data(url)
    assert isinstance(tables, list)
    assert all(isinstance(table, pd.DataFrame) for table in tables)

def test_get_table_by_match():
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    tables = read_population_data(url)
    table = get_table_by_match(tables, "Spain")
    assert isinstance(table, pd.DataFrame)
    assert "Spain" in table.to_string()

def test_count_tables():
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    tables = read_population_data(url)
    count = count_tables(tables)
    assert isinstance(count, int)
    assert count > 0  # Asegura que haya al menos una tabla
