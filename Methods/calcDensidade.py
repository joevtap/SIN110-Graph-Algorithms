from Initialize import create_igraph_graph
from Methods.tipoGrafo import tipoGrafo


def calcDensidade(matriz):
    graph = create_igraph_graph(matriz)
    v = graph.vcount()
    e = graph.ecount()

    if tipoGrafo(matriz) == 1:
        # Directed
        return round((e / (v * (v - 1))), 3)

    # Undirected
    return round(((2 * e) / (v * (v - 1))), 3)

