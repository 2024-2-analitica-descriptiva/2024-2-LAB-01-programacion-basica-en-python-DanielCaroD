"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("files\input\data.csv", "r") as file:
        lines = file.readlines()
    
    data = {"A":[], "B":[], "C":[], "D":[], "E":[]}

    for line in lines:
        columns = line.split()
        letter = columns[0]
        num = int(columns[1])

        data[letter].append(num)
    
    result = [(key, max(values), min(values)) for key,values in data.items()]

    return result