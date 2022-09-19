from Initialize import create_igraph_graph


def insereVertice(matriz, vi):
    grafo = create_igraph_graph(matriz)

    grafo.add_vertex(vi)
    return grafo.get_adjacency()