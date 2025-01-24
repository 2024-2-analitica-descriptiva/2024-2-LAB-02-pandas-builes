import pandas as pd
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

#ruta de los archivos
path = "files/input/tbl0.tsv"

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """

    
    # convertimos el archivo a un dataframe
    df = pd.read_csv(path, sep='\t')

    #df.columns retorna una lista con los nombres de las columnas
    # retornamos la cantidad de columnas
    return len(df.columns)

print(pregunta_02())


