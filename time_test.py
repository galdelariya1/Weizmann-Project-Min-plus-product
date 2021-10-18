from min_plus import min_plus
from min_plus_opt import min_plus_product_opt
from Algorithm import quick_min_plus
from Algorithm_opt import quick_min_plus_opt
from matrix_generate import matrix_generator_1
from alternative import alternative
from timeit import default_timer as timer


def time_test(size, delta, start, difference, iteration_number):
    mat_a = matrix_generator_1(size, start, difference / 2)
    mat_b = matrix_generator_1(size, start, difference / 2)

    """
    reg_time = 0.0
    for j in range(3):
        res = [[0 for x in range(size)] for y in range(size)]
        start = timer()
        min_plus(mat_a, mat_b, res)
        end = timer()
        reg_time += (end - start)

    reg_time = reg_time / 3

    
    opt_time = 0.0
    for j in range(3):
        start = timer()
        opt_res = min_plus_product_opt(mat_a, mat_b)
        end = timer()
        opt_time += (end - start)

    opt_time = opt_time / 3

    """
    quick_reg_time = 0.0
    for j in range(3):
        start = timer()
        quick_res = quick_min_plus(mat_a, mat_b, delta, difference, iteration_number)
        end = timer()
        quick_reg_time += (end - start)

    quick_reg_time = quick_reg_time / 3

    """
    quick_opt_time = 0.0
    for j in range(3):
        start = timer()
        quick_opt_res = quick_min_plus_opt(mat_a, mat_b, delta, difference, iteration_number)
        end = timer()
        quick_opt_time += (end - start)

    quick_opt_time = quick_opt_time / 3
    """

    alter_time = 0.0
    for j in range(3):
        start = timer()
        alter_res = alternative(mat_a, mat_b, size, delta)
        end = timer()
        alter_time += (end - start)

    alter_time = alter_time / 3

    #print('naive brute force {}sec'.format(reg_time))
    #print('Numpy brute force {}sec'.format(opt_time))
    print('Regular Algorithm {}sec'.format(quick_reg_time))
    #print('Numpy Algorithm {}sec'.format(quick_opt_time))
    print('Alternative time {}sec'.format(alter_time))


print("2000")
time_test(2000, 40, 50, 4, 2)





















