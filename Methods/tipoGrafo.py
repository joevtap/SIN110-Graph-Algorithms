from Initialize import create_igraph_graph


def tipoGrafo(matriz):
    grafo = create_igraph_graph(matriz)

    if any(grafo.is_loop()):
        return 3

    if any(grafo.is_multiple()):
        return 2

    if grafo.is_directed():
        return 1

    if grafo.is_simple():
        return 0
