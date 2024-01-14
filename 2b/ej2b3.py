"""
Enunciado:
Desarrolla una clase llamada `CountryPopulationAnalyzer` para extraer y analizar datos de población de países desde una
tabla HTML en Wikipedia. La clase tendrá dos funciones principales:
1. Un método para leer todas las tablas HTML de la web, `read_population_data()`.
2. Un método para extraer datos de una tabla que contenga el parámetro `match` de `pd.read_html`,
`get_table_by_match(match_text)`.

Parámetros:
    - url (str): URL de la página de Wikipedia con la tabla de población de países.
    - match_text (str): Texto para identificar la tabla específica que se quiere extraer.

La clase debe utilizar Pandas para leer y procesar los datos de la tabla HTML.

Ejemplo:
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    analyzer = CountryPopulationAnalyzer(url)
    analyzer.read_population_data()
    print(analyzer.get_table_by_match("United States"))

Salida esperada:
    Un DataFrame de Pandas con los datos de la tabla que coincide con el texto proporcionado.
"""

import pandas as pd
from typing import Union


class CountryPopulationAnalyzer:
    def __init__(self, url):
        self.url = url
        self.population_data = None

    def read_population_data(self) -> pd.DataFrame:
        tables = pd.read_html(self.url)
        self.population_data = tables[0]
        return self.population_data

    def read_table_by_match(self, match_text: str) -> Union[pd.DataFrame, None]:
        try:
            table_data = pd.read_html(self.url, match=match_text)
            return table_data[0] if table_data else None
        except ValueError as e:
            print(f"Error: Could not find a table matching '{match_text}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Para probar el código, descomenta las siguientes líneas
# url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
# analyzer = CountryPopulationAnalyzer(url)
# print(analyzer.read_population_data().size)
# print(analyzer.read_table_by_match("Spain").size)
# print(analyzer.read_table_by_match("Madrid"))
