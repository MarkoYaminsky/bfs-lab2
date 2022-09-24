from matrix_functional import print_matrix

def fill_adjucent_squares(matrix, row_start, column_start, filler):
    starting_vertex_value = matrix[row_start][column_start]
    verexes_to_visit = [(row_start, column_start)]
    visited_vertexes = set()

    while len(verexes_to_visit) > 0:
        current_vertex_row, current_vertex_column = verexes_to_visit.pop(0)
        visited_vertexes.add((current_vertex_row, current_vertex_column))
        matrix[current_vertex_row][current_vertex_column] = filler

        for row, column in get_neighbours(matrix, current_vertex_row, current_vertex_column, starting_vertex_value):
            if (row, column) not in visited_vertexes:
                verexes_to_visit.append((row, column))

    return matrix


def get_neighbours(matrix, row, column, start):
    potential_neighbours = []
    neighbours = []

    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if i >= 0 and j >= 0:
                potential_neighbours.append((i, j))

    for i, j in potential_neighbours:
        if i < len(matrix) and j < len(matrix[i]):
            if matrix[i][j] == start and (i, j) != (row, column):
                neighbours.append((i, j))

    return neighbours


def find_island_amount(matrix):
    island_index = 0
    visited_islands = set()

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            vertex = matrix[row][column]
            if vertex not in visited_islands and vertex != '0':
                island_index += 1
                visited_islands.add(island_index)
                fill_adjucent_squares(matrix, row, column, island_index)

    print()
    print_matrix(matrix)
    print()
    return island_index
