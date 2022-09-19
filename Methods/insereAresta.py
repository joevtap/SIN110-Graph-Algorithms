from Initialize import create_igraph_graph


def insereAresta(matriz, vi, vj):
    grafo = create_igraph_graph(matriz)

    grafo.add_edge(vi, vj)
    return grafo.get_adjacency()
