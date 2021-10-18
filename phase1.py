# Function that compute the first phase of the algorithm -
# gets two integer matrices and their size, and the delta to divide them
# returns the evaluated matrix C

from min_plus import min_plus
from matrix_generate import matrix_generator_1


def phase1(mat_a, mat_b, delta):

    size = len(mat_a[0])
    reduce_size = int(size / delta)

    # initializing the reduced matrices A' and B' and the matrix C' for the result
    reduced_mat_a = [[0 for i in range(reduce_size)] for j in range(reduce_size)]
    for i in range(1, reduce_size + 1):
        for j in range(1, reduce_size + 1):
            reduced_mat_a[i - 1][j - 1] = mat_a[i * delta - 1][j * delta - 1]


    reduced_mat_b = [[0 for i in range(reduce_size)] for j in range(reduce_size)]
    for i in range(1, reduce_size + 1):
        for j in range(1, reduce_size + 1):
            reduced_mat_b[i - 1][j - 1] = mat_b[i * delta - 1][j * delta - 1]

    reduced_mat_c = [[0 for i in range(reduce_size)] for j in range(reduce_size)]

    # computing C' = A'* B'

    min_plus(reduced_mat_a, reduced_mat_b, reduced_mat_c)

    # Creating the matrix C

    mat_c = [[0 for i in range(size)] for j in range(size)]

    for i in range(reduce_size):
        for j in range(reduce_size):
            value = reduced_mat_c[i][j]
            for k in range(delta):
                for w in range(delta):
                    mat_c[i * delta + k][j * delta + w] = value

    return mat_c

"""
mat = matrix_generator_1(100, 10)
print(mat)

phase = phase1(mat, mat, 1)
print(phase)

result = [[0 for i in range(100)] for j in range(100)]
min_plus(mat, mat, result)
print(result)

print(phase == result)

"""