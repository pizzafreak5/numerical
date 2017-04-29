from numpy import *
import parser
import compiler

#===================================#
#       Gaussian Quadrature         #
#===================================#

#references https://rosettacode.org/wiki/Numerical_integration/Gauss-Legendre_Quadrature#Python

def gaussian_quadrature(function, a, b, polyorder):
    func_string = 'def temp_func(x):\n\treturn ' + function

    #input validation
    
    
    print (func_string)
    h = parser.suite(func_string).compile()
    exec(h)
    

    [Ws, xs, err] = GaussLegendreWeights(polyorder)

    if err == 0:
        ans = (b-a)*0.5*sum( Ws*temp_func( (b-a)*0.5*xs+ (b+a)*0.5 ) )

    else:
        err = 1
        ans = None
    return [ans, err]

def func(x):
    return exp(x)

#===================================#
#       Gaussian Utilities          #
#===================================#

def legendre(n, x):

    x = array(x)

    if n == 0:
        return x*0+1.0 #addition of x*0 is most likely for correct datatype
    elif n == 1:
        return x
    else:
        return ((2.0 * n - 1.0) * x * legendre(n-1, x) - (n-1) * legendre(n-2, x))/n

def dlegendre(n, x):

    x = array(x)
    if n == 0 :
        return x * 0
    elif n == 1:
        return x*0+1.0
    else:
        return (n / (x**2 - 1.0))*(x*legendre(n,x) - legendre(n-1, x))

def legendre_roots(polyorder, tolerance = 1e-20):
    if polyorder < 2:
        err = 1 #bad poly order

    else:
        roots = []

        for i in range(1, int(polyorder)/2 + 1):
            x = cos(pi * (i - 0.25)/(polyorder+0.5))
            error = 10 * tolerance
            iters = 0
            while error > tolerance and iters < 1000:
                dx = -legendre(polyorder, x) / dlegendre(polyorder, x)
                x = x+dx
                iters = iters + 1
                error = abs(dx)
            roots.append(x)

        roots = array(roots)
        if polyorder%2 == 0:
            roots = concatenate((-1.0*roots, roots[::-1]))
        else:
            roots = concatenate((-1.0*roots, [0.0], roots[::-1]))
        err = 0
    return [roots, err]

def GaussLegendreWeights(polyorder):
    w = []
    [xis, err] = legendre_roots(polyorder)
    if err == 0:
        w = 2.0/((1.0 - xis**2) * dlegendre(polyorder, xis)**2)
        err = 0
    else:
        err=1
    return [w, xis, err]
