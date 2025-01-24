import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

path = "files/input/tbl0.tsv"

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """


    # Leer el archivo TSV
    df = pd.read_csv(path, sep='\t')

    # primero agrupamos por c1 y luego sacamos el maximo de c2
    maximo_c2_por_c1 = df.groupby('c1')['c2'].max()

    return maximo_c2_por_c1

print(pregunta_05())