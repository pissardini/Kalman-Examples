#******************************************************************
# FILE: state_matrix_example.py
# DESCRIPTION: This script presents three examples of state matrix
# without iterations
# VERSION: 0.0.1
# AUTHOR: R.S. Pissardini
# LICENSE: MIT License. 
#******************************************************************/

from matrix import *

def State_Matrix(A, B, x_prev, u, w):    
    x_curr  = (A * x_prev)+ (B * u) + w
    return x_curr

#begin

##1D (x)

p_x = 5 

A = matrix([[1.]])
B = matrix([[0.]])
x = matrix([[p_x]])
u = matrix([[0]])
w = matrix([[0]])

print("Example 1 variable : " + str(State_Matrix(A, B, x, u, w)))

## Falling Ball - 1 D (y /y')

dt    = 1
a     = -9.8
p_y   = 20.
v_y   = 0. 

A = matrix([[1.,dt],
            [0.,1.]])

B = matrix([[0.5 * dt * dt],
            [dt]])

x = matrix([[p_y],
            [v_y]])

u = matrix([[a]])

w = matrix([[0.],
            [0.]])

print("Example 1D - Falling Ball (y /y'): "+ str(State_Matrix(A, B, x, u, w)))

## One-dimensional vehicle (x /x') -  1 D (x /x')

dt  = 1
a   = 2
p_x = 50.
v_x = 5.

A = matrix([[1.,dt],
           [0.,1.]]) # next state function

B = matrix([[0.5 * dt * dt],
            [dt]])

x = matrix([[p_x],
            [v_x]])

u = matrix([[a]])

w = matrix([[0.],
            [0.]])

print("Example 1D - One-dimensional vehicle (x /x'): " + str (State_Matrix(A, B, x,u, w)))

#end
