import numpy as np
import sys
from polynomials import Polynomial



print (4*int(sys.argv[1])**4 + 3*int(sys.argv[1])**2 + 1)

p1 = Polynomial([2,2,2,4])
p2 = Polynomial([1,2,0,0,0])

p3 = Polynomial([1,2,3])
print(str(p1.coefficients()))
print(p1)
print(str(p2.coefficients()))
print(p2)
