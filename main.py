import sys
from Read import read_instance
from Initialize import create_igraph_graph
from Initialize import visualize_graph


def main(datasets: str):
    for dataset in datasets.split(','):
        matrix, _ = read_instance(dataset)
        print(matrix, end='\n\n')

        graph = create_igraph_graph(matrix)
        print(graph, end='\n\n')

        visualize_graph(graph)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:  # This means the program read an out of index value
        print('Execute this script providing the required arguments')
    except FileNotFoundError:  # This means the program couldn't find the file because of it's name or format
        print('Provide correct file names')
