import numpy

from Initialize import create_igraph_graph
from Methods.tipoGrafo import tipoGrafo


def calcDensidade(data):
    data_format = 'adj_list' if type(data) is dict else 'matrix'
    graph = create_igraph_graph(data, data_format=data_format)

    v = graph.vcount()
    e = graph.ecount()

    print(v, e)

    if tipoGrafo(data) == 1:
        # Directed
        return round((e / (v * (v - 1))), 3)

    # Undirected
    return round(((2 * e) / (v * (v - 1))), 3)

