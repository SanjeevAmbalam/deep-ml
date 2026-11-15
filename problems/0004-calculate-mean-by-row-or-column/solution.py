def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode=='row':
        means = [0 for _ in range(len(matrix))]
        for r in range(len(matrix)):
            count = 0
            for c in range(len(matrix[0])):
                count += 1
                means[r] += matrix[r][c]
            means[r] /= count
    elif mode == 'column':
        means = [0 for _ in range(len(matrix[0]))]
        for c in range(len(matrix[0])):
            count = 0
            for r in range(len(matrix)):
                count += 1
                means[c] += matrix[r][c]
            means[c] /= count
    return means