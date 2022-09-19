from Initialize import create_igraph_graph


def removeAresta(matriz, vi, vj):
    grafo = create_igraph_graph(matriz)

    grafo.delete_edges(vi, vj)
    return grafo.get_adjacency()
