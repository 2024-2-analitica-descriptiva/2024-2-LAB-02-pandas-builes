import pandas as pd
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


path = "files/input/tbl0.tsv"

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    # 1. Leer el archivo `tbl0.tsv`
    df = pd.read_csv(path, sep='\t')
    
    # 2. Agrupar por la columna `c1`
    grouped = df.groupby('c1')['c2']

    # 3. Ordenar los valores de `c2` dentro de cada grupo
    sorted_values = grouped.apply(lambda x: sorted(x))

    # 4. Convertir los valores ordenados a cadenas de texto y unirlos con ':'
    concatenated = sorted_values.apply(lambda x: ':'.join(map(str, x)))

    # 5. Resetear el índice para convertir el resultado en un DataFrame
    result = concatenated.reset_index()

    # 6. Establecer la columna `c1` como índice para que coincida con el formato de la respuesta
    result = result.set_index('c1')

    return result

print(pregunta_10())
