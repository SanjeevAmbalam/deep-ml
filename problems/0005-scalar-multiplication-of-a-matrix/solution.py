def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	rows = len(matrix)
    cols = len(matrix[0])
    result = [[scalar * matrix[row][col] for col in range(cols)] for row in range(rows)]
    
    return result