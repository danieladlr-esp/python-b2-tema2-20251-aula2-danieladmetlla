import pytest
from ej2d1 import calculate_mean, calculate_variance, calculate_skewness, calculate_kurtosis

@pytest.fixture
def loaded_data():
    return './data/calificaciones.csv'

def test_calculate_mean(loaded_data):
    assert calculate_mean(loaded_data) == pytest.approx(5.0, 0.1), "Mean calculation failed"

def test_calculate_variance(loaded_data):
    assert calculate_variance(loaded_data) == pytest.approx(2.5, 0.1), "Variance calculation failed"

def test_calculate_skewness(loaded_data):
    assert calculate_skewness(loaded_data) == pytest.approx(0.0, 0.1), "Skewness calculation failed"

def test_calculate_kurtosis(loaded_data):
    assert calculate_kurtosis(loaded_data) == pytest.approx(-0.15, 0.1), "Kurtosis calculation failed"