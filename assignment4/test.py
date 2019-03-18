import numpy as np
import integrator
import time
from contextlib import contextmanager

@contextmanager
def timeit_context(name):
    startTime = time.time()
    yield
    elapsedTime = round((time.time()-startTime)*1000.0,3)
    print('[{}] finished in {} ms'.format(name, elapsedTime))


f1 = lambda x: 2*x

with timeit_context('Python implementation, midpoint method, n=100'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100, method="midpoint", implementation="default")

print(sum_of_integral1)

with timeit_context('Numpy implementation, midpoint method, n=100'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100, method="midpoint", implementation="numpy")

print(sum_of_integral1)

with timeit_context('Numba implementation, midpoint method, n=100'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100, method="midpoint", implementation="numba")

print(sum_of_integral1)

with timeit_context('Cython implementation, midpoint method, n=100'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100, method="midpoint", implementation="cython")

print(sum_of_integral1)

with timeit_context('Python implementation, default method, n=100000'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100000, method="default", implementation="default")

print(sum_of_integral1)

with timeit_context('Numpy implementation, default method, n=100000'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100000, method="default", implementation="numpy")

print(sum_of_integral1)

with timeit_context('Numba implementation, default method, n=100000'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100000, method="default", implementation="numba")

print(sum_of_integral1)

with timeit_context('Cython implementation, default method, n=100000'):
	sum_of_integral1 = integrator.integrate(f1, 0, 1, 100000, method="default", implementation="cython")

print(sum_of_integral1)