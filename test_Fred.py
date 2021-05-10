#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import sympy as sym


# In[11]:


# Tests that Fred produces the correct roots for a example quadratic equation

a = 2
b = 4
c = 4
    
sqr_discriminant = (b**2 - 4*a*c)**0.5
x_1 = (-b + (sqr_discriminant))/(2*a)
x_2 = (-b - (sqr_discriminant))/(2*a)
    
expected_roots = np.roots([a, b, c])
np.round(expected_roots[0])
np.round(x_1.real) + np.round(x_1.imag)*1j
    
assert np.round(x_1.real) + np.round(x_1.imag)*1j == np.round(expected_roots[0]), "Should be " + np.round(expected_roots[0])


# In[12]:


# Tests that Fred produces the correct derivative for a example quadratic equation

a = 2
b = 4 
c = 4
    
x = sym.Symbol("x")
eq = a * (x ** 2) + (b * x) + c
diff_eq = sym.diff(eq)
    
expected_derivative = (2 * a * x) + b
    
assert diff_eq == expected_derivative, "Should be " + expected_derivative

