import os
from typing import List


def output_results(results: List[str], fname: str):
    file_path = os.path.join(os.getcwd(), fname)

    with open(file_path, 'a+') as f:
        for result in results:
            f.write(result + '\n')


if __name__ == '__main__':
    output_results(['exemplo'], 'teste.csv')
