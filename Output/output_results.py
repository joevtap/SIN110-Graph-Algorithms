import os
from typing import List


def output_results(results: List[str], fname: str):

    # Here I got the path of the destination file
    file_path = os.path.join(os.getcwd(), fname)

    # Open it in append mode
    with open(file_path, 'a+') as f:
        # Iterates over results list, appending each string to the file
        for result in results:
            f.write(result + '\n')


if __name__ == '__main__':
    output_results(['exemplo'], 'teste.csv')
