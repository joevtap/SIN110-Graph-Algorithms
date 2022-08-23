import sys
from Read import read_instance
from Output import output_results


# Arguments: [1]Datasets located in 'instances' directory (e.g. 'exemplo,zachary' without quotation marks)
def main():
    datasets: str = sys.argv[1]

    # The dataset argument is converted to a list, then I iterate over it
    for dataset in datasets.split(','):
        # read_instance() function returns a tuple containing the read matrix, and it's shape
        matrix, shape = read_instance(dataset)

        # The shape itself is a tuple (nrows, ncols)
        nrows, ncols = shape

        result = f'{dataset};{nrows};{ncols}'

        # Here I reformatted the result string to print it to the terminal
        print(result.replace(';', ' = ', 1).replace(';', ' '))

        # output_results() function takes a list of strings.
        # Those are going to be appended to a file of the given format
        output_results([result], 'results.csv')


if __name__ == '__main__':
    try:
        main()
    except IndexError:  # This means the program read an out of index value
        print('Execute this script providing the required arguments')
    except FileNotFoundError:  # This means the program couldn't find the file because of it's name or format
        print('Provide correct file names')
