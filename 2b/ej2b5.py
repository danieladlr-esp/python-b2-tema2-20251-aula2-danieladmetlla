"""
Enunciado:

Desarrolla un conjunto de funciones para extraer y analizar datos de población de países desde una tabla HTML en
Wikipedia. Estas funciones deben ser capaces de leer tablas HTML con atributos específicos en la página y filtrar para
encontrar datos en una tabla específica basada en un texto de coincidencia.

Implementa las siguientes funciones:
    - read_population_data(url, match_text=None): Función para leer todas las tablas HTML de una página web con
    atributos específicos y, opcionalmente, que contengan un texto de coincidencia, devolviendo una lista de DataFrames.
    - get_table_by_string_match(tables, match_text): Función para extraer una tabla específica de la lista de DataFrames
    que contenga el parámetro match_text.
    - count_tables(tables): Función para contar el número de tablas HTML en la página web.

Parámetros:
    - url (str): URL de la página de Wikipedia con la tabla de población de países para read_population_data.
    - match_text (str, opcional): Texto para identificar la tabla específica que se quiere extraer en
    read_population_data y get_table_by_string_match.
    - tables (List[pd.DataFrame]): Lista de DataFrames que representan las tablas HTML leídas de la página web en
    count_tables.

Funcionamiento y Atributos:
    - La función read_population_data utiliza el parámetro attrs para especificar los atributos HTML que deben tener las
    tablas a leer. En este caso, estamos buscando tablas con la clase wikitable, que es común para las tablas
    estandarizadas en Wikipedia.
    - El parámetro na_values se utiliza para identificar qué cadenas de texto deben ser interpretadas como valores
    NA/NaN (Not Available/Not a Number). Por ejemplo, los guiones o la palabra 'None' se consideran indicadores de datos
    no disponibles.
    - Si se proporciona el parámetro match_text a read_population_data, solo se leerán las tablas que contengan ese
    texto específico, haciendo uso del parámetro match de la función pd.read_html.

Ejemplo:
    tables = read_population_data(url)
    selected_table = get_table_by_string_match(tables, "Spain")
    if selected_table is not None:
        print(selected_table)
    else:
        print("No se encontró la tabla con el texto proporcionado.")

Salida esperada:
    - El número de tablas HTML encontradas en la página con los atributos especificados.
    - Un DataFrame de Pandas con los datos de la tabla que coincide con el texto proporcionado, si existe.
"""

import pandas as pd
import typing as t
import requests
from ej2b5 import read_population_data, get_table_by_string_match, count_tables

#URL for the Wikipedia page with population data
URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def read_population_data():
    #Check if the Wikipedia page is reachable
    responde = request.get(URL)
    assert response.status_code == 200, "Wikipedia page not reachable"

    #Check if tables can be read
    tables = read_population_data(URL)
    assert isinstance(tables, list), "Should return a list"
    assert all(
        isinstance(table, pd.DataFrame) for table in tables
    ), "Each item should be a DataFrame"

def get_table_by_string_match():
    tables = read_population_data(URL)
    #Use a match_text that is known to exist in the tables
    match_text = "Spain"
    match_table = get_table_by_string_match(tables, match_text)
    assert matched_table is not None, f"Should find a table with text {match_text}"
    assert (
        match_text in matched_table.to_string()
    ), f"The table should contain the tect {match_text}"

def count_tables():
    tables = read_population_data(URL)
    assert isinstance(count_tables(tables), int), "Should return an integer"
    assert count_tables(tables) > 0, "Should find one or more tables"

# Para probar el código, descomenta las siguientes líneas
# url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
# tables = read_population_data(url)
# print(f"Número de tablas en la página: {count_tables(tables)}")
# selected_table = get_table_by_string_match(tables, "Spain")

# if selected_table is not None:
#     print(f"Registros en la tabla: {len(selected_table)}")
#     print(f"Nombres de columnas: {selected_table.columns.tolist()}")
#     print(selected_table)
# else:
#     print("No se encontró la tabla con el texto proporcionado.")
