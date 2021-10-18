import numpy as np
from min_plus import min_plus
from matrix_generate import matrix_generator_1


def alternative(mat_a, mat_b, size, delta):
    if (size % delta) != 0:
        print("Wrong delta!")
        return -1

    reduce_size = int(size / delta)

    # initializing the matrix of multiplication matrices
    mat_mat = [[] for i in range(reduce_size ** 2)]

    for j in range(reduce_size):
        for i in range(reduce_size):
            for k in range(reduce_size):
                temp_out = [[0 for i in range(delta)] for j in range(delta)]
                slice_a = [mat_a[h][(k * delta):((k + 1) * delta)] for h in range((i * delta), ((i + 1) * delta))]
                slice_b = [mat_b[p][(j * delta):((j + 1) * delta)] for p in range((k * delta), ((k + 1) * delta))]
                min_plus(slice_a, slice_b, temp_out)

                mat_mat[j * reduce_size + i].append(temp_out)

    outcome = [[0 for i in range(size)] for j in range(size)]
    for i in range(reduce_size ** 2):
        matrices_arr = mat_mat[i]
        for k in range(delta):
            for h in range(delta):
                min_value = matrices_arr[0][k][h]
                for j in range(1, reduce_size):
                    if matrices_arr[j][k][h] < min_value:
                        min_value = matrices_arr[j][k][h]
                outcome[(i % reduce_size) * delta + k][(i // reduce_size) * delta + h] = min_value

    return outcome


"""
mat = matrix_generator_1(200, 50, 4)

out_1 = [[0 for i in range(200)] for j in range(200)]
min_plus(mat, mat, out_1)

out_2 = alternative(mat, mat, 200, 10)

print(out_1 == out_2)
"""
