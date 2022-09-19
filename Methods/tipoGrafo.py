import numpy

from Initialize import create_igraph_graph


def tipoGrafo(data):
    global grafo

    if type(data) is numpy.ndarray:
        grafo = create_igraph_graph(data, data_format='matrix')

    if type(data) is dict:
        grafo = create_igraph_graph(data, data_format='adj_list')

    if any(grafo.is_loop()):
        return 3

    if any(grafo.is_multiple()):
        return 2

    if grafo.is_directed():
        return 1

    if grafo.is_simple():
        return 0
