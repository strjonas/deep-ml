import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	val = 0
	scal = 1 / math.sqrt(math.pi * 2 * (std_dev**2))
	pot = math.exp(-((x - mean)**2) / (2*std_dev**2))
	val = scal * pot

	return round(val,5)