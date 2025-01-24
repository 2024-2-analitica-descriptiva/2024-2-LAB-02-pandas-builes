import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
# Ruta de los archivos
path_tbl0 = "files/input/tbl0.tsv"
path_tbl2 = "files/input/tbl2.tsv"

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    # Leer ambos archivos TSV
    tbl0 = pd.read_csv(path_tbl0, sep="\t")
    tbl2 = pd.read_csv(path_tbl2, sep="\t")

    # Realizar la combinación (merge) entre tbl0 y tbl2 usando 'c0' como clave
    merged_df = pd.merge(tbl0, tbl2, on="c0")

    # Agrupar por la columna 'c1' de tbl0 y sumar los valores de 'c5b' de tbl2
    result = merged_df.groupby('c1')['c5b'].sum()

    return result

# Imprimir el resultado
print(pregunta_13())