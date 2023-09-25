import numpy as np
import math as math
import sympy as sympy
import random
from sympy import symbols, diff, integrate
from matplotlib import pyplot as plt 

x, y = symbols('x y')
y = 
lower_limit =  
upper_limit = 
n = 25000

width_of_rectangle = upper_limit - lower_limit 

if y.subs(x, upper_limit) >= y.subs(x, lower_limit):
    length_of_rectangle = y.subs(x, upper_limit)
else:
    length_of_rectangle = y.subs(x, lower_limit)

area_rectangle = width_of_rectangle * length_of_rectangle
x_coords = []

for i in range(1, n+1):
    x_coord = random.uniform(lower_limit, upper_limit)
    x_coords.append(x_coord)

y_coords_curve = []

for i in x_coords:
    y_coord_curve = y.subs(x, i)
    y_coords_curve.append(y_coord_curve)

y_coords = []

for i in range(1, n+1):
    y_coord = random.uniform(0, length_of_rectangle)
    y_coords.append(y_coord)

random_coords = [x_coords, y_coords]
curve_coords = [x_coords, y_coords_curve]
valid_points = []

for i in range(0, n):
    for j in range(0, n):
        if i == j and random_coords[1][j] < curve_coords[1][i]:
            valid_points.append(j) 

number_of_valid_points = len(valid_points)
fraction = number_of_valid_points / n
answer = area_rectangle * fraction
print(answer)

x_values = np.linspace(lower_limit, upper_limit, 100)
y_values = x_values ** 2
plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function Over Interval") 
plt.show() 


