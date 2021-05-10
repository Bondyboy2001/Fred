#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math


# In[2]:


# Defining Function To Find Roots
def quadRoots(a, b, c):
    sqr_discriminant = (b**2 - 4*a*c)**0.5
    x_1 = (-b + (sqr_discriminant))/(2*a)
    x_2 = (-b - (sqr_discriminant))/(2*a)
    
    # Defining the discriminant 
    discriminant = (b**2 - 4*a*c)
    
    # Defining case discriminant > 0
    if discriminant > 0:
        print('This function has two distinct real roots: ')
        time.sleep(1)
        print('Root 1 = : {0}'.format(x_1))
        time.sleep(1)
        print('Root 2 = : {0}'.format(x_2))

    # Defining case discriminant = 0
    if discriminant == 0:
        print('This function two equal and real roots: ')
        time.sleep(1)
        print('Root 1 = Root 2 = : {0}'.format(x_1))                  

    # Defining case discriminant < 0
    elif discriminant < 0:
        print('This function has 2 distinct complex conjugate roots: ')
        time.sleep(1)
        print('Root 1 = : {0}'.format(x_1))
        time.sleep(1)
        print('Root 2 = : {0}'.format(x_2))

# Input Options
print('Please submit your values of coefficients a, b, c for a function of form: f(x) = ax^2 + bx + c, with a ≠ 0')
time.sleep(1)
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))
time.sleep(1)

# Function Call
quadRoots(a, b, c)


# In[3]:


# Finding the minima/maxima of the function
time.sleep(1)
x = sym.Symbol("x")
eq = a * (x ** 2) + (b * x) + c
diff_eq = sym.diff(eq)
diff_eq_equal_0 = sym.Eq(diff_eq, 0)
x_point = sym.solve(diff_eq_equal_0, x)
y_point = eq.subs(x, x_point[0])
min_or_max_point = sym.diff(diff_eq, x)

## Defining case function has a minima
if min_or_max_point > 0:
    time.sleep(1)
    print("Your function has 1 minimum point at (" + str(x_point[0]) + ' , ' + str(y_point) + ')')

## Defining case function has a maxima
elif min_or_max_point < 0:
    time.sleep(1)
    print("Your function has 1 maximum point at (" + str(x_point[0]) + ' , ' + str(y_point) + ')')


# In[4]:


# Creating a graph for the function
time.sleep(1.5)
print("Here is the graph of your function: ")

## 100 linearly spaced numbers
x = np.linspace(-20, 20, 1000)

## Defining our function
y = a * (x ** 2) + (b * x) + c

## Setting up the axes
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

## Plotting the function
ax.plot(x, y, 'b-', label="f(x)")

## Plotting the minimum/maximum point on the graph
if a > 0:
    ax.plot(x_point[0],y_point,'m*', label='Minima', markersize='6')
if a < 0:
    ax.plot(x_point[0],y_point,'m*', label='Maxima', markersize='6')

## Plotting the real roots on the graph
discriminant = (b**2 - 4*a*c)
if discriminant > 0:
    x_1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    x_2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
    ax.plot(x_1, 0, 'yo', label='Root 1')
    ax.plot(x_2, 0, 'go', label='Root 2')
elif discriminant == 0:
    x_1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    ax.plot(x_1, 0, 'yo', label='Double Root')
    
## Decorating the graph
plt.legend(loc='best',prop={'size': 15})
plt.axhline(0, color='gray')
plt.title('Graph of f(x)',fontsize=20)
ax.set_ylabel('f(x)', fontsize=15, color='r')
ax.set_xlabel('x', fontsize=15, color='r', horizontalalignment='left', x=1)
plt.show()


# In[5]:


# Plotting Roots in the complex plane (in case discriminant < 0)
if discriminant < 0:
    time.sleep(1.5)
    print("Here are the complex roots for the function plotted in the complex plane: ")
    
    ## Finding the real and imaginary parts of our roots 
    x_1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
    x_2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
    real_x1 = x_1.real
    imag_x1 = x_1.imag
    real_x2 = x_2.real
    imag_x2 = x_2.imag

    ## Setting up the graph and plotting our roots
    plt.figure(figsize=(8,8), dpi=80)
    plt.plot(real_x1,imag_x1,".",markersize=10)
    plt.plot(real_x2,imag_x2,".",markersize=10)
    plt.grid()
    plt.xlabel('Re(x)',fontsize=20,color='r')
    plt.ylabel('Im(x)',fontsize=20,color='r')

    ## Creating a straight line from the origin to our plotted roots
    point_1 = [x_1.real,x_1.imag]
    point_2 = [x_2.real,x_2.imag]
    point_3 = [0,0]
    x1_values = [point_1[0],point_3[0]]
    y1_values = [point_1[1],point_3[1]]
    plt.plot(x1_values,y1_values)
    x2_values = [point_2[0],point_3[0]]
    y2_values = [point_2[1],point_3[1]]
    plt.plot(x2_values,y2_values)

    ## Creating a circle passing through our roots
    r = math.sqrt((real_x1)**2 + (imag_x1)**2)
    x = np.linspace(-r,r,100)
    y = np.sqrt(-x**2+r**2)
    plt.plot(x, y,'b--',linewidth=0.5)
    plt.plot(x,-y,'b--',linewidth=0.5)
    plt.gca().set_aspect('equal')
    
    ## Decorating the graph
    plt.title('Roots in the Complex Plane',fontsize=20)
    plt.text(x_1.real,x_1.imag, str(x_1),verticalalignment='bottom',fontsize=15)
    plt.text(x_2.real,x_2.imag, str(x_2),verticalalignment='top',fontsize=15)
    plt.show()


# In[6]:


def quadDerivative(a, b, c):
    x = sym.Symbol("x")
    eq = a * (x ** 2) + (b * x) + c
    diff_eq = sym.diff(eq)
    latex_diff = sym.latex(diff_eq)
    time.sleep(1)
    print("The derivative of your function is given by: f'(x) = " + latex_diff)

# Function Call
quadDerivative(a, b, c)


# In[7]:


time.sleep(1)
print("Here is the graph of the derivative of your function: ")

# Creating a graph for the derivative

## 100 linearly spaced numbers
x = np.linspace(-10, 10, 1000)

## Defining our derivative
y = (2 * a) * x + b

## Setting up the axes
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

## Plotting the derivative
ax.plot(x, y, 'b-', label="f '(x)")

## Decorating the graph
plt.legend(loc='best',prop={'size': 15})
plt.axhline(0, color='gray')
plt.title("Graph of f '(x)",fontsize=20)
ax.set_ylabel("f ' (x)", fontsize=15, color='r', y=1,  rotation=1, verticalalignment='top', labelpad=-70)
ax.set_xlabel('x', fontsize=15, color='r', horizontalalignment='left', x=1)
plt.show()


# In[ ]:




