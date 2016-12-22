#******************************************************************
# FILE: prediction_step_example.py
# DESCRIPTION: This script presents three examples of prediction step
# with predicted state matrix and predicted covariance matrix
# VERSION: 0.0.1
# AUTHOR: R.S. Pissardini
# LICENSE: MIT License. 
#******************************************************************/

from matrix import *

# Prediction Step

def Predicted_State_Matrix(A, B, x_prev, u, w):    
    x_curr  = (A * x_prev)+ (B * u) + w
    return x_curr

def Predicted_Covariance_Matrix(A,P,D):
    P = (A * P * A.transpose())* D
    return P

#begin

#1D (x)

p_x  = 5 #initial value [position]
sd_x = 1 #standard-deviation example 

A = matrix([[1.]])
B = matrix([[0.]])
x = matrix([[p_x]])
u = matrix([[0]])
w = matrix([[0]])
P = matrix([[sd_x * sd_x]])
D = matrix([[1]])


print("Example 1D- 1 variable\nPredicted State:" + str(Predicted_State_Matrix(A, B, x, u, w))+\
            "\nCovariance Matrix:"+ str(Predicted_Covariance_Matrix(A,P,D))+"\n\n")

### Ball Falling - 1 D (y /y')

dt     = 1    #time lapse 
a      = -9.8 #acceleration
p_y    = 20.  #initial value [position - y]
sd_y   = 0.5  #standard-deviation [position - y]
v_y    = 0.   #initial value [velocity - y']
sd_vy  = 0.1  #standard-deviation [velocity - y']

A = matrix([[1.,dt],
            [0.,1.]])

B = matrix([[0.5 * dt * dt],
            [dt]])

x = matrix([[p_y],
            [v_y]])

u = matrix([[a]])

w = matrix([[0.],
            [0.]])

P = matrix([[sd_y  * sd_y, sd_y * sd_vy],
            [sd_vy * sd_y, sd_vy * sd_vy]])

D = matrix([[1,0],
            [0,1]])

print("Example 1D - Falling Ball (y /y')\nPredicted State:"  + str(Predicted_State_Matrix(A, B, x, u, w))+\
                      "\nCovariance Matrix:"+ str(Predicted_Covariance_Matrix(A,P,D))+"\n\n")

## Vehicle-  1 D (x /x')

dt   = 1    #time lapse 
a    = 2    #acceleration
p_x  = 50.  #initial value [position - x]
sd_x = 0.5  #standard-deviation [position - x]
v_x  = 5.   #initial value [velocity - x']
sd_vx = 0.2 #standard-deviation [velocity - x']

A = matrix([[1.,dt],
            [0.,1.]]) # next state function

B = matrix([[0.5 * dt * dt],
            [dt]])

x = matrix([[p_x],
            [v_x]])

u = matrix([[a]])

w = matrix([[0.],
            [0.]])
P = matrix([[sd_x * sd_x , sd_x * sd_vx],
            [sd_vx * sd_x, sd_vx * sd_vx]])

D = matrix([[1,0],
            [0,1]])


print("Example 1D\nOne-dimensional vehicle (x /x')\nPredicted State:" + str (Predicted_State_Matrix(A, B, x,u, w))+\
                                  "\nPredicted Covariance Matrix:"+ str(Predicted_Covariance_Matrix(A,P,D))+"\n\n")


#end
