import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	m = np.asmatrix(matrix) 

	vals, vecs = np.linalg.eig(m)

	return [float(x) for x in vals]