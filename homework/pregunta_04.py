import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


path = "files/input/tbl0.tsv"

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """

    # Leer el archivo TSV
    df = pd.read_csv(path, sep='\t')

    # Calcular el promedio de c2 por cada letra de c1
    # groupby('c1') agrupa los datos comunes en c1
    # ['c2'] selecciona la columna c2
    # mean() calcula el promedio
    promedio_c2_por_c1 = df.groupby('c1')['c2'].mean()

    return promedio_c2_por_c1

print(pregunta_04())