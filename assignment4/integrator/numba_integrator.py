import numpy as np
from numba import jit

def numba_integrate(f, a, b, n):
	f_jit = jit("f8(f8)", nopython=True)(f)
	@jit("f8(f8, f8, i8)", nopython=True)
	def sum(n, a, b):
   		sum_of_integral = 0
   		step_size = (b-a)/n
   		for x in range(1,n+1):
   			sum_of_integral += (f_jit(step_size * x)) * step_size
   		return sum_of_integral
	return sum(n, a, b)


def numba_midpoint_integrate(f, a, b, n):
	f_jit = jit("f8(f8)", nopython=True)(f)
	@jit("f8(f8, f8, i8)", nopython=True)
	def sum(n, a, b):
   		sum_of_integral = 0
   		step_size = (b-a)/n
   		mid_sted = step_size / 2
   		for x in range(1,n+1):
   			sum_of_integral += (f_jit(step_size * x - mid_sted)) * step_size
   		return sum_of_integral	
	return sum(n, a, b)