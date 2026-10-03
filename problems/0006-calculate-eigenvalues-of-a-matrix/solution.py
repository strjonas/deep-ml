import numpy as np
import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	#m = np.asmatrix(matrix) 
	#vals, vecs = np.linalg.eig(m)

	a, c = matrix[0]
	b, d = matrix[1]

	tr = a + d
	det = a*d-(b*c)

	descr = math.sqrt(tr**2-(4*det))

	e1 = (tr+descr)/2
	e2 = (tr-descr)/2
	
	return [e1, e2]