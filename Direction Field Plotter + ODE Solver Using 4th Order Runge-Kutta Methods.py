import numpy as np
import math as math
import sympy as sympy
import random
from sympy import symbols, diff, integrate
from matplotlib import pyplot as plt
from sympy.solvers import solve

### This program uses fourth-order Runge-Kutta numerical methods to solve first-order differential equations as well as systems of first order differential equations. 

y, x = symbols("y x")

# Enter the first order differential equation here.
derivative = ((y**2 + x**5)*y**2)/((x-3)*(y*(3/2)))

# Enter the initial conditions here.
x_0 = 0
y_0 = 1

# Enter the step size here (smaller step sizes will produce more accurate solutions, at the cost of computational time).
h = 0.01

# Enter the lower and upper limits to specify the domain over which the differential equation is being solved. 
lower = 1
upper = 2


#critical_values = solve(denominator)
#crit_values = []
#list_1 = []

#for i in critical_values:
    #crit_values.append(i)
    
#print(crit_values)
#print(list_1)
#print(critical_values)
steps = (upper - lower) / h
steps = int(steps)
x_step = np.array([], dtype = 'float64')

for i in range(0, steps + 1):
    x_value = x_0 + (i * h)
    x_step = np.append(x_step, [x_value])
    
y_values = np.array([y_0], dtype = 'float64')
x_step_2 = x_step[1:]

for i in x_step_2: 
    k_1 = derivative.subs([(x, i) , (y, y_0)]) 
    k_2 = derivative.subs([(x, (i + h/2)) , (y, (y_0 + (k_1 * h/2)))])
    k_3 = derivative.subs([(x, (i + h/2)) , (y, (y_0 + (k_2 * h/2)))])
    k_4 = derivative.subs([(x, (i + h)) , (y, (y_0 + (k_3 * h)))])
    y_0 = y_0 + (h*(k_1 + 2*k_2 + 2*k_3 + k_4))/6
    y_values = np.append(y_values, y_0)

#print(np.size(x_step))
#print(np.size(y_values))
#print(y_values)

plt.plot(x_step, y_values)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution to ODE")
plt.grid()
fig_1 = plt.figure("Figure 1")

x_1 = np.arange(-5,5.15,0.15)
y_1 = np.arange(-5,5.15,0.15)
X, Y = np.meshgrid(x_1, y_1)
ones = np.ones((int((np.size(X)))))
derivatives = []

#print(ones.shape)
#print(x_1)
#print(y_1)

for i in x_1:
    for j in y_1:
        scalar = derivative.subs([(x, i) , (y, j)])
        if scalar > 50:
            derivatives.append(50)
        else:
            derivatives.append(scalar)

derivatives_2 = np.array(derivatives, dtype=float)
#print(derivatives_2.shape)
normalised_ones = ones/np.sqrt(ones**2 + derivatives_2**2)
normalised_derivatives = derivatives_2/np.sqrt(ones**2 + derivatives_2**2)

#print(derivatives)
#print(len(derivatives))
derivatives_np = np.array(normalised_derivatives, dtype="float")

#plt.plot(X, Y, marker = ".", color = "k", linestyle = "none")
plt.xticks(x_1)
plt.yticks(y_1)
plt.xlabel(x)
plt.ylabel(y)
plt.title("Direction Field For ODE")
plt.quiver(Y, X, normalised_ones, derivatives_np, color='purple', headaxislength=2, headlength=0, pivot='middle', scale=10, linewidth=0.2, units='xy', width=0.01, headwidth=1)
plt.show()


            
            
