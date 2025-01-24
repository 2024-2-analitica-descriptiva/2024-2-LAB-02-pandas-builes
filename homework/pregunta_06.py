import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

path = "files/input/tbl1.tsv"
def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    df = pd.read_csv(path, sep='\t')

    #  df['c4']: Selecciona la columna c4 del DataFrame.
    # .str.upper(): Convierte todos los valores de la columna a mayúsculas.
    # .unique(): Obtiene los valores únicos de la columna.
    # sorted(): Ordena los valores únicos alfabéticamente.
    return sorted(df['c4'].str.upper().unique())

print(pregunta_06())
