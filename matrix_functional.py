def input_matrix(rows_number):
    matrix = []
    for _ in range(rows_number):
        matrix.append(input().split())
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
