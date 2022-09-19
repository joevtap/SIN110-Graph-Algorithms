from Initialize import create_igraph_graph


def removeVertice(matriz, vi):
    grafo = create_igraph_graph(matriz)

    grafo.delete_vertices(vi)
    return grafo.get_adjacency()
