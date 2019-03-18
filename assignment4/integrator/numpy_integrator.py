import numpy as np

def numpy_integrate(f, a, b, n):
	interval = np.linspace(a, b, n+1)
	sum_of_integral = 0
	for x in range(1,n+1):
		sum_of_integral += (interval[x] - interval[x-1]) * f(interval[x])
	return sum_of_integral

def numpy_midpoint_integrate(f, a, b, n):
	interval = np.linspace(a, b, n)
	sum_of_integral = 0
	for x in range(1,n+1):
		midpoint = (interval[x] + interval[x-1])/2
		sum_of_integral += (interval[x] - interval[x-1]) * f(midpoint)
	return sum_of_integral