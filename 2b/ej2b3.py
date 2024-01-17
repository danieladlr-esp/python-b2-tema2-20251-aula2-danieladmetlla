"""
Enunciado:
Desarrolla un conjunto de funciones para extraer y analizar datos de población de países desde una tabla HTML en
Wikipedia. Estas funciones deben ser capaces de leer todas las tablas HTML de la página y extraer datos de una tabla
específica basada en un texto de coincidencia.

Implementa las siguientes funciones:
    - read_population_data(url): Función para leer todas las tablas HTML de una página web y devolver una lista de
    DataFrames.
    - get_table_by_match(tables, match_text): Función para extraer una tabla específica de la lista de DataFrames que
    contenga el parámetro match_text.
    - count_tables(tables): Función para contar el número de tablas HTML en la página web.

Parámetros:
    url (str): URL de la página de Wikipedia con la tabla de población de países en read_population_data.
    match_text (str): Texto para identificar la tabla específica que se quiere extraer en get_table_by_match.
    tables (List[pd.DataFrame]): Lista de DataFrames que representan las tablas HTML leídas de la página web en
    count_tables.

Estas funciones deben utilizar Pandas para leer y procesar los datos de la tabla HTML.

Ejemplo:
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    tables = read_population_data(url)
    print(count_tables(tables))
    print(get_table_by_match(tables, "Spain"))

Salida esperada:
    El número de tablas HTML encontradas en la página.
    Un DataFrame de Pandas con los datos de la tabla que coincide con el texto proporcionado.
"""
import pandas as pd
import typing as t

def read_population_data(url: str) -> t.List[pd.DataFrame]:
    return pd.read_html(url)

def get_table_by_match(tables: t.List[pd.DataFrame], match_text: str) -> t.Union[pd.DataFrame, None]:
    try:
        for table in tables:
            if match_text in table.to_string():
                return table
        print(f"No se encontró una tabla que coincida con '{match_text}'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

def count_tables(tables: t.List[pd.DataFrame]) -> int:
    return len(tables)

# Para probar el código, descomenta las siguientes líneas
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
tables = read_population_data(url)
print(f"Número de tablas en la página: {count_tables(tables)}")
print(get_table_by_match(tables, "Spain"))
print(f"Tabla 2: {read_population_data(url)[1]}")
