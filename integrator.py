#===================================#
#   Numeric Integration Methods     #
#===================================#

#Originaly Written By Garrett Schwartz, 04-24-2017

from math import *
import re
import parser
import numpy
import compiler #For gaussian



#===================================#
#       Trapezoidal Method          #
#===================================#

#preforms trapezoid method on a function
def trapezoid_method(function_string, interval_start, interval_end, steps):

    function = comp_func(function_string)

    step_size = (float(interval_end) - float(interval_start)) / float(steps)
    steps = numpy.arange(interval_start, interval_end, step_size)
    py_steps = []

    #copy ndarray to list
    for elem in steps:
        py_steps.append(elem)

    #Sometimes numpy allows the end of the range on the list
    if py_steps[-1] == interval_end:
        py_steps.pop()

    #Calculate the integral
    total_area = 0
        
    for elem in py_steps:
        #Check for last value of list.
        #If true, use point 2 as interval end
        if elem == py_steps[-1]:
            point_1 = elem
            point_2 = interval_end

        else:
            point_1 = elem
            point_2 = py_steps[py_steps.index(elem) + 1]

        side_1 = eval_function(function, point_1)
        side_2 = eval_function(function, point_2)

        area = trap_area(side_1, side_2, step_size)

        total_area += area

    return total_area
        
        
#===================================#
#       Simpson's Composite         #
#===================================#

def simpson_composite(function, start, end, n):

    func = comp_func(function)

    step_size = (float(end) - float(start)) / float(n)

    k = eval_function(func, start) + eval_function(func, end)

    for i in range(1, n, 2):
        k += 4 * eval_function(func, (start + (i * step_size)))

    for i in range(2, n-1, 2):
        k += 2 * eval_function(func, (start + (i * step_size)))

    result = (k * step_size) / 3

    return result
    


#===================================#
#               Romberg             #
#===================================#

def romberg(function, start, end, n, m):

    if n < 0 or m < 0:
        e = 'n or m must be greater or equal to 0'
        raise Exception(e)

    if m > n:
        e = 'm must be less than or equal to n'
        raise Exception(e)

    #Pre-compiling the function results in higher run times.
    func = comp_func(function)

    

    #Romberg's could be written recursively,
    #but python has some limited recursion support,
    #as its not considered pythonic. To that end,
    #an iterative method should be less memory intensive.
    #Plus its a bit of fun to come up with an iterative method.

    #build matrix for results
    results =[]

    for i in range(0, n + 1):
        results.append([])

        for j in range(0, m+1):
            results[i].append(float('nan'))

    for i in range(0, n+1):
        for j in range(0, m+1):

            if j <= i:

                h = (float(end) - float(start))/(2**i)

                if i == 0 and j == 0:
                    rom = h * (eval_function(func, start) + eval_function(func, end))

                elif i > 0 and j == 0:
                    summation = 0.0
                    for k in range (1, ((i*2) - 1)):
                        summation += eval_function(func, (start + ((2 * k - 1) * h)))
                    rom = (0.5 * results[(i - 1)][0]) + (h * summation)
                    

                elif i > 0 and j > 0:
                    rom = (1 / ((4 ** float(j)) - 1)) * (((4**j) * results[i][(j-1)]) - results[(i - 1)][(j-1)])

                #check_str = str(len(results)) + ':' + str(i) + '@' + str(len(results[0])) + ':' + str(j)
                #print(check_str)
                results[i][j] = rom

    return results


#===================================#
#       Adaptive Trapezoid          #
#===================================#

#References matlab code in Numerical Analysis textbook, page 271

def adaptive_trap(function, start, end, tolerance):

    #compile speedup + input check
    func = comp_func(function)
    
    n = 0
    app = []
    app.append(trap(func, start, end))

    a = []
    b = []

    tol = []
    tol.append(tolerance)

    a.append(float(start))
    b.append(float(end))

    result = 0.0
    
    while n >= 0:

        c = (a[n] + b[n]) / float(2)
        old_app = app[n]

        if len(app) <= n:
            app.append(float('nan'))

        app[n] = trap(func, a[n], c)

        if len(app) <= n + 1:
            app.append(float('nan'))

        app[n+1] = trap(func, c, b[n])
        

        if abs(old_app - (app[n] + app[n+1])) < 3*tol[n]:
            
            result += app[n] + app[n+1]
            n = n-1
        else:
            if len(b) <= n:
                b.append(float('nan'))

            if len(a) <= n:
                a.append(float('nan'))

            if len(b) <= n+1:
                b.append(float('nan'))

            if len(a) <= n+1:
                a.append(float('nan'))

            b[n+1] = b[n]
            b[n] = c
            a[n+1] = c

            tol[n] = tol[n] / float(2)

            if len(tol) <= n+1:
                tol.append(float('nan'))

            tol[n+1] = tol[n]

            n += 1

    return result

        
        
        

