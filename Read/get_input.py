import os
import numpy as np


def read_instance(inst: str):

    # Here I got the path of the 'instances' directory
    file_path = os.path.join(os.getcwd(), 'instances', f'{inst}.txt')

    # Numpy's loadtxt method can read simply formatted files, which is the case here
    # It takes the values from the file and stores they into a multidimensional numpy array
    matrix = np.loadtxt(file_path)

    # Numpy's shape method returns the shape of a np.array in a tuple
    matrix_shape = np.shape(matrix)

    # If the tuple has a unique value, that means we're reading a unidimensional array
    # Here we're working with matrices, lines and columns, so we are going to say that the unidimensional array has 1
    # line and matrix_shape[0] columns
    if len(matrix_shape) == 1:
        return matrix, (1, matrix_shape[0])

    # matrix_shape = (nrows, ncols)
    return matrix, matrix_shape


if __name__ == '__main__':
    print(read_instance('exemplo'))
