"""
Enunciado:
Desarrolla un conjunto de funciones en Python para manejar y procesar un conjunto de datos de calificaciones que 
potencialmente contiene valores faltantes o no válidos. El conjunto de datos está almacenado en un archivo CSV y
contiene calificaciones en diversas materias para un grupo de estudiantes. El objetivo es limpiar los datos, eliminar
filas con datos faltantes en columnas clave, y aplicar técnicas de imputación para tratar los valores faltantes en
ciertas columnas.

Las funciones a desarrollar son:
1. Leer el archivo CSV: `read_csv(filepath: str)` que lee el archivo CSV desde la ruta especificada y devuelve un 
DataFrame de pandas.
2. Limpiar el DataFrame: `clean_dataframe(df)` que limpia el DataFrame reemplazando valores no válidos ('Null', '-',
'NA', 'na', y espacios en blanco) por `NaN`, y convierte las columnas numéricas a su tipo correspondiente, excepto la
primera columna.
3. Eliminar filas con `NaN` en una columna específica: `dropna_specific_row_in_column(df, column_name: str)` que
elimina las filas que contienen un valor `NaN` en la columna especificada por `column_name`.
4. Rellenar valores faltantes en una columna específica: `fillna_method(df, column_name: str, fill_method='ffill',
fill_value=None, limit=1)` que rellena los valores faltantes en la columna especificada utilizando un método de 
relleno especificado (`ffill` para relleno hacia adelante con un límite de 1, o `mean` para rellenar con el promedio
de la columna).

Parámetros:
- filepath (str): Ruta al archivo CSV que contiene los datos de calificaciones.
- column_name (str): Nombre de la columna en la cual aplicar la eliminación de filas o el relleno de valores 
faltantes.
- fill_method (str): Método de relleno para tratar valores faltantes (`ffill` para relleno hacia adelante, `mean` 
para el promedio).
- fill_value (Optional[float]): Valor específico de relleno a usar si se especifica. Útil solo cuando 
`fill_method` es `mean`.
- limit (int)`: Número máximo de rellenos consecutivos a aplicar cuando se utiliza `ffill`.

Ejemplo de uso:
    df_cleaned = clean_dataframe(df_v2)
    df_drop_na_rows = dropna_specific_row_in_column(df_cleaned, 'Name')
    df_filled_column_ffill = fillna_method(df_drop_na_rows, 'Hindi', fill_method='ffill', limit=1)
    df_filled_column_mean = fillna_method(df_filled_column_ffill, 'Maths', fill_method='mean')


Salida esperada:
- Un DataFrame limpio y procesado donde las filas con valores faltantes en columnas clave han sido eliminadas, y los
valores faltantes en ciertas columnas han sido tratados mediante técnicas de imputación específicas.
"""

from pathlib import Path
import pandas as pd
import numpy as np


def read_csv(filepath):
    # Write here your code
    return pd.read_csv(filepath)


def clean_dataframe(df: pd.DataFrame):
    # Write here your code
    dictionary = df.to_dict()
    for column in dictionary:
        if column != "Name":
            for i in dictionary[column]:
                if not str(dictionary[column][i]).isnumeric():
                    dictionary[column][i] = np.nan
                if column == "Maths" and str(dictionary[column][i]).isnumeric():
                    dictionary[column][i] = float(dictionary[column][i])
    return pd.DataFrame(dictionary)


def dropna_specific_row_in_column(df, column_name):
    # Write here your code
    dictionary = df.to_dict()
    NaNs = ["NaN", "nan", "-", "na", "NA", " "]
    for i in range(len(dictionary[column_name])):
        if str(dictionary[column_name][i]) in NaNs:
            for column in dictionary:
                dictionary[column].pop(i)
    return pd.DataFrame(dictionary)


def fillna_method(df, column_name, fill_method="ffill", fill_value=None, limit=1):
    # Write here your code
    dictionary = df.to_dict()
    NaNs = ["NaN", "nan", "-", "na", "", "NA", " "]
    ffill = 0
    ffill_count = 0
    mean = 0
    mean_limit = 0

    if fill_method == "mean":
        for i in dictionary[column_name]:
            if str(dictionary[column_name][i]) not in NaNs:
                mean += dictionary[column_name][i]
                mean_limit += 1
        mean /= mean_limit

    for i in dictionary[column_name]:
        if str(dictionary[column_name][i]) not in NaNs:
            ffill = dictionary[column_name][i]
            ffill_count = 0
        if str(dictionary[column_name][i]) in NaNs:
            if fill_method == "ffill":
                if ffill_count < limit:
                    dictionary[column_name][i] = ffill
            elif fill_method == "mean":
                if fill_value == None:
                    print(dictionary[column_name][i])
                    dictionary[column_name][i] = mean
                    print(dictionary[column_name][i])
                else:
                    dictionary[column_name][i] = fill_value
            else:
                print("Error: Metodo no valido.")
                break

    return pd.DataFrame(dictionary)


# Para probar el código, descomenta las siguientes líneas y asegúrate de que el path al archivo sea correcto
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/grades_na.csv"
    dataframe = read_csv(FILE_PATH)
    df_cleaned = clean_dataframe(dataframe)
    df_drop_na_rows = dropna_specific_row_in_column(df_cleaned, "Name")
    df_filled_column_ffill = fillna_method(
        df_drop_na_rows, "Hindi", fill_method="ffill", limit=1
    )
    df_filled_column_mean = fillna_method(
        df_filled_column_ffill, "Maths", fill_method="mean"
    )

    print(dataframe.head())
    print(df_filled_column_mean.head())