#===================================#
#           Adaptive Simpson        #
#===================================#

def adaptive_simpson (f, a, b, tolerance):
    tolerance_factor  = 10.0
 
    h = 0.5 * (b - a)
 
    x_0 = a
    x_1 = a + 0.5 * h
    x_2 = a + h
    x_3 = a + 1.5 * h
    x_4 = b
 
    #eval() speedup
    st = parser.expr(f)
    compiled = st.compile('<string>')
 
    x = x_0
    f_0 = eval(compiled)
 
    x = x_1
    f_1 = eval(compiled)
 
    x = x_2
    f_2 = eval(compiled)
 
    x = x_3
    f_3 = eval(compiled)
 
    x = x_4
    f_4 = eval(compiled)
 
   
    s_0 = h * (f_0 + 4.0 * f_2 + f_4) / 3
    s_1 = h * (f_0 + 4.0 * f_1 + 2.0 * f_2 + 4.0 * f_3 + f_4) / 6.0
 
    if abs(s_0 - s_1) >= tolerance_factor * tolerance:
        s = adaptive_simpson(f, x_0, x_2, 0.5 * tolerance) + adaptive_simpson(f, x_2, x_4, 0.5 * tolerance)
    else:
        s = s_1 + ( s_1 - s_0 ) / 15.0
    return s
 

#===================================#
#       Composite Midpoint          #
#===================================#
        
def composite_midpoint_rule(f, a, b, m):
    #eval() speedup
    st = parser.expr(f)
    compiled = st.compile('<string>')
   
    sum_total = 0
 
    h = (b - a) / m
    x = h / 2
    for i in numpy.arange(0, m):
        sum_total += eval(compiled) * h
        x += h
    return sum_total


#===================================#
#       Gaussian Quadrature         #
#===================================#

#references https://rosettacode.org/wiki/Numerical_integration/Gauss-Legendre_Quadrature#Python

def gaussian_quadrature(function, polyorder, a, b):
    func_string = 'def temp_func(x):\n\treturn ' + function
    h = parser.suite(func_string).compile()
    exec(h)
    

    [Ws, xs, err] = GaussLegendreWeights(polyorder)

    if err == 0:
        ans = (b-a) * 0.5 * sum(Ws * temp_func((b-a)*0.5*xs + (b+a)*0.5))

    else:
        err = 1
        ans = None
    return [ans, err]

#===================================#
#       Gaussian Utilities          #
#===================================#

def legendre(n, x):

    x = numpy.array(x)

    if n == 0:
        return x*0+1.0 #addition of x*0 is most likely for correct datatype
    elif n == 1:
        return x
    else:
        return ((2.0 * n - 1.0) * x * legendre(n-1, x) - (n-1) * legendre(n-2, x))/n

def dlegendre(n, x):

    x = numpy.array(x)
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

        roots = numpy.array(roots)
        if polyorder%2 == 0:
            roots = numpy.concatenate((-1.0*roots, roots[::-1]))
        else:
            roots = numpy.concatenate((-1.0*roots, [0.0], roots[::-1]))
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
            


#===================================#
#               Utility             #
#===================================#

def trap(compiled_function, a, b):
    floata = float(a)
    floatb = float(b)
    return trap_area(eval_function(compiled_function, a), eval_function(compiled_function, b), (floatb - floata))

#NOTE: Rewrite to move compilation out of function
         
#Takes a string, representing a mathematical function in python
#syntax (with variable x), and a value to evaluate it at.
#Returns the f(val)
def eval_function(compiled_string, val):

    x = float(val)

    result = eval(compiled_string)
    result = float(result)

    if type(result) != type(0.0):
        e = 'Invalid Function: Final type is not float: {} {}'.format(type(result), result)
        raise Exception(e)

    return result

#Returns a compiled function, but raises exceptions
#if the statement is incorrect
def comp_func(string):

    if 'x' not in string:
        e = 'Independant Variable x not found in provided function.'
        raise Exception(e)

    pycode = parser.expr(string).compile()

    return pycode

#Returns the area of a trapezoid. Probably doesn't
#need to be it's own function, but its nice anyway
def trap_area(side_1, side_2, height):

    area = (side_1 + side_2) * 0.5 * height

    return area





