import numpy

from Initialize import create_igraph_graph


def tipoGrafo(data):
    if type(data) is numpy.ndarray:
        global grafo
        grafo = create_igraph_graph(data)

    if any(grafo.is_loop()):
        return 3

    if any(grafo.is_multiple()):
        return 2

    if grafo.is_directed():
        return 1

    if grafo.is_simple():
        return 0