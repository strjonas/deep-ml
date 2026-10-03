import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	m = np.array(matrix)

	return np.mean(m, axis=0 if mode=='column' else 1)