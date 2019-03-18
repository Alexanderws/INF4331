class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with 
        the i-th element being the coefficient a_i."""
        self.c = coefficients

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""
        for i in range (len(self.c)-1,-1,-1):
            if self.c[i]>0:
                return i
        return -1

    def coefficients(self):
        """Return the list of coefficients. 

        The i-th element of the list should be a_i, meaning that the last 
        element of thselfe list is the coefficient of the highest degree term."""
        return self.c


    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""
        total_sum = self.c[0]
        for i in range(1,len(self.c)):
            total_sum += self.c[i]*x**i
        return total_sum
    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 
        
        If p is not an int or Polynomial, should raise ArithmeticError."""
        if(isinstance(p, int)):
            new_c = self.coefficients()
            new_c[0] += p
            return Polynomial(new_c)

        shortest = self.coefficients()
        longest = p.coefficients()
        new_c = []
        if (len(longest) < len(shortest)):
            shortest = p.coefficients()
            longest = self.coefficients()

        for i in range(0,len(shortest)):
            new_c.append(longest[i] + shortest[i])
        for i in range(len(shortest),len(longest)):
            new_c.append(longest[i])
        return Polynomial(new_c)
        raise ArithmeticError
 
        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""
        if(isinstance(p, int)):
            new_c = self.coefficients()
            new_c[0] -= p
            return Polynomial(new_c)

        original = self.coefficients()
        other = p.coefficients()
        new_c = []
        if (len(original) < len(other)):
            for i in range(0,len(original)):
                new_c.append(original[i] - other[i])
            for i in range(len(original),len(other)):
                new_c.append(-other[i])
        else:
            for i in range(0,len(other)):
                new_c.append(original[i]-other[i])
            for i in range(len(other),len(original)):
                new_c.append(original[i])

        return Polynomial(new_c)
        raise ArithmeticError

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""
        if(isinstance(c, int)):
            new_c = []
            for i in range(0,len(self.coefficients())):
                new_c.append(c * self.coefficients()[i])
            return Polynomial(new_c)

        raise ArithmeticError


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""
        return self * c
    
    def __repr__(self):
        """Return a nice string representation of polynomial.
        
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        formatted = ''
        if self.coefficients()[0] != 0:
            formatted += str(self.coefficients()[0])
        if self.coefficients()[1] != 0:
            if self.coefficients()[1] == 1:
                formatted += (' + x')
            else:
                formatted += (' + ' + str(self.coefficients()[1]) + 'x')
        for i in range(2,len(self.coefficients())):
            if self.coefficients()[i] != 0:
                if self.coefficients()[i] == 1:
                    formatted += (' + x^' + str(i))
                else:
                    formatted += (' + ' + str(self.coefficients()[i]) + 'x^' + str(i))

        return formatted

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""
        if (len(self.coefficients()) == len(p.coefficients())):
            for i in range(0, len(self.coefficients())):
                if self.coefficients()[i] != p.coefficients()[i]:
                    return False
            return True 
        return False
        

def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    
    
    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))

    
    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )
    
    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
