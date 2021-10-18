import numpy as np
from matrix_generate import matrix_generator_1
from min_plus import min_plus


def min_plus_product_opt(A,B):
    B = np.transpose(B)
    Y = np.zeros((len(B),len(A)))
    for i in range(len(B)):
         Y[i] = (A + B[i]).min(1)
    return np.transpose(Y)

"""
mat1 = matrix_generator_1(1000, 10, 10)
mat2 = matrix_generator_1(1000, 10, 10)


#res = [[0 for i in range(1000)] for j in range(1000)]
#min_plus(mat1, mat2, res)
#print(res)

res_opt = min_plus_product_opt(mat1, mat2)
print(res_opt)

"""