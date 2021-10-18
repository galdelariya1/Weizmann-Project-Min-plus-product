def phase3(mat_a, mat_b, mat_c, result_mat_c, check_mat_a, check_mat_b, delta, difference):
    size = len(result_mat_c[0])

    for i in range(delta - 1, size, delta):
        for j in range(delta - 1, size, delta):
            for k in range(delta - 1, size, delta):
                if -8 * delta * difference <= mat_a[i][k] + mat_b[k][j] - mat_c[i][j] <= 8 * delta * difference:
                    if check_mat_a[int((i + 1) / delta - 1)][int((k + 1) / delta - 1)] or check_mat_b[int((k + 1) / delta - 1)][int((j + 1) / delta - 1)]:
                        for x in range(1, delta):
                            for y in range(1, delta):
                                for z in range(1, delta):
                                    result_mat_c[i - x][j - y] = min(result_mat_c[i - x][j - y], mat_a[i-x][k-z] + mat_b[k-z][j-y])
