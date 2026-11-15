def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	return quadratic(1, -trace(matrix), det(matrix))

def trace(matrix):
	return matrix[0][0] + matrix[1][1]
def det(matrix):
	return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
def quadratic(a, b, c):
	if(b**2-4*a*c<0):
		return None
	else:
		x1 = (-b+(b**2-4*a*c)**0.5)/2*a
		x2 = (-b-(b**2-4*a*c)**0.5)/2*a
	return [x1, x2]

