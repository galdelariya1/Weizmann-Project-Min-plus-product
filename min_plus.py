# Brute force function for computing the (min, +)-product of two matrices
# Accepts two matrices to multiply and third matrix for the result


def min_plus(mat_a, mat_b, mat_c):
    size = len(mat_a[0])

    for i in range(size):
        for j in range(size):
            min_value = mat_a[i][0] + mat_b[0][j]
            for k in range(1, size):
                current_value = mat_a[i][k] + mat_b[k][j]
                if current_value < min_value:
                    min_value = current_value

            mat_c[i][j] = min_value



