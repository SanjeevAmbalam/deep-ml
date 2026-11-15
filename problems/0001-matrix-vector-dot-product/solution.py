import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
        return -1
    else:
        col_cnt = len(a)
        row_cnt = len(a[0])
        ans = np.zeros(col_cnt)
        for col in range(col_cnt):
            for row in range(row_cnt):
                ans[col] += a[col][row] * b[row]
        return ans
