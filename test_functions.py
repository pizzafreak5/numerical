import * from integrator

def test_adaptive_tolerance():
    #'''Simpson 7 a.
    f = "e**(x**2)"
    a = 0
    b = 1
    tolerance = 0.5 * 10**-8
    s = adaptive_simpson(f, a, b, tolerance)
    print ("adaptive simpson:",f, ":", s, " with tolerance value:", tolerance)
    #'''
 
    #'''Simpson 7 b.
    f = "sin(x**2)"
    a = 0
    b = numpy.sqrt(numpy.pi)
    tolerance = 0.5 * 10**-8
    s = adaptive_simpson(f, a, b, tolerance)
    print ("adaptive simpson:",f, ":", s, " with tolerance value:", tolerance)
    #'''
 
    #'''Simpson 7 c.
    f = "e**(cos(x))"
    a = 0
    b = numpy.pi
    tolerance = 0.5 * 10**-8
    s = adaptive_simpson(f, a, b, tolerance)
    print ("adaptive simpson:",f, ":", s, " with tolerance value:", tolerance)
    #'''
   
    #'''Simpson 7 e.
    f = "x/(2*(e**x)-(e**(-x)))"
    a = 0
    b = 1
    tolerance = 0.5 * 10**-8
    s = adaptive_simpson(f, a, b, tolerance)
    print ("adaptive simpson:",f, ":", s, " with tolerance value:", tolerance)
    #'''


def test_romberg():
    '''Romberg 1 a.
   f = "x/sqrt(x**2 + 9)"
   a = 0
   b = 4
   n = 20
   r = romberg(f, a, b, n)
   x, y = (r.shape)
 
   print ("function:",f)
   print ("romberg:",n, ":", r[x-1, y-1])
   #'''
 
    '''Romberg 1 b.
   f = "(x**3)/(x**2 + 1)"
   a = 0
   b = 1
   n = 20
   r = romberg(f, a, b, n)
   x, y = (r.shape)
 
   print ("function:",f)
   print ("romberg:",n, ":", r[x-1, y-1])
   #'''
 
    '''Romberg 1 c.
   f = "(x*e**x)"
   a = 0
   b = 1
   n = 20
   r = romberg(f, a, b, n)
   x, y = (r.shape)
 
   print ("function:",f)
   print ("romberg:",n, ":", r[x-1, y-1])
   #'''
 
    #''' Romberg 1 d.
    f = "(x**2)*log1p(x)"
    a = 1
    b = 3
    n = 20
    r = romberg(f, a, b, n)
    x, y = (r.shape)
    print ("function:",f)
    print ("romberg:",n, ":", r[x-1, y-1])
    #'''

