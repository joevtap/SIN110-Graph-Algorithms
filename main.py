import sys
from Read import read_instance
from Output import output_results


# Arguments: [1]Datasets located in 'figures' directory (e.g. 'exemplo,zachary' without quotation marks)
def main():
    datasets: str = sys.argv[1]

    for dataset in datasets.split(','):
        matrix, shape = read_instance(dataset)
        nrows, ncols = shape

        result = f'{dataset}; {nrows}; {ncols}'

        print(result.replace(';', ''))
        output_results([result], 'results.csv')


if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print('Execute this script providing the required arguments')
    except FileNotFoundError:
        print('Provide correct file names')
