import numpy as np


cpdef double cython_integrate(f, int a, int b, int n):
	cdef double sum_of_integral = 0
	cdef double b_a = (b-a)
	cdef double step_size = b_a / n
	for x in range(1,n+1):
		sum_of_integral += f(step_size * x) * step_size
	return sum_of_integral

cpdef double cython_midpoint_integrate(f, int a, int b, int n):
	cdef double sum_of_integral = 0
	cdef double b_a = (b-a)
	cdef double step_size = b_a / n
	cdef double mid_step = step_size / 2
	for x in range(1,n+1):
		sum_of_integral += f(step_size * x - mid_step) * step_size
	return sum_of_integral