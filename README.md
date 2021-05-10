# Documentation for <mark>Fred</mark>

## Fred
Software to study quadratic functions

## Tutorial

In this tutorial we will see how to use <mark>Fred</mark> to study quadratic functions. For some background infomation on quadratic functions we recommend: https://en.wikipedia.org/wiki/Quadratic_function

### Installing required libaries
Enter the following in your terminal to obtain the required libaries for <mark>Fred</mark> (If you do not already own them):
```python
pip install matplotlib
pip install numpy
pip install sympy
pip install math
```
### Downloading the Python script for <mark>Fred</mark>
Download the script for <mark>Fred</mark> from here: https://drive.google.com/uc?export=download&id=1O7GKBvJbOBp3NLKjayflUCAR9qX2X6G2

### Loading up <mark>Fred</mark> in terminal
First locate the location of the Fred.py file
Then open up your terminal and type in the following:
```python
cd <location>

py Fred.py
```
![image.png](./downloads/Fred_Images/1.png)

### Operating Fred
After Loading up <mark>Fred</mark> you will be prompted to enter values of the coefficients a, b and c

For Example: 
```python
Please submit your values of coefficients a, b, c for a function of form: f(x) = ax^2 + bx + c = 0, with a ≠ 0
Enter the value of a: 4
Enter the value of b: 5
Enter the value of c: 6
```

### Understanding Fred
Now this will run the python script for <mark>Fred</mark> , of which will determine:

- The roots of the function 
- The minima/maxima of the function 
- The derivative of the function

For Example (Continuing from above):

```python
This function has 2 distinct complex conjugate roots:
Root 1 = : (-0.6249999999999999+1.0532687216470449j)
Root 2 = : (-0.6250000000000001-1.0532687216470449j)
```
```python
Your function has 1 minimum point at (-0.625000000000000 , 4.43750000000000)
```
```python
The derivative of your function is given by: f'(x) = 8.0 x + 5.0

```

<mark>Fred</mark> will also produce graphs of:

- The function
- The derivative

, and if the function produces complex roots:

- The complex roots in the complex plane

For Example (Continuing from above):

![image.png](./downloads/Fred_Images/6.png)

![image.png](./downloads/Fred_Images/7.png)

![image.png](./downloads/Fred_Images/8.png)

## How to Guides

### How to load <mark>Fred</mark>

Locate the location of the Fred.py file

Then open up your terminal and type in the following:
```python
cd <location>

py Fred.py
```
![image.png](./downloads/Fred_Images/1.png)

### How to operate <mark>Fred</mark>

Once you have values for the coefficients for a, b and c of a polynomial of form
```python
f(x) = ax^2 + bx + c = 0
```
then input your values into <mark>Fred</mark> , e.g.
```python
For 4x^2 + 5x + 6 = 0
```
![image.png](./downloads/Fred_Images/0.2.png)

### How to test the software

To test the code:
```python
$ py test_Fred.py
```
To test the documentation:
```python
$ py -m doctest README.md
```

## Explanation

### Brief overview of solving quadratic functions

The general solution for a quadratic equation: 
$$ ax^2+bx+c=0 $$
is given by the "Quadratic Formula":
$$ x = \frac{-b\pm\sqrt{b^2-4ac}}{2a} $$
which produces the roots of the quadratic function.

$$ f(x) = ax^2+bx+c $$

(For proof of the formula seek: https://www.chilimath.com/lessons/intermediate-algebra/derive-quadratic-formula/)

### Determining the number and types of roots of the quadratic function

Here we can consider the discriminant of the quadratic function:
$$ b^2 - 4ac $$

We have 3 possible cases depending on the the given quadratic function:

Case 1: $$ b^2 - 4ac > 0$$

- Then our quadratic function will have " Two distinct and real roots " given by:
$$ Root_1 = \frac{-b + \sqrt{b^2-4ac}}{2a} $$

$$ Root_2 = \frac{-b - \sqrt{b^2-4ac}}{2a} $$

Case 2: $$ b^2 - 4ac = 0$$

- Then our quadratic function will have " Two equal and real roots " given by:
$$ Root_1 = Root_2 =  \frac{-b}{2a} $$

Case 3: $$ b^2 - 4ac < 0$$

- Then our quadratic function will have " Two distinct complex conjugate roots" given by:
$$ Root_1 = \frac{-b}{2a} + \frac{i\sqrt{-(b^2-4ac)}}{2a} $$

$$ Root_2 = \frac{-b}{2a} - \frac{i\sqrt{-(b^2-4ac)}}{2a}  $$



This can be all be determined in the following code
```python
import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

# Creating the function 
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
        print('Root 2 = : {0}'.format(x_2)

```

### Finding the minima/maxima of the quadratic function
To find the minima / maxima of the quadratic function we do the following:

1. Differentiate our quadratic equation
- Create a equation of this derivative equal to 0
- Solve the equation for the value of x
- Plug in this value of x to obtain the f(x)

Now we need to determine if our coordinate obtained is a minima or maxima, and we do this by taking the second derivative of the quadratic function:
-  If $$ f''(x) > 0 $$

, then our coordinate obtained is the "minima" of the quadratic function

-  If $$ f''(x) < 0 $$

, then our coordinate obtained is the "maxima" of the quadratic function

(We dont consider the case for f''(x) = 0 , since we are only dealing with quadratic functions)

This can be all be represented in the following code:
```python

    
```

### Plotting our quadratic function with the real roots & minima/maxima indicated

Here we use the matplotlib library to create a graph to plot our quadratic function.

Our quadratic function can be graphed by the following code:

```python
import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

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

```

### Plotting roots in the complex plane
In the case our discriminant < 0 , we will be unable to plot any real roots of our quadratic function on the graph.

Therefore we create a graph using the matplotlib library to show the behaviour of these complex roots in the complex plane , which can be graphed by the following code:

```python
import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

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
   
```


### Plotting the derivative of the quadratic function
Again we use the matplotlib library to create a graph for the derivative of our quadratic function , which can be graphed by the following code:
```python
import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import math

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

```

## References

### The following sites helped to develop Fred
- The quadratic formula: https://en.wikipedia.org/wiki/Quadratic_formula ' 
- Implementing the quadratic formula in python: https://mathbitsnotebook.com/Algebra2/Quadratics/QDQuadratics.html
- Understanding quadratic functions with complex solutions: https://mathbitsnotebook.com/Algebra2/Quadratics/QDQuadratics.html
- Graphing using Matplotlib: https://matplotlib.org/stable/tutorials/introductory/pyplot.html

### Bibliography
The wikipedia page on quadratic equations gives a great overview of the topic:
https://en.wikipedia.org/wiki/Quadratic_equation

The following text is recommended for gaining a greater grasp on quadratic equations and understanding how their graphs behave:
> Redden, John. Beginning Algebra, Chapter 9: Solving Quadratic Equations and Graphing Parabolas, Creative Commons by-nc-sa, 2012


```python

```
