import numpy as np
import igraph


def create_igraph_graph(data, data_format='matrix'):  # Credits to Professor Rafael Frinhani - SIN110
    graph = igraph.Graph()

    if type == data_format:
        n_vertices = np.shape(data)[0]
        graph.add_vertices(n_vertices)

        # Label                   0 to n_vertices
        graph.vs['label'] = range(0, graph.vcount())

        for vi in range(0, n_vertices):  # For each vertex vi
            for vj in range(vi + 1, n_vertices):  # For each vertex vj
                aux = data[vi][vj]  # Aux var to keep track of items in the matrix
                while aux > 0:
                    graph.add_edges([(vi, vj)])
                    aux -= 1

    if data_format == 'adj_list':
        n_vertices = len(data)
        graph.add_vertices(n_vertices)

        graph.vs['label'] = range(0, graph.vcount())

        # for vi in data:
        #     for vj in vi:


    return graph


def criaListaAdjacencias(matriz):
    graph = create_igraph_graph(matriz)

    igraph_adj_list = graph.get_adjlist()

    dict_adj_list = dict(enumerate(igraph_adj_list))

    return dict_adj_list
