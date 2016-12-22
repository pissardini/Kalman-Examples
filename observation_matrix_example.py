#******************************************************************
# FILE: observation_matrix_example.py
# DESCRIPTION: This script presents three examples of observation matrix for Kalman Filter
# VERSION: 0.0.1
# AUTHOR: R.S. Pissardini
# LICENSE: MIT License. 
#******************************************************************/

from matrix import *

## Observation Matrix (Y = Cx + z)

# Test 1 - only position

C = matrix([[1.,0.]])
x = matrix([[4],
            [2]])

Y = C * x
print("Test 1: "+ str(Y))


# Test 2 - only velocity

C = matrix([[0.,1.]])
x = matrix([[4],
            [2]])

Y = C * x
print("Test 2: "+ str(Y))


# Test 3 - position and velocity

C = matrix([[1.,0.],
            [0.,1.]])
x = matrix([[4.],
            [2.]])

Y = C * x
print("Test 3: "+ str(Y))
