from ej2b3 import CountryPopulationAnalyzer  # Asegúrate de cambiar 'your_script_name' al nombre de tu script
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def test_web_url_accessibility():
    response = requests.get(url)
    assert response.status_code == 200, "The webpage should be accessible"

def test_read_population_data():
    analyzer = CountryPopulationAnalyzer(url)
    data = analyzer.read_population_data()
    assert not data.empty, "The population table should not be empty"

def test_get_table_by_match_valid_match():
    analyzer = CountryPopulationAnalyzer(url)
    table = analyzer.read_table_by_match("Spain")
    assert table is not None and not table.empty, "Should find a table for 'Spain'"

def test_get_table_by_match_invalid_match():
    analyzer = CountryPopulationAnalyzer(url)
    table = analyzer.read_table_by_match("InvalidCountry")
    assert table is None, "Should not find any table for an invalid match"
