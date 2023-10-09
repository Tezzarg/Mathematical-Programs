import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
from scipy import constants
from sympy import *

lower_bound = 0
upper_bound = 5
delta = 0.05
# Initalising variables that will be called upon later.

x = Symbol('x')
# Instead of using lambda functions, I prefer to use the Sympy library.

eigenvalue = 1
funct = ((x**2) - eigenvalue) 
f_prime = diff(funct) # Using the sympy library to perform symbolic differentiation. 
f_2prime = diff(f_prime)
n = (eigenvalue - 1)/2

if (eigenvalue - 1)%2 == 0 and n%2 == 0: # Checking for n being even.
    print(n)
    print('n is even')
    psi0 = 1
    dpsi0 = 0
elif (eigenvalue - 1)%2 == 0 and n%2 == 1: # Checking for n being odd.
    print(n)
    print('n is odd')
    psi0 = 0
    dpsi0 = 1
else:
    print(n)
    print('n is not an integer, thus the solution is unphysical') # If n is neither even nor odd, n isn't an integer
    psi0 = 1
    dpsi0 = 0
    
x_values = np.arange(lower_bound, upper_bound + delta, delta)

def solve_numerov(f, x_values, psi0, dpsi0):
    f_values = []
    
    for i in x_values:
        j = f.subs(x, i)
        f_values.append(j)

    # This generates a list of values for the function f, evaluated for all steps in x. 

    psi1 = (psi0) + (dpsi0 * delta) + (0.5 * delta**2 * f.subs(x, lower_bound) * psi0)\
           + ((1/6 * delta**3) * (f.subs(x, lower_bound)*dpsi0 + f_prime.subs(x, lower_bound) * psi0))\
           + ((1/24 * delta**4) * (f_2prime.subs(x, lower_bound) * psi0 + (2* f_prime.subs(x, lower_bound) * dpsi0)\
           + (f.subs(x,lower_bound)**2 * psi0))) # Finding the second point via Taylor series so that the iteration scheme can begin.
    
    psi_values = [psi0, psi1]

    for i in range(0, (len(x_values) - 2)): # Repeat len(x_values) - 2 times because we already have 2 elements inside psi_values.
        next_psi = (((2 + (5/6 * delta**2 * f_values[i+1])) * psi_values[i+1]) - ((1 - (1/12 * delta**2 * f_values[i])) * psi_values[i]))\
                   /(1 - (1/12 * delta**2 * f_values[i+2])) # Applying Numerov's method iteratively to find the next point.

        psi_values.append(next_psi)
        # After the next point is calculated, it is appended to psi_values, where it can be used for the next loop/cycle.
        
    return psi_values # As per the lab script, this function now returns a list containing all values for psi.

print(sp.polys.orthopolys.hermite_poly(n)) # Using in-built sympy function for generate Hermite polynomials.
hermite = 2*x
analytical_solution = 0.5 * (hermite) * exp(((-x**2)/2)) # Need to scale analytical function by 0.5 so it matches numerical answer.
#print(analytical_solution)
y_values = []

for i in x_values: # Generating points to plot the analytical solution to the Schrödinger equation.
    value = analytical_solution.subs(x,i)
    y_values.append(value)

plt.figure(1)
plt.plot(x_values, y_values)
plt.title("Analytical Wave Function Solution to Schrödinger Equation")
plt.xlabel('x')
plt.ylabel('Ψ(x)')

#print((solve_numerov(funct, x_values, psi0, dpsi0)))
E = 0.95
function = ((x**2) - E)
psi_test = solve_numerov(function, x_values, psi0, dpsi0)
#print(psi_test)

psi_even = 1
dpsi_even = 0
psi_odd = 0
dpsi_odd = 1
##################### NOTE TO SELF, SWITCH VALUES OF BOUNDARY CONDITIONS ABOVE WHEN ALTERNATING BETWEEN EIGENVALUE GUESSES!!! 
          
def find_oscillator_eigenvalue(E0): # Function to find nearest eigenvalue based on lab script method. 

    epsilon = 0.01
    list_1 = []

    if (round(E0) - E0) < 0 :
        for i in range(1, 25):
            if type(round(E0)%2) == "int": # Checking whether E0 is even or odd so that the right boundary conditions can be applied.
                E = E0 - i*epsilon
                function = ((x**2) - E)
                psi_test = solve_numerov(function, x_values, psi_even, dpsi_even)
                list_1.append((abs(psi_test[-1])))
            else:
                E = E0 - i*epsilon
                function = ((x**2) - E)
                psi_test = solve_numerov(function, x_values, psi_odd, dpsi_odd)
                list_1.append((abs(psi_test[-1])))
            # Going in the negative direction.
             
        minimum = min(list_1) # This finds the element in the list that is closest to 0.
        #print(list_1)
        #print(minimum)

        for j in list_1:
            if j == minimum:
                deltas = list_1.index(j) + 1 # The number of steps taken to reach the minimum value from the intial guess.
                return E0 - deltas*epsilon 
                
    elif (round(E0) - E0) > 0 :
        for i in range(1, 25):
            if type(round(E0)%2) == "int": # Checking whether E0 is even or odd so that the right boundary conditions can be applied.
                E = E0 + i*epsilon
                function = ((x**2) - E)
                psi_test = solve_numerov(function, x_values, psi_even, dpsi_even)
                list_1.append((abs(psi_test[-1])))
            else:
                E = E0 + i*epsilon
                function = ((x**2) - E)
                psi_test = solve_numerov(function, x_values, psi_odd, dpsi_odd)
                list_1.append((abs(psi_test[-1])))
                # Going in the negative direction.

        minimum = min(list_1) #This finds the element in the list that is closest to 0.
        #print(list_1)
        #print(minimum)
        
        for k in list_1:
            if k == minimum:
                deltas = list_1.index(k) + 1 # The number of steps taken to reach the minimum value from the intial guess.
                return E0 + deltas*epsilon

    else: return("You have guessed an eigenvalue!")

print(find_oscillator_eigenvalue(3.05)) # Calling function B. 
psi = solve_numerov(funct, x_values, psi0, dpsi0) # Solving the Schrödinger equation numerically.

plt.figure(2)
plt.plot(x_values, psi)
plt.title("Numerical Wave Function Solution to Schrödinger Equation")
plt.xlabel('x')
plt.ylabel('Ψ(x)')
plt.show()











    
    
    

        
