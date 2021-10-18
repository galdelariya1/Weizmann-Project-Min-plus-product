# The main function for the second phase of the algorithm.
# Gets all three matrices and the delta and the difference W, and the number ro of iteration.

import random
import math
import numpy as np
from phase1_opt import phase1_opt
from matrix_generate import matrix_generator_1
from min_plus_opt import min_plus_product_opt


def phase2_opt(mat_a, mat_b, mat_c, delta, difference, iteration_number):
    size = len(mat_a[0])
    reduce_size = int(size / delta)
    infinity = math.inf

    check_mat_a = [[True for i in range(reduce_size)] for j in range(reduce_size)]
    check_mat_b = [[True for i in range(reduce_size)] for j in range(reduce_size)]
    result_mat_c = np.full((size, size), infinity)

    # The main loop for Ro number of iteration
    for x in range(iteration_number):

        # temporary index i and j for the current iteration
        index_i = random.randrange(size)
        index_j = random.randrange(size)

        # temporary matrices for the current iteration
        temp_mat_a = np.zeros((size, size), dtype=np.float32)
        temp_mat_b = np.zeros((size, size), dtype=np.float32)

        for i in range(size):
            for k in range(size):
                temp_mat_a[i][k] = mat_a[i][k] + mat_b[k][index_j] - mat_c[i][index_j]
                if not (-48 * delta * difference <= temp_mat_a[i][k] <= 48 * delta * difference):
                    temp_mat_a[i][k] = infinity
                if (i + 1) % delta == 0 and (k + 1) % delta == 0:
                    if check_mat_a[int((i + 1) / delta - 1)][int((k + 1) / delta - 1)]:
                        if -44 * delta * difference <= temp_mat_a[i][k] <= 44 * delta * difference:
                            check_mat_a[int((i + 1) / delta - 1)][int((k + 1) / delta - 1)] = False

        for k in range(size):
            for j in range(size):
                temp_mat_b[k][j] = mat_b[k][j] - mat_b[k][index_j] + mat_c[index_i][index_j] - mat_c[index_i][j]
                if not (-48 * delta * difference <= temp_mat_b[k][j] <= 48 * delta * difference):
                    temp_mat_b[k][j] = infinity
                if (k + 1) % delta == 0 and (j + 1) % delta == 0:
                    if check_mat_b[int((k + 1) / delta - 1)][int((j + 1) / delta - 1)]:
                        if -44 * delta * difference <= temp_mat_b[k][j] <= 44 * delta * difference:
                            check_mat_b[int((k + 1) / delta - 1)][int((j + 1) / delta - 1)] = False

        # Temporary using the regular multiplication
        temp_mat_c = min_plus_product_opt(temp_mat_a, temp_mat_b)

        for i in range(size):
            for j in range(size):
                result_mat_c[i][j] = min(result_mat_c[i][j],
                                         temp_mat_c[i][j] + mat_c[i][index_j] - mat_c[index_i][index_j] +
                                         mat_c[index_i][j])

    return result_mat_c, check_mat_a, check_mat_b

"""
mat = matrix_generator_1(6, 0, 10)

print(mat)

phase = phase1_opt(mat, mat, 2)
print(phase)

result, check1, check2 = phase2_opt(mat, mat, phase, 2, 10, 4)
print(result)

"""