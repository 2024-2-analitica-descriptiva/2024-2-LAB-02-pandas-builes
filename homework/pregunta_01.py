import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

#ruta de los archivos
path = "../files/input/tbl0.tsv"

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """

    # convertimos el archivo a un dataframe
    df = pd.read_csv(path, sep='\t')
    
    # retornamos la cantidad de filas
    # shape[0] retorna la cantidad de filas
    return df.shape[0]

print(pregunta_01())

