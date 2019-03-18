import integrator
import math

# Pure Python implementation
def python_midpoint():
	difference = 1
	n = 90600
	f = lambda x: math.sin(x)
	while (difference > 1E-10):
		n += 1
		sum_of_integral = integrator.integrate(f, 0, math.pi, n, method="midpoint", implementation="default")
		difference = abs(2 - sum_of_integral)
		print(n)
	print('Python - sum = {}  difference = {}  N = {}'.format(sum_of_integral, difference, n))

# Numpy implementation
def numpy_midpoint():
	difference = 1
	n = 90600
	f = lambda x: math.sin(x)
	while (difference > 1E-10):
		n += 1
		sum_of_integral = integrator.integrate(f, 0, math.pi, n, method="midpoint", implementation="numpy")
		difference = abs(2 - sum_of_integral)
		print(n)
	print('Numpy - sum = {}  difference = {}  N = {}'.format(sum_of_integral, difference, n))

# Numba implementation
def numba_midpoint():
	difference = 1
	n = 90600
	f = lambda x: math.sin(x)
	while (difference > 1E-10):
		n += 1
		sum_of_integral = integrator.integrate(f, 0, math.pi, n, method="midpoint", implementation="numpy")
		difference = abs(2 - sum_of_integral)
		print(n)
	print('Numba - sum = {}  difference = {}  N = {}'.format(sum_of_integral, difference, n))

# Cython implementation
def cython_midpoint():
	difference = 1
	n = 90600
	f = lambda x: math.sin(x)
	while (difference > 1E-10):
		n += 1
		sum_of_integral = integrator.integrate(f, 0, math.pi, n, method="midpoint", implementation="numpy")
		difference = abs(2 - sum_of_integral)
		print(n)
	print('Cython - sum = {}  difference = {}  N = {}'.format(sum_of_integral, difference, n))


if __name__ == '__main__':
	python_midpoint()
	numpy_midpoint()
	numba_midpoint()
	cython_midpoint()