import Tkinter as tk
import ttk
import integrator as terminator
import gaussian
import math
import time
 
root = tk.Tk()

timestring = '\nComplete in {} seconds'
 
class gui():
    def __init__(self):

        root.wm_title('Garrett Schwartz - Integration Functions')
        
        self.notebook = ttk.Notebook(root)
       
        self.trapezoid_method = ttk.Frame(self.notebook)
        self.simpson_composite = ttk.Frame(self.notebook)
        self.romberg = ttk.Frame(self.notebook)
        self.adaptive_trapezoid = ttk.Frame(self.notebook)
        self.adaptive_simpson = ttk.Frame(self.notebook)
        self.composite_midpoint = ttk.Frame(self.notebook)
        self.gaussian = ttk.Frame(self.notebook)
       
        self.notebook.add(self.trapezoid_method, text='Trapezoidal Method')
        self.notebook.add(self.simpson_composite, text='Simpson\'s Composite Method')
        self.notebook.add(self.romberg, text='Romberg')
        self.notebook.add(self.adaptive_trapezoid, text= 'Adaptive Trapezoid')
        self.notebook.add(self.adaptive_simpson , text='Adaptive Simpson\'s Rule')
        self.notebook.add(self.composite_midpoint , text='Composite Midpoint')
        self.notebook.add(self.gaussian , text='Gaussian Quadrature')
       
        self.notebook.grid(row = 0, column = 0)
       
        self.gui_trapezoid_method(self.trapezoid_method)
        self.gui_simpson_composite(self.simpson_composite)
        self.gui_romberg(self.romberg)
        self.gui_adaptive_trapezoid(self.adaptive_trapezoid)
        self.gui_adaptive_simpson(self.adaptive_simpson)
        self.gui_composite_midpoint(self.composite_midpoint)
        self.gui_gaussian(self.gaussian)

    #-------------------------------------------------------------------------------------------------
    def gui_trapezoid_method(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_trap_method = tk.Entry(root)
        self.function_trap_method.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_trap_method = tk.Entry(root)
        self.start_trap_method.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_trap_method = tk.Entry(root)
        self.end_trap_method.grid(row=2, column=1)
       
        #Steps
        tk.Label(root, text='Steps:').grid(row=3, column=0)
        #Input
        self.steps_trap_method = tk.Entry(root)
        self.steps_trap_method.grid(row=3, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_trap_method = tk.Text(root, height=5, width=40)
        self.text_trap_method.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_trap_method.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_trap_method.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_trap_method.grid(row=1, column=4, rowspan=3)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_trapezoid_method).grid(row=4, column=0)
       
    def do_trapezoid_method(self):
        function = self.function_trap_method.get()
        start = float(self.start_trap_method.get())
        end = float(self.end_trap_method.get())
        steps = float(self.steps_trap_method.get())
        
        time1 = time.clock()
        result = terminator.trapezoid_method(function, start, end, steps) #GET RESULT FROM TRAP METHOD
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'
        
        self.text_trap_method.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_trap_method.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_trap_method.insert(tk.END, result)     #PRINT RESULT
        self.text_trap_method.insert(tk.END, timestring.format(func_time))
        self.text_trap_method.config(state=tk.DISABLED)  #PREVENT OUTPUT
    #-------------------------------------------------------------------------------------------------

    def gui_simpson_composite(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_simp_comp = tk.Entry(root)
        self.function_simp_comp.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_simp_comp = tk.Entry(root)
        self.start_simp_comp.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_simp_comp = tk.Entry(root)
        self.end_simp_comp.grid(row=2, column=1)
       
        #Steps
        tk.Label(root, text='N:').grid(row=3, column=0)
        #Input
        self.steps_simp_comp = tk.Entry(root)
        self.steps_simp_comp.grid(row=3, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_simp_comp = tk.Text(root, height=5, width=40)
        self.text_simp_comp.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_simp_comp.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_simp_comp.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_simp_comp.grid(row=1, column=4, rowspan=3)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_simp_comp).grid(row=4, column=0)

    def do_simp_comp(self):
        function = self.function_simp_comp.get()
        start = float(self.start_simp_comp.get())
        end = float(self.end_simp_comp.get())
        steps = int(self.steps_simp_comp.get())
        
        time1 = time.clock()
        result = terminator.simpson_composite(function, start, end, steps) #GET RESULT FROM SIMP COMP
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'
        
        self.text_simp_comp.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_simp_comp.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_simp_comp.insert(tk.END, result)     #PRINT RESULT
        self.text_simp_comp.insert(tk.END, timestring.format(func_time))
        self.text_simp_comp.config(state=tk.DISABLED)  #PREVENT OUTPUT

    #-------------------------------------------------------------------------------------------------

    def gui_romberg(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_romberg = tk.Entry(root)
        self.function_romberg.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_romberg = tk.Entry(root)
        self.start_romberg.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_romberg = tk.Entry(root)
        self.end_romberg.grid(row=2, column=1)
       
        #N
        tk.Label(root, text='N:').grid(row=3, column=0)
        #Input
        self.n_romberg = tk.Entry(root)
        self.n_romberg.grid(row=3, column=1)

        #M
        tk.Label(root, text='M:').grid(row=4, column=0)
        #Input
        self.m_romberg = tk.Entry(root)
        self.m_romberg.grid(row=4, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_romberg = tk.Text(root, height=8, width=40)
        self.text_romberg.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_romberg.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_romberg.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_romberg.grid(row=1, column=4, rowspan=6)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_romberg).grid(row=5, column=0)

    def do_romberg(self):
        function = self.function_romberg.get()
        start = float(self.start_romberg.get())
        end = float(self.end_romberg.get())
        n = int(self.n_romberg.get())
        m = int(self.m_romberg.get())

        time1 = time.clock()
        result = terminator.romberg(function, start, end, n, m) #GET RESULT FROM ROMBERG
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'

        str_to_print = 'Printing rightmost values:'

        

        for i in result:
            for j in i:
                if not math.isnan(j):
                    c = '\nR({},{}): {}'.format(result.index(i),i.index(j),j)
                if i.index(j) == len(i) - 1:
                    str_to_print += c
        
        self.text_romberg.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_romberg.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_romberg.insert(tk.END, str_to_print)     #PRINT RESULT
        self.text_romberg.insert(tk.END, timestring.format(func_time))
        self.text_romberg.config(state=tk.DISABLED)  #PREVENT OUTPUT

    #-------------------------------------------------------------------------------------------------

    
        
    #-------------------------------------------------------------------------------------------------

    def gui_adaptive_trapezoid(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_adaptive_trapezoid = tk.Entry(root)
        self.function_adaptive_trapezoid.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_adaptive_trapezoid = tk.Entry(root)
        self.start_adaptive_trapezoid.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_adaptive_trapezoid = tk.Entry(root)
        self.end_adaptive_trapezoid.grid(row=2, column=1)
       
        #Steps
        tk.Label(root, text='Tolerance:').grid(row=3, column=0)
        #Input
        self.tolerance_adaptive_trapezoid = tk.Entry(root)
        self.tolerance_adaptive_trapezoid.grid(row=3, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_adaptive_trapezoid = tk.Text(root, height=5, width=40)
        self.text_adaptive_trapezoid.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_adaptive_trapezoid.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_adaptive_trapezoid.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_adaptive_trapezoid.grid(row=1, column=4, rowspan=3)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_adaptive_trapezoid).grid(row=4, column=0)

    def do_adaptive_trapezoid(self):
        function = self.function_adaptive_trapezoid.get()
        start = float(self.start_adaptive_trapezoid.get())
        end = float(self.end_adaptive_trapezoid.get())
        tolerance = float(self.tolerance_adaptive_trapezoid.get())

        time1 = time.clock()
        result = terminator.adaptive_trap(function, start, end, tolerance) #GET RESULT 
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'
       
        self.text_adaptive_trapezoid.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_adaptive_trapezoid.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_adaptive_trapezoid.insert(tk.END, result)     #PRINT RESULT
        self.text_adaptive_trapezoid.insert(tk.END, timestring.format(func_time))
        self.text_adaptive_trapezoid.config(state=tk.DISABLED)  #PREVENT OUTPUT

    #-------------------------------------------------------------------------------------------------

    def gui_adaptive_simpson(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_adaptive_simpson = tk.Entry(root)
        self.function_adaptive_simpson.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_adaptive_simpson = tk.Entry(root)
        self.start_adaptive_simpson.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_adaptive_simpson = tk.Entry(root)
        self.end_adaptive_simpson.grid(row=2, column=1)
       
        #Steps
        tk.Label(root, text='Tolerance:').grid(row=3, column=0)
        #Input
        self.tolerance_adaptive_simpson = tk.Entry(root)
        self.tolerance_adaptive_simpson.grid(row=3, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_adaptive_simpson = tk.Text(root, height=5, width=40)
        self.text_adaptive_simpson.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_adaptive_simpson.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_adaptive_simpson.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_adaptive_simpson.grid(row=1, column=4, rowspan=3)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_adaptive_simpson).grid(row=4, column=0)

    def do_adaptive_simpson(self):
        function = self.function_adaptive_simpson.get()
        start = float(self.start_adaptive_simpson.get())
        end = float(self.end_adaptive_simpson.get())
        tolerance = float(self.tolerance_adaptive_simpson.get())

        time1 = time.clock()
        result = terminator.adaptive_simpson(function, start, end, tolerance) #GET RESULT FROM ADAPT SIMP
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'
        
       
        
        self.text_adaptive_simpson.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_adaptive_simpson.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_adaptive_simpson.insert(tk.END, result)     #PRINT RESULT
        self.text_adaptive_simpson.insert(tk.END, timestring.format(func_time))
        self.text_adaptive_simpson.config(state=tk.DISABLED)  #PREVENT OUTPUT

    #-------------------------------------------------------------------------------------------------

    def gui_composite_midpoint(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_composite_midpoint = tk.Entry(root)
        self.function_composite_midpoint.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_composite_midpoint = tk.Entry(root)
        self.start_composite_midpoint.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_composite_midpoint = tk.Entry(root)
        self.end_composite_midpoint.grid(row=2, column=1)
       
        #Steps
        tk.Label(root, text='M:').grid(row=3, column=0)
        #Input
        self.m_composite_midpoint = tk.Entry(root)
        self.m_composite_midpoint.grid(row=3, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_composite_midpoint = tk.Text(root, height=5, width=40)
        self.text_composite_midpoint.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_composite_midpoint.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_composite_midpoint.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_composite_midpoint.grid(row=1, column=4, rowspan=3)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_composite_midpoint).grid(row=4, column=0)

    def do_composite_midpoint(self):
        function = self.function_composite_midpoint.get()
        start = float(self.start_composite_midpoint.get())
        end = float(self.end_composite_midpoint.get())
        m = float(self.m_composite_midpoint.get())

        time1 = time.clock()
        result = terminator.composite_midpoint_rule(function, start, end, m) #GET RESULT FROM MID COMP
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'
        
       
        
        self.text_composite_midpoint.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_composite_midpoint.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_composite_midpoint.insert(tk.END, result)     #PRINT RESULT
        self.text_composite_midpoint.insert(tk.END, timestring.format(func_time))
        self.text_composite_midpoint.config(state=tk.DISABLED)  #PREVENT OUTPUT

    #-------------------------------------------------------------------------------------------------

    def gui_gaussian(self, root):
        #INPUTS
        #Function
        tk.Label(root, text='Function:').grid(row=0, column=0)
        #Input
        self.function_gaussian = tk.Entry(root)
        self.function_gaussian.grid(row=0, column=1)
       
        #Start Interval
        tk.Label(root, text='Start:').grid(row=1, column=0)
        #Input
        self.start_gaussian = tk.Entry(root)
        self.start_gaussian.grid(row=1, column=1)
       
        #End Interval
        tk.Label(root, text='End:').grid(row=2, column=0)
        #Input
        self.end_gaussian = tk.Entry(root)
        self.end_gaussian.grid(row=2, column=1)
       
        #Steps
        tk.Label(root, text='Order:').grid(row=3, column=0)
        #Input
        self.order_gaussian = tk.Entry(root)
        self.order_gaussian.grid(row=3, column=1)
       
        #OUTPUT
        tk.Label(root, text='Result:').grid(row=0, column=4)
        #output
        self.text_gaussian = tk.Text(root, height=5, width=40)
        self.text_gaussian.config(state=tk.NORMAL)    #ALLOW OUTPUT
        self.text_gaussian.delete('1.0', tk.END)      #CLEAR ALL OUTPUT
        self.text_gaussian.config(state=tk.DISABLED)  #PREVENT OUTPUT
        self.text_gaussian.grid(row=1, column=4, rowspan=3)
       
        calc_button = tk.Button(root, text='Calculate', command=self.do_gaussian).grid(row=4, column=0)

    def do_gaussian(self):
        function = self.function_gaussian.get()
        start = float(self.start_gaussian.get())
        end = float(self.end_gaussian.get())
        order = int(self.order_gaussian.get())
        
        time1 = time.clock()
        res = gaussian.GaussLegendreWeights(order)
        time2 = time.clock()

        func_time = time2 - time1

        if func_time == 0.0:
            func_time = 'less than 1/10'

        if res[2] != 0:
            str_1 = 'Root and Weight Evaluation Failed'
        else:
            str_1 = ''
       
        result = gaussian.gaussian_quadrature(function, start, end, order) #GET RESULT FROM MID COMP

        if result[1] != 0:
            str_2 = 'Integral Evaluation Failed :('
        else:
            str_2 = 'Integral\t\t:{}'.format(result[0])

        str_to_print = str_1 + '\n' + str_2
        self.text_gaussian.config(state=tk.NORMAL)    #ALLOW WRITING TO THE BOX
        self.text_gaussian.delete('1.0', tk.END)      #CLEAR THE BOX
        self.text_gaussian.insert(tk.END, str_to_print)     #PRINT RESULT
        self.text_gaussian.insert(tk.END, timestring.format(func_time))
        self.text_gaussian.config(state=tk.DISABLED)  #PREVENT OUTPUT

    #-------------------------------------------------------------------------------------------------
        
gui_window = gui()
root.mainloop()
