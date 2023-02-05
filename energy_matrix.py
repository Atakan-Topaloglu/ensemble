from typing import List, Set, Dict, Optional, TypeVar
import numpy as np


def energy_matrix(matrix: list) -> list:
    """Creates the energy matrix of the input matrix.
    Energy matrix is calculated by adding the corresponding cell's value on the input matrix
    to the minimum of the three cells below given in the energy matrix."""

    energy_matrix_y, energy_matrix_x = matrix.shape
    energy_matrix_y, energy_matrix_x = int(energy_matrix_y), int(energy_matrix_x)
    energy_matrix = np.zeros((energy_matrix_y, energy_matrix_x))
    energy_matrix[-1:] = matrix[-1:]

    for row in range(energy_matrix_y-2,-1,-1):
        for col in range(energy_matrix_x):
            if col == 0:
                energy_matrix[row, col] += matrix[row, col] + min(energy_matrix[row+1, col], energy_matrix[row+1, col+1])
            elif col == energy_matrix_x-1:
                energy_matrix[row, col] += matrix[row, col] + min(energy_matrix[row+1, col], energy_matrix[row+1, col-1], )
            else:
                energy_matrix[row, col] += matrix[row, col] + min(energy_matrix[row+1, col], energy_matrix[row+1, col-1], energy_matrix[row+1, col+1]) 
    return energy_matrix


def path_finder(energy_matrix, matrix) -> list:
    """ Finds the path through a matrix from the top row to the bottom row such that the sum of
    values through that path is the minimum sum possible, called energy minimizing matrix.
    The path from a cell are three cells directly below it. (down left, down, down right) """

    energy_matrix_y, energy_matrix_x = matrix.shape
    energy_matrix_y, energy_matrix_x = int(energy_matrix_y), int(energy_matrix_x)
    path_stack = []
    prev_col = int(np.where(energy_matrix[0] == min(energy_matrix[0]))[0])
    path_stack.append([prev_col])

    for row1 in range(1, energy_matrix_y):
        if prev_col == 0:
            new_col = int(np.where(energy_matrix[row1] == min(energy_matrix[row1,prev_col], energy_matrix[row1,prev_col+1]))[0])
        elif prev_col == energy_matrix_x-1:
            new_col = int(np.where(energy_matrix[row1] == min(energy_matrix[row1,prev_col-1], energy_matrix[row1,prev_col]))[0])
        else:
            new_col = int(np.where(energy_matrix[row1] == min(energy_matrix[row1,prev_col-1], energy_matrix[row1,prev_col], energy_matrix[row1,prev_col+1]))[0])
        path_stack.append([new_col])

        prev_col = new_col 

    path = [matrix[row, col_min][0] for row, col_min in enumerate(path_stack)]
    return path

