"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    with open("files\input\data.csv", "r") as file:
        lines = file.readlines()

    data = {"A":0, "B":0, "C":0, "D":0, "E":0}

    for line in lines:
        columns = line.split()
        letter = columns[0]
        data[letter] += 1
    
    result = [(key, value) for key, value in data.items()]
    
    return result