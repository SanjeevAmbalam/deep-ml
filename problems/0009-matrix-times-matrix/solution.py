def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        return -1
    c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    rows_c = rows_a
    cols_c = cols_b

    for i in range(rows_c):
        for j in range(cols_c):
           c[i][j] = dot(a[i], col_vector(b, j))
	return c

def dot(m, n):
    s = 0
    for i in range(len(m)):
        s += m[i]*n[i]
    return s

def col_vector(matrix, col):
    s = []
    rows = len(matrix)
    for i in range(rows):
        s.append(matrix[i][col])
    return s

