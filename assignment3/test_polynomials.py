import numpy as np
from polynomials import Polynomial

def test_evaluation():
	p = Polynomial([3,2,2]) # 2x**2 + 2x + 3
	assert p(3) == 27
	assert p(7) == 115
	assert p(209) == 87783

def test_adding():
	p1 = Polynomial([3,2,4,1]) # x**3 + 4*x**2 + 2*x + 3
	p2 = Polynomial([7,2,3]) # 3*x**2 + 2*x + 7
	assert p1 + p2 == Polynomial([10,4,7,1])

def test_subtracting():
	p1 = Polynomial([7,4,5,6]) # 6*x**3 + 5*x**2 + 4*x + 7
	p2 = Polynomial([2,2,3,2]) # 2*x**3 + 3*x**2 + 2*x + 2
	assert p1 - p2 == Polynomial([5,2,2,4])

def test_degree():
	p1 = Polynomial([2,2,2,4]) # 4*x**3 + 2*x**2 + 2*x + 2
	p2 = Polynomial([1,0,2,4]) # 4*x**3 + 2*x**2 + 0*x + 1
	p3 = Polynomial([1,2,0,0,0]) # 0*x**4 + 0*x**3 + 0*x**2 + 2*x + 1
	p4 = Polynomial([0,0,0,0])
	assert p1.degree() == 3
	assert p2.degree() == 3
	assert p3.degree() == 1
	assert p4.degree() == -1

def test_multiplication():
	p1 = Polynomial([2,2,2,4])
	p2 = Polynomial([1,2,0,0,0])
	assert p1 * 2 == Polynomial([4,4,4,8])
	assert p2 * 5 == Polynomial([5,10,0,0,0])

def test_repr():
	p1 = Polynomial([2,2,2,4])
	p2 = Polynomial([1,2,0,0,0])
	assert p1 == '2 + 2x + 2x^2 + 4x^3'
	assert p2 == '1 + 2x'


test_evaluation()
test_adding()
test_subtracting()
test_degree()
test_multiplication()
test_repr()