import sys
from Read import read_instance
from Initialize import create_igraph_graph, criaListaAdjacencias
from Initialize import visualize_graph
from Methods import calcDensidade, tipoGrafo, verificaAdjacencia, insereVertice, insereAresta, removeAresta, \
    removeVertice


def main(datasets: str):
    for dataset in datasets.split(','):
        matrix, _ = read_instance(dataset)
        print(matrix, end='\n\n')

        graph = create_igraph_graph(matrix)
        print(graph, end='\n\n')

        print(criaListaAdjacencias(matrix))

        print('Tipo:', tipoGrafo(matrix))
        print('Densidade:', calcDensidade(matrix))

        if dataset == 'ponte':
            print('Ponte: 2 - 3?', verificaAdjacencia(matrix, 2, 3))
            print('Ponte: 1 - 2?', verificaAdjacencia(matrix, 1, 2))

            ponte_com_4 = insereVertice(matrix, 4)
            print('Ponte: Inserido vertice com id 4: \n', ponte_com_4)
            # visualize_graph(create_igraph_graph(ponte_com_4))

            aresta_1_4 = insereAresta(ponte_com_4, 1, 4)
            print('Ponte: Inserido aresta 1 - 4: \n', aresta_1_4)
            # visualize_graph(create_igraph_graph(aresta_1_4))

            sem_aresta_2_3 = removeAresta(matrix, 2, 3)
            print('Ponte: Removida aresta 2 - 3: \n', sem_aresta_2_3)
            # visualize_graph(create_igraph_graph(sem_aresta_2_3))

            sem_vertice_2 = removeVertice(matrix, 2)
            print('Ponte: Removido vertice 2: \n', sem_vertice_2)
            # visualize_graph(create_igraph_graph(sem_vertice_2))

        if dataset == 'teste_remove':
            sem_aresta = removeAresta(matrix, 0, 1)
            # visualize_graph(create_igraph_graph(sem_aresta))

            sem_vertice = removeVertice(matrix, 0)
            # visualize_graph(create_igraph_graph(sem_vertice))

        visualize_graph(graph)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:  # This means the program read an out of index value
        print('Execute this script providing the required arguments')
    except FileNotFoundError:  # This means the program couldn't find the file because of it's name or format
        print('Provide correct file names')
