import matrix_functional
import bfs

if __name__ == '__main__':
    matrix = matrix_functional.input_matrix(4)
    print(f'Total amount of islands: {bfs.find_island_amount(matrix)}')
