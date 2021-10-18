# Function that compute the first phase of the algorithm -
# gets two integer matrices and their size, and the delta to divide them
# returns the evaluated matrix C

import numpy as np
from min_plus_opt import min_plus_product_opt
from matrix_generate import matrix_generator_1


def phase1_opt(mat_a, mat_b, delta):
    size = len(mat_a[0])
    reduce_size = int(size / delta)

    # initializing the reduced matrices A' and B' and the matrix C' for the result
    reduced_mat_a = np.zeros((reduce_size, reduce_size), dtype=np.int16)
    for i in range(1, reduce_size + 1):
        for j in range(1, reduce_size + 1):
            reduced_mat_a[i - 1][j - 1] = mat_a[i * delta - 1][j * delta - 1]

    reduced_mat_b = np.zeros((reduce_size, reduce_size), dtype=np.int16)
    for i in range(1, reduce_size + 1):
        for j in range(1, reduce_size + 1):
            reduced_mat_b[i - 1][j - 1] = mat_b[i * delta - 1][j * delta - 1]

    # computing C' = A'* B'

    reduced_mat_c = min_plus_product_opt(reduced_mat_a, reduced_mat_b)

    # Creating the matrix C

    mat_c = np.zeros((size, size), dtype=np.int16)

    for i in range(reduce_size):
        for j in range(reduce_size):
            value = reduced_mat_c[i][j]
            for k in range(delta):
                for w in range(delta):
                    mat_c[i * delta + k][j * delta + w] = value

    return mat_c

"""
mat = np.empty((4, 4), dtype=np.int16)
for i in range(4):
    for j in range(4):
        mat[i][j] = j

print(mat)

phase = phase1_opt(mat, mat, 2)
print(phase)
"""
