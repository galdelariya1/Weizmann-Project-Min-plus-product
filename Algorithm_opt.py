#The complete algorithem with optimum use of Numpy

import numpy as np
from phase1_opt import phase1_opt
from phase2_opt import phase2_opt
from phase3 import phase3
from Algorithm import quick_min_plus
from matrix_generate import matrix_generator_1
from matrix_generate import matrix_generator_2
from min_plus_opt import min_plus_product_opt


def quick_min_plus_opt(mat_a, mat_b, delta, difference, iteration_number):
    mat_c = phase1_opt(mat_a, mat_b, delta)

    result_mat_c, check_mat_a, check_mat_b = phase2_opt(mat_a, mat_b, mat_c, delta, difference, iteration_number)

    phase3(mat_a, mat_b, mat_c, result_mat_c, check_mat_a, check_mat_b, delta, difference)

    return result_mat_c

"""
mat = matrix_generator_1(1000, 5, 10)

# res = quick_min_plus(mat, mat, 2, 10, 5)
# print(res)
res = min_plus_product_opt(mat, mat)

# res_opt = quick_min_plus_opt(mat, mat, 100, 10, 5)

print(res)
"""