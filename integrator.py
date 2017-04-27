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

                print ('rom {}:{} = {}'.format(i, j, rom))
                results[i][j] = rom

    return results


#===================================#
#       Adaptive Trapezoid          #
#===================================#

def adaptive_trap(function, )

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
#       Composite Midpoint          #
#===================================#

#===================================#
#               Utility             #
#===================================#

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





