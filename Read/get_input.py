import os
import numpy as np


def read_instance(inst: str):

    file_path = os.path.join(os.getcwd(), 'figures', f'{inst}.txt')

    matrix = np.loadtxt(file_path)
    matrix_shape = np.shape(matrix)

    if len(matrix_shape) == 1:
        return matrix, (matrix_shape[0], 0)

    return matrix, matrix_shape


if __name__ == '__main__':
    print(read_instance('exemplo'))
