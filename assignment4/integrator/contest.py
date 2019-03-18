import integrator
import math

# Contest
a = 1E-20
b = 1E7
n = 100000000


def function_1():
	f = lambda x: (1 / math.pi) * (math.sin(x) / x) * (math.sin(x/3) / (x/3)) * (math.sin(x/5) / (x/5))
	sum_of_integral = integrator.integrate(f, a, b, n, method="midpoint", implementation="numba")
	print('Function 1 - sum = {}  N = {}'.format(sum_of_integral, n))

def function_2():
	f = lambda x: (1 / math.pi) * (math.sin(x) / x) * (math.sin(x/3) / (x/3)) * (math.sin(x/5) / (x/5)) * (math.sin(x/7) / (x/7))
	sum_of_integral = integrator.integrate(f, a, b, n, method="midpoint", implementation="numba")
	print('Function 2 - sum = {}  N = {}'.format(sum_of_integral, n))

def function_3():
	f = lambda x: (1 / math.pi) * (math.sin(x) / x) * (math.sin(x/3) / (x/3)) * (math.sin(x/5) / (x/5)) * (math.sin(x/7) / (x/7)) * (math.sin(x/9) / (x/9)) * (math.sin(x/11) / (x/11))
	sum_of_integral = integrator.integrate(f, a, b, n, method="midpoint", implementation="numba")
	print('Function 3 - sum = {}  N = {}'.format(sum_of_integral, n))

def function_4():
	f = lambda x: (1 / math.pi) * (math.sin(x) / x) * (math.sin(x/3) / (x/3)) * (math.sin(x/5) / (x/5)) * (math.sin(x/7) / (x/7)) * (math.sin(x/9) / (x/9)) * (math.sin(x/11) / (x/11)) * (math.sin(x/13) / (x/13)) 
	sum_of_integral = integrator.integrate(f, a, b, n, method="midpoint", implementation="numba")
	print('Function 4 - sum = {}  N = {}'.format(sum_of_integral, n))

def function_5():
	f = lambda x: (1 / math.pi) * (math.sin(x) / x) * (math.sin(x/3) / (x/3)) * (math.sin(x/5) / (x/5)) * (math.sin(x/7) / (x/7)) * (math.sin(x/9) / (x/9)) * (math.sin(x/11) / (x/11)) * (math.sin(x/13) / (x/13)) * (math.sin(x/15) / (x/15)) 
	sum_of_integral = integrator.integrate(f, a, b, n, method="midpoint", implementation="numba")
	print('Function 5 - sum = {}  N = {}'.format(sum_of_integral, n))

def function_6():
	f = lambda x: (1 / math.pi) * (math.sin(x) / x) * (math.sin(x/4) / (x/4)) * (math.sin(x/4) / (x/4)) * (math.sin(x/7) / (x/7)) * (math.sin(x/7) / (x/7)) * (math.sin(x/9) / (x/9)) * (math.sin(x/9) / (x/9))
	sum_of_integral = integrator.integrate(f, a, b, n, method="midpoint", implementation="numba")
	print('Function 6 - sum = {}  N = {}'.format(sum_of_integral, n))


if __name__ == '__main__':
	function_1()
	function_2()
	function_3()
	function_4()
	function_5()
	function_6()