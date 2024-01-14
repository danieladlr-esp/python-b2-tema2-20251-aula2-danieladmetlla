import pytest
from ej2b2 import RamenDataAnalyzer

# Suponiendo que tienes archivos de prueba en una carpeta de prueba
test_file_paths = {
    'csv': 'data/ramen-ratings.csv',
    'json': 'data/ramen-ratings.json',
    'xlsx': 'data/ramen-ratings.xlsx',
    'sqlite': 'data/ramen-ratings.db'
}

# Instancia de la clase para usar en las pruebas
analyzer = RamenDataAnalyzer(test_file_paths)


def test_read_csv():
    df = analyzer.read_csv()
    assert not df.empty
    assert 'Stars' in df.columns


def test_read_json():
    df = analyzer.read_json()
    assert not df.empty
    assert 'Stars' in df.columns


def test_read_excel():
    df = analyzer.read_excel()
    assert not df.empty
    assert 'Stars' in df.columns


def test_read_sqlite():
    df = analyzer.read_sqlite()
    assert not df.empty
    assert 'Stars' in df.columns


def test_analyze():
    result = analyzer.analyze()
    expected_mean = 3.6546759798214974

    assert isinstance(result, dict)
    assert all(format in result for format in ['csv', 'json', 'xlsx', 'sqlite'])
    assert all(isinstance(result[format], float) for format in result)
    # Comprueba que la media calculada para cada formato sea la esperada
    assert all(abs(result[format] - expected_mean) < 1e-6 for format in result)
