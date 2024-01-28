import pandas as pd

file_path = "data/ej2b4/ramen-ratings.xlsx"


def read_excel_sheet1(file_path):
    dataframe = pd.read_excel(file_path, sheet_name='Sheet1')
    return dataframe


def read_excel_sheet2_custom(file_path):
    # Función para detectar columnas no vacías
    def is_not_empty_column(col):
        return col.dropna().any()

    dataframe = pd.read_excel(file_path, sheet_name='Sheet2', header=3, skipfooter=4)
    cols_to_use = [col for col in dataframe.columns if is_not_empty_column(dataframe[col])]
    dataframe = dataframe[cols_to_use]

    return dataframe


print(read_excel_sheet1(file_path))
print(read_excel_sheet2_custom(file_path).columns)
