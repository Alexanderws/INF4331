import numpy as np
import numpy_integrator
import numba_integrator
import cython_integrator
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f.__name__, 'function took',round((time2-time1)*1000.0,3), 'ms')
        return ret
    return wrap

def integrate(f, a, b, n, method="default", implementation="default"):
	sum_of_integral = 0
	if implementation == "default":
		if method == "default":
			sum_of_integral = integrate_default(f, a, b, n)
		elif method == "midpoint":
			sum_of_integral = midpoint_integrate(f, a, b, n)
	if implementation == "numpy":
		if method == "default":
			sum_of_integral = numpy_integrator.numpy_integrate(f, a, b, n)
		elif method == "midpoint":
			sum_of_integral = numpy_integrator.numpy_midpoint_integrate(f, a, b, n)
	if implementation == "numba":
		if method == "default":
			sum_of_integral = numba_integrator.numba_integrate(f, a, b, n)
		elif method == "midpoint":
			sum_of_integral = numba_integrator.numba_midpoint_integrate(f, a, b, n)
	if implementation == "cython":
		if method == "default":
			sum_of_integral = cython_integrator.cython_integrate(f, a, b, n)
		elif method == "midpoint":
			sum_of_integral = cython_integrator.cython_midpoint_integrate(f, a, b, n)
	return sum_of_integral


def integrate_default(f, a, b, n):
	sum_of_integral = 0
	step_size = (b-a)/n
	interval = []
	for i in range(n+1):
		interval.append(step_size*i+a)
	for x in range(1,n+1):
		sum_of_integral += (interval[x] - interval[x-1]) * f(interval[x])
	return sum_of_integral

def midpoint_integrate(f, a, b, n):
	sum_of_integral = 0
	step_size = (b-a)/n
	interval = []
	for i in range(n+1):
		interval.append(step_size*i+a)
	for x in range(1,n+1):
		midpoint = (interval[x] + interval[x-1])/2
		sum_of_integral += (interval[x] - interval[x-1]) * f(midpoint)
	return sum_of_integral

def plot_error(n):
	errors = []
	for i in range(1,n):
		errors.append(abs(integrate(f,0,1,i) - float(1/3)))
	plt.plot(range(len(errors)), errors)
	plt.xlabel('N value', fontsize=10)
	plt.ylabel('Error value', fontsize=10)
	plt.show()


if __name__ == '__main__':
	f1 = lambda x: 2*x
	sum_of_integral1 = integrate(f1, 0, 1, 200)
	print(sum_of_integral1)
