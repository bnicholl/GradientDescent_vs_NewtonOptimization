#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:49:24 2018

@author: bennicholl
"""
# packages for analyses
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

"""hashtagged functions show the rosenbrock equation, and its first and second order derivitves"""
# Rosenbrock valley function = 100(x - x^2) ^2 + (1 - x)^2
# simplified                   101x^2 - 200x^3 + 100x^4 + 1 - 2x  
                            
# 1st order derivative         400x^3 − 600x^2 + 202x − 2               
# 2nd order derivative         1200x^2 - 1200x +202
"""hashtagged functions show newton-raphson optimazation and gradient descent optimization"""                
# Newton-Raphson optimization -  x - ( f' / f'' )
# Gradient descent            -  W0 := a·2·∑(W·x - Y)x)
#                             -  W1 := a·2·∑(W·x - Y)  

"""first 2 functions simply give values for rosenbrock function and its derivatives, and are optional"""
"""rosenbrock equation"""
def rosenbrock(x):
    function = 100 * (x - x**2)**2 + (1 - x)**2
    print(function)
    
"""prints the first and second order derivaitves for the rosenbrock equation"""    
def derivatives(x):
    first_order = 400 * x**3 - 600 * x **2 + 202 * x - 2
    print(first_order)
    second_order = 1200 * x**2 - 1200 * x +202
    print(second_order)  

"""a good x starting point is anywhere from 8 - 16"""
"""performs gradient descent on rosenbrock function"""
def gradient_descent(x, alpha = 0.000001):
    difference = 10   
    """the below lines of code plotthe function"""    
    fig = plt.figure(figsize=(10.5, 10.5))
    #fig.set_size_inches(9.5, 9.5)
    ax = fig.gca(projection='3d')
    """changes the azimuth"""
    ax.view_init(azim=110)
    
    """Make data for rosenbrock equation"""
    X = np.arange(-6, 16, .5)
    Y = np.arange(-6, 16, .5)
    X, Y = np.meshgrid(X, Y)
    Z = 100 * (Y - X**2) **2 + (1 - X)**2
    
    """Plot the surface of rosenbrock equation, with our data"""
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           antialiased=False)
    
        
    """instantiate first order derivative with our initial starting point, x"""
    first_order = 400 * x**3 - 600 * x **2 + 202 * x - 2    
    li = []
    
    while difference > 10**-5:  
        li.append(x)          
        x = x - alpha * first_order
        first_order = 400 * x**3 - 600 * x **2 + 202 * x - 2        
        difference = abs(x - (x - alpha * (first_order)) )       
    global x_values1  
    """This variable is our gradient path in both the x and y direction in a numpy vector""" 
    x_values1 =  np.array(li)
    
    """This variable is our gradient path in z direction in a numpy vector"""
    z = 100 * (x_values1 - x_values1**2) **2 + (1 - x_values1)**2
    ax.plot(x_values1,x_values1,z) 
    
    """plots [1,1] which is our global minimum in the function"""
    ax.plot([1],[1],[0], marker = 'x')
    return ax    

"""a good x starting point is anywhere from 8 - 16"""        
"""performs gradient descent on rosenbrock function"""
def newton_method(x):
    difference = 10
    """the below lines of code plotthe function"""
    fig = plt.figure(figsize=(10.5, 10.5))
    
    ax = fig.gca(projection='3d')
    """changes the azimuth"""
    ax.view_init(azim=110)
    
    """Make data for rosenbrock equation."""
    X = np.arange(-6, 16, .5)
    Y = np.arange(-6, 16, .5)
    X, Y = np.meshgrid(X, Y)
    Z = 100 * (Y - X**2) **2 + (1 - X)**2
    
    """Plot the surface of rosenbrock equation, with our data"""
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           antialiased=False)
    
      
    """instantiate first order derivative with our initial starting point, x"""
    first_order = 400 * x**3 - 600 * x **2 + 202 * x - 2
    """instantiate second order derivative with our initial starting point, x"""
    second_order = 1200 * x**2 - 1200 * x +202
    li = []
    
    while difference > 10**-10:
        li.append(x)
        x = x - (first_order/second_order)
        first_order = 400 * x**3 - 600 * x **2 + 202 * x - 2
        second_order = 1200 * x**2 - 1200 * x +202
        """calculates difference of previous and current x locations if X
        locations havn't changed, we reached local minimum and loop will stop"""
        difference = abs(x - (x - (first_order/second_order)) )  
    global x_values2
    """This variable is our gradient path in both the x and y direction in a numpy vector""" 
    x_values2 = np.array(li)
    """This variable is our gradient path in z direction in a numpy vector"""
    z = 100 * (x_values2 - x_values2**2) **2 + (1 - x_values2)**2
    ax.plot(x_values2,x_values2,z)  
    
    """plots [1,1] which is our global minimum in the function"""
    ax.plot([1],[1],[0], marker = 'x')
    return ax    
    
        
        
        