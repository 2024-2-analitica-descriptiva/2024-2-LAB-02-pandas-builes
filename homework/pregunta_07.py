import pandas as pd
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
path = "files/input/tbl0.tsv"

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """

    df = pd.read_csv(path, sep='\t')
    suma_c1_groupby_c2 = df.groupby('c1').sum()['c2']
    return suma_c1_groupby_c2

print(pregunta_07())
