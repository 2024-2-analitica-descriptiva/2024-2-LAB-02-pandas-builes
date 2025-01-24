import pandas as pd
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

path = "files/input/tbl1.tsv"

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """

    df = pd.read_csv(path, sep='\t')

    
    # Agrupar los valores de `c4` por `c0` y unirlos con una coma
    grouped = df.groupby("c0")["c4"].apply(lambda x: ','.join(sorted(x)))

    # Convertir el resultado en un DataFrame
    result = grouped.reset_index()

    return result

# Imprimir el resultado
print(pregunta_11())
