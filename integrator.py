#===================================#
#   Numeric Integration Methods     #
#===================================#

#Originaly Written By Garrett Schwartz, 04-24-2017

import Tkinter
from math import *
import re
import parser
import numpy



#===================================#
#       Trapezoidal Method          #
#===================================#

#preforms trapezoid method on a function
def trapezoid_method(function_string, interval_start, interval_end, steps):

    step_size = (float(interval_end) - float(interval_start)) / float(steps)
    steps = numpy.arange(interval_start, interval_end, step_size)
    print(steps)
    py_steps = []

    #copy ndarray to list
    for elem in steps:
        py_steps.append(elem)

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

        side_1 = eval_function(function_string, point_1)
        side_2 = eval_function(function_string, point_2)

        area = trap_area(side_1, side_2, step_size)

        total_area += area

    return total_area
        
        
#===================================#
#       Simpson's Composite         #
#===================================#

def simpson_composite(func, start, end, n):

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

#referenced Source:
#http://www.math-cs.gordon.edu/courses/ma342/python/

def romberg(f, a, b, n):
    r = numpy.array([[0] * (n+1)] * (n+1), float)
    h = b - a
 
    #eval() speedup
    st = parser.expr(f)
    compiled = st.compile('<string>')
   
    #Get f(a)
    x = a
    f_a = eval(compiled)
 
    #Get f(b)
    x = b
    f_b = eval(compiled)
    r[0,0] = 0.5 * h * ( f_a + f_b )
    power_2 = 1                         #First power is 1 then 2, 4, 8
 
    for i in numpy.arange(1, n+1):
        h = 0.5 * h
        sum_total = 0.0
        power_2 *= 2        
        for k in numpy.arange(1, power_2, 2):
            x = (a+k*h)
            sum_total = sum_total + eval(compiled)
 
        r[i, 0] = 0.5 * r[i-1, 0] + sum_total * h
 
        power_4 = 1
        for j in numpy.arange(1, i + 1):
            power_4 *= 4
            r[i,j] = r[i, j-1] + ( r[i,j-1] - r[i-1, j-1]) / (power_4 - 1)
    return r


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


#===================================#
#               Utility             #
#===================================#
         
#Takes a string, representing a mathematical function in python
#syntax (with variable x), and a value to evaluate it at.
#Returns the f(val)
def eval_function(string, val):

    if 'x' not in string:
        e = 'Independant Variable x not found in provided function.'
        raise Exception(e)

    x = val

    pycode = parser.expr(string).compile()
    result = eval(pycode)
    result = float(result)

    if type(result) != type(0.0):
        e = 'Invalid Function: Final type is not float: {} {}'.format(type(result), result)
        raise Exception(e)

    return result

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
 
def test_composite():
    #'''Simpson 4 a.
    f = "e**(x**2)"
    a = 0
    b = 1
    m = 16
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    #'''Simpson 4 a.
    f = "e**(x**2)"
    a = 0
    b = 1
    m = 32
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    print()
 
    #'''Simpson 4 b.
    f = "sin(x**2)"
    a = 0
    b = numpy.sqrt(numpy.pi)
    m = 16
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    #'''Simpson 4 b.
    f = "sin(x**2)"
    a = 0
    b = numpy.sqrt(numpy.pi)
    m = 32
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    print()
 
    #'''Simpson 4 c.
    f = "e**(cos(x))"
    a = 0
    b = numpy.pi
    m = 16
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    #'''Simpson 4 c.
    f = "e**(cos(x))"
    a = 0
    b = numpy.pi
    m = 32
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    print()
    #'''Simpson 4 e.
    f = "x/(2*(e**x)-e**(-x))"
    a = 0
    b = 1
    m = 16
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''
 
    #'''Simpson 4 e.
    f = "x/(2*(e**x)-e**(-x))"
    a = 0
    b = 1
    m = 32
    sum_total = composite_midpoint_rule(f, a, b, m)
    print ("Composite midpoint rule:",f, ":", sum_total, " with m value:", m)
    #'''    




#Returns the area of a trapezoid. Probably doesn't
#need to be it's own function, but its nice anyway
def trap_area(side_1, side_2, height):

    area = (side_1 + side_2) * 0.5 * height

    return area
