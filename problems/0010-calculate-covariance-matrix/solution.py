import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	l = len(vectors)
	m = [[0 for _ in range(l)] for _ in range(l)]
	for row in range(l):
		for col in range(l):
			m[row][col] = cov(vectors[row], vectors[col])
	return m
def cov(x1, x2):
	x1_mean = np.mean(x1)
	x2_mean = np.mean(x2)
	s = 0
	for i in range(len(x1)):
		s += (x1[i]-x1_mean)* (x2[i]-x2_mean)
	return s/(len(x1)-1)
