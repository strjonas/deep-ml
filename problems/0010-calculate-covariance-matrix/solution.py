def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n = len(vectors)
	m = len(vectors[0])
	cov = [[] for x in range(n)]
	means = [sum(feat)/len(feat) for feat in vectors]

	for i1 in range(n):
		for i2 in range(n): 
			summ = sum([(vectors[i1][it] - means[i1])*(vectors[i2][it]-means[i2]) for it in range(m)])
			cov[i1].append((1/(m-1))*summ)

	return cov