import numpy as np
import igraph


def create_igraph_graph(matrix):  # Credits to Professor Rafael Frinhani - SIN110
    graph = igraph.Graph()

    n_vertices = np.shape(matrix)[0]
    graph.add_vertices(n_vertices)

    # Label                   0 to n_vertices
    graph.vs['label'] = range(0, graph.vcount())

    for vi in range(0, n_vertices):  # For each vertex vi
        for vj in range(vi + 1, n_vertices):  # For each vertex vj
            aux = matrix[vi][vj]  # Aux var to keep track of items in the matrix
            while aux > 0:
                graph.add_edges([(vi, vj)])
                aux -= 1
    return graph
