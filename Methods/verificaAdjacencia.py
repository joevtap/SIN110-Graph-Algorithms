from Initialize import create_igraph_graph

def verificaAdjacencia(matriz, vi, vj):
    grafo = create_igraph_graph(matriz)
    return grafo.are_connected(vi, vj)

