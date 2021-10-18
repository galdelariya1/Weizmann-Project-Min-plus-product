import random
import numpy as np


def matrix_generator_1(size, start, difference):
    test_mat = [[start for i in range(size)] for j in range(size)]

    row_big = 0
    column_big = 0

    for i in range(1, size):
        if test_mat[0][i - 1] < (difference // 2):
            test_mat[0][i] = test_mat[0][i - 1] + random.randrange(difference)
        else:
            test_mat[0][i] = test_mat[0][i - 1] + random.randrange(-1 * (difference // 2), difference)
    for i in range(size):
        if test_mat[0][i] > row_big:
            row_big = test_mat[0][i]

    for j in range(1, size):
        if test_mat[j - 1][0] < (difference // 2):
            test_mat[j][0] = test_mat[j - 1][0] + random.randrange(difference)
        else:
            test_mat[j][0] = test_mat[j - 1][0] + random.randrange(-1 * (difference // 2), difference)

    for i in range(size):
        if test_mat[i][0] > column_big:
            column_big = test_mat[i][0]

    for i in range(1, size):
        for j in range(1, size):
            min_num = max(test_mat[i - 1][j] - difference, test_mat[i][j - 1] - difference, 0)
            max_num = min(test_mat[i - 1][j] + difference, test_mat[i][j - 1] + difference)
            test_mat[i][j] = random.randrange(min_num, max_num + difference)

    """
    big = 0
    small = 0

    for i in range(size):
        for j in range(size):
            if test_mat[i][j] < small:
                small = test_mat[i][j]
            if test_mat[i][j] > big:
                big = test_mat[i][j]

    print(row_big)
    print(column_big)
    print(big)
    print(small)
    """

    numpy_test_mat = np.array(test_mat, dtype= np.int64)

    return numpy_test_mat


def matrix_generator_2(size, start, difference):
    test_mat = [[start for i in range(size)] for j in range(size)]

    row_big = 0

    for i in range(1, size):
        if test_mat[0][i - 1] < (difference // 2):
            test_mat[0][i] = test_mat[0][i - 1] + random.randrange(difference)
        else:
            test_mat[0][i] = test_mat[0][i - 1] + random.randrange(-1 * (difference // 2), difference)

    for i in range(size):
        if test_mat[0][i] > row_big:
            row_big = test_mat[0][i]

    for i in range(1, size):
        num = random.randrange(difference)
        for j in range(size):
            test_mat[i][j] = test_mat[i - 1][j] + num

    for i in range(1, size, (size // int(size ** 0.5))):
        for j in range(1, size, (size // int(size ** 0.5))):
            min_num = max(test_mat[i - 1][j] - difference, test_mat[i][j - 1] - difference,
                          test_mat[i + 1][j] - difference, test_mat[i][j + 1] - difference, 0)
            max_num = min(test_mat[i - 1][j] + difference, test_mat[i][j - 1] + difference,
                          test_mat[i + 1][j] + difference, test_mat[i][j + 1] + difference)
            test_mat[i][j] = random.randrange(max(min_num - difference, 0), max_num + difference)

    """"
    big = 0
    small = 0
    is_good = True
    index_i = 0
    index_j = 0

    for i in range(size):
        for j in range(size):
            if test_mat[i][j] < small:
                small = test_mat[i][j]
            if test_mat[i][j] > big:
                big = test_mat[i][j]
            if i > 0 and j > 0:
                if not (-2 * difference <= test_mat[i][j] - test_mat[i - 1][j] <= difference * 2) or not (
                        -2 * difference <= test_mat[i][j] - test_mat[i][j - 1] <= difference * 2):
                    is_good = False
                    (index_i, index_j) = (i, j)
    print(row_big)
    print(big)
    print(small)
    print(is_good)
    print(index_i)
    print(index_j)
    """

    return test_mat

