def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    row_cnt = len(a)
    col_cnt = len(a[0])

    ans = [[0 for _ in range(row_cnt)] for _ in range(col_cnt)]

    
    for row in range(row_cnt):
        for col in range(col_cnt):
            ans[col][row] = a[row][col]

    return ans
        
