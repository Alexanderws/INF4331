import integrator


def test_integral_of_constant_function():
	f = lambda x: 2

	for n in range(1,10):
		sum_of_integral = integrator.integrate(f, 0, 1, n, method="default", implementation="default")
		assert abs(sum_of_integral - 2) < 1E-10

def test_integral_of_linear_function():
	f = lambda x: 2*x

	for n in range(1,10):
		sum_of_integral = integrator.integrate(f, 0, 1, n, method="default", implementation="default")
		assert abs(sum_of_integral - 1) <= (float(1/n) + 0.00000000001)
		#Added small increment to prevent errors from floating point numbers

def test_integral_of_constant_function_numpy():
	f = lambda x: 2

	for n in range(1,10):
		sum_of_integral = integrator.integrate(f, 0, 1, n, method="default", implementation="numpy")
		assert abs(sum_of_integral - 2) < 1E-10

def test_integral_of_linear_function_numpy():
	f = lambda x: 2*x

	for n in range(1,10):
		sum_of_integral = integrator.integrate(f, 0, 1, n, method="default", implementation="numpy")
		assert abs(sum_of_integral - 1) <= (float(1/n) + 0.00000000001)
		#Added small increment to prevent errors from floating point numbers


test_integral_of_constant_function()
test_integral_of_linear_function()
test_integral_of_constant_function_numpy()
test_integral_of_linear_function_numpy()
