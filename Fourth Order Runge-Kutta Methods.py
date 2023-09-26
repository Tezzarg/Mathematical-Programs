import numpy as np
import math as math
import sympy as sympy
import random
from sympy import symbols, diff, integrate
from matplotlib import pyplot as plt

### This program uses fourth-order Runge-Kutta numerical methods to solve first-order differential equations as well as systems of first order differential equations. 

x, y = symbols("x y")

# Enter the first order differential equation here.
derivative = 
# Enter the initial conditions here.
x_0 = 
y_0 = 
# Enter the step size here (smaller step sizes will produce more accurate solutions, at the cost of computational time).
h = 
# Enter the lower and upper limits to specify the domain over which the differential equation is being solved. 
lower = 
upper = 

steps = (upper - lower) / h
steps = int(steps)
x_step = []

for i in range(0, steps + 1):
    x_value = x_0 + (i * h)
    x_step.append(x_value)

y_values = [y_0]
x_step_2 = x_step[1:]

for i in x_step_2: 
    k_1 = derivative.subs(([x, i] , [y, y_0])) 
    k_2 = derivative.subs(([x, (i + h/2)] , [y, (y_0 + (k_1 * h/2))]))
    k_3 = derivative.subs(([x, (i + h/2)] , [y, (y_0 + (k_2 * h/2))]))
    k_4 = derivative.subs(([x, (i + h)] , [y, (y_0 + (k_3 * h))]))
    y_0 = y_0 + (h*(k_1 + 2*k_2 + 2*k_3 + k_4))/6
    y_values.append(y_0)

#print(x_step)
#print(y_values)

plt.plot(x_step, y_values)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution to ODE")
plt.show()


