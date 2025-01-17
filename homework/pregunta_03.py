"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
    
    data = {}

    for line in lines:
        columns = line.split()
        letter = columns[0]
        num = int(columns[1])
        
        if letter not in data:
            data[letter] = 0
        data[letter] += num
    
    result = sorted([(key, value) for key, value in data.items()])

    return result