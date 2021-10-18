##The complete algorithem


from phase1 import phase1
from phase2 import phase2
from phase3 import phase3
from matrix_generate import matrix_generator_1
from matrix_generate import matrix_generator_2
from min_plus import min_plus


def quick_min_plus(mat_a, mat_b, delta, difference, iteration_number):
    mat_c = phase1(mat_a, mat_b, delta)

    result_mat_c, check_mat_a, check_mat_b = phase2(mat_a, mat_b, mat_c, delta, difference, iteration_number)

    phase3(mat_a, mat_b, mat_c, result_mat_c, check_mat_a, check_mat_b, delta, difference)

    return result_mat_c

"""
test = matrix_generator_1(200, 10, 10)

reg = [[0 for i in range(200)] for j in range(200)]

min_plus(test, test, reg)

res = quick_min_plus(test, test, 20, 10, 10)

print(res == reg)

"""