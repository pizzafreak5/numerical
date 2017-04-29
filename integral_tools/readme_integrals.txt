---INTEGRATION METHODS---

This tool contains solvers for the:

Trapezoid Method
Simpson's Composite Method
Romberg Method
Adaptive Trapezoid Quadrature
Adaptive Simpson Quadrature
Composite Midpoint Method
Guassian Adaptive Quadrature


---INSTALLATION---

Please note that python must be installed on your system to use this tool.
Additionaly, this tool require the following 3rd party libraries:

numpy

On Windows, it is not nessisarily required that Python is added to your path, but reccoomended.
On Linux, python should already be added to your path
On Mac, ensure that /usr/local/bin is on your shell search path

Note that this program was written for Python 2,
however, if may work and may work better with Python 3

---START UP---

To use this tool, follow the steps for your specific Operating System:

Windows:

If python is in your path enviroment variable, open a terminal in the tool directory
by pressing SHIFT + Right-Click, and from the dropdown select 'Open command window here'

Now into the consol, type
python gooey.py

Alternatively, if you have IDLE installed, simply right click the gooey.py script and select
'Edit with IDLE'. From there, select Run -> Run Module or press the F5 key

Linux:

In terminal, navigate to the directory of the tool. From there, run: 

# python gooey.py

Alternatively, from any directory, run:

# python [full path to tool directory from root]

Mac:
From Finder, drag the gooey.py script to your PythonLauncher. This may not work, as this tool uses a GUI

Alternatively, from terminal, run 

python gooey.py

Or

pythonw gooey.py

The w indicates that a gui is nessisary.

Is this still won't run:

¯\_( '-')_/¯

Alternatively, purchase a real computer, and attempt to run the script on that :D
(jk)

---USAGE---

GENERAL:

	-Formulas
		Formulas follow a specific syntax.

		First of all, DO NOT type the 'f(x) =' portion of a function,
		only the right-hand side.

		Second, the independant variable MUST be 'x'

		Do not surround the function in quotes of any kind.

		Operators:

		+		:		plus
		-		:		minus
		*		:		multiply
		/		:		divide
		**	:		exponent
		
		Please note that if any operators are missing, the syntax and usage of expressions
		is exactly python syntax. You may use any python reference.
		
		Functions:
		
		exp(a)		:		e^a
		log(a)		:		ln(a)
		log(a, 10)	:		log10(a)	#This goes for any base
		sqrt(a)		:		Equivalent to a ** 0.5
		acos(a)	:		Arc cosine
		asin(a)		:		Arc sine
		atan(a)	:		Arc tangent
		cos(a)		:		cosine
		sin(a)		:		sine
		tan(a)		:		Tangent
		
		Constants:
		pi				:		3.1415......
		e				:		2 something something. 17 I think
		
		Please note that if you are dividing by integers and using Python 2, i.e. x/2, please use
		x / 2.0, as, due to the nature of python 2, unexepected behavior can occur with the former
		
METHODS:

	1.Trapezoid Method
	
		This function takes 4 arguments:
			Function 		- the mathematical function in terms of x
			Start			- The lower bound of the integral
			End				-The upper bound of the integral
			Steps			-The number of divisions, or 'panels' #Must be an integer
			
	2.Simpson's Composite Method
		
		This function takes 4 arguments:
			Function 		- the mathematical function in terms of x
			Start			- The lower bound of the integral
			End				-The upper bound of the integral
			N					-The number of sub-intervals. Must be even
			
	3.Romberg Method
		This function takes 5 arguments:
			Function 		- the mathematical function in terms of x
			Start			- The lower bound of the integral
			End				-The upper bound of the integral
			N					-The number of rows. This is a non-negative integer
			M					-The number of colums. This should be equal to N, and cannot be less. This is also a non-negative integer
			
	4.Adaptive Trapezoid Quadrature
		This function takes 4 arguments:
			Function 		- the mathematical function in terms of x
			Start			- The lower bound of the integral
			End				-The upper bound of the integral
			Tolerance		-The degree of precision wanted. A tolerance of 0.01 will result in an answer within 0.01 of the integral.
			
		
		5.Adaptive Simpson Quadrature
			This function takes 4 arguments:
				Function 		- the mathematical function in terms of x
				Start			- The lower bound of the integral
				End				-The upper bound of the integral
				Tolerance		-The degree of precision wanted. A tolerance of 0.01 will result in an answer within 0.01 of the integral.

		6.Composite Midpoint Method
			This function takes 4 arguments:
				Function 		- the mathematical function in terms of x
				Start			- The lower bound of the integral
				End				-The upper bound of the integral
				M					-The number of rectangles
			
		7.Guassian Adaptive Quadrature
			This function takes 4 arguments:
				Function 		- the mathematical function in terms of x
				Start			- The lower bound of the integral
				End				-The upper bound of the integral
				Order			-The number of rectangles

---HELP---

Please send concerns or questions regarding functionality, hatemail, and credit-card offers to:

pf5dev@gmail.com

I will reply ASAP
