#******************************************************************
# FILE: complete_kalman_example.py
# DESCRIPTION: This script presents complete kalman example - 1D
# VERSION: 0.0.1
# AUTHOR: R.S. Pissardini
# LICENSE: MIT License. 
#******************************************************************/

from matrix import *

# Prediction Step

def Prediction_State_Matrix(A, B, x_prev, u, w):    
    x_curr  = (A * x_prev)+ (B * u) + w
    return x_curr

def Prediction_Covariance_Matrix(A,P,D):
    P = (A * P * A.transpose())* D
    return P

# Correction Step

def Kalman_Gain(H, R, P):
    S = H * P * H.transpose() + R
    K = P * H.transpose() * S.inverse()
    return K

def Observation_Matrix(n,x,H):
    Z = matrix([n])
    Y = Z.transpose() - (H * x)
    return Y

def New_State(Y,x,K):
    x = x + (K * Y)
    return x

def New_Covariance(P,I,K,H):
    P = (I - (K * H)) * P
    return P

#begin 

print ("Kalman Filter Example- (x)(x')")
print ("One-diretional car - (x)(x')")
print ("--------------------------------------")

measurements = [[20,5],   # (x)(x')- 0 s
                [34,10],  # (x)(x')- 1 s
                [45,11],  # (x)(x')- 2 s
                [60,15],  # (x)(x')- 3 s
                [70,16],  # (x)(x')- 4 s
                [80,14],  # (x)(x')- 5 s
                [95,20]]  # (x)(x')- 6 s

##Initial Conditions 

dt    = 1  # time lapse 
a     = 2  # example acceleration (m/s^2) 
sd_x  = 2  # example standard-deviation for estimated position - x (m)
sd_v  = 3  # example standard-deviation for estimated velocity - x' (m/s)
d_x   = 1  # example standard-deviation for measured position - x (m)
d_v   = 2  # example standard-deviation for measured velocity - x' (m/s)

##Matrices

###State Matrix

A = matrix([[1.,dt],
            [0.,1.]]) 

B = matrix([[0.5* dt * dt],
            [dt]])

###Initial state 
x = matrix([[0.],
            [0.]])

u = matrix([[a]])

w = matrix([[0.],
            [0.]])

C  = matrix([[1,0],
             [0,0]])

D = matrix([[1,0],
            [0,1]])

H = matrix([[1,0],
            [0,1]])

I = matrix([[1,0],
            [0,1]])

### Predicted Process Covariance Matrix

P = matrix([[sd_x*sd_x, 0],
            [0, sd_v*sd_v]])

### Measurement Covariance Matrix 

R = matrix([[d_x * d_x, 0],
            [0, d_v * d_v]])

###Loop

for n in range(len(measurements)-1):

    # Prediction Step
    x = Prediction_State_Matrix(A, B, x, u, w)    
    P = Prediction_Covariance_Matrix(A,P,D)
    print ("Predicted :"+ str(x))
    
    # Correction Step
    
    K = Kalman_Gain(H,R,P)
    Y = Observation_Matrix(measurements[n+1],x,H)
    print ("Measured:"+ str(measurements[n+1]))
    
    x = New_State(Y,x,K)
    P=  New_Covariance(P,I,K,H)
    print ("Kalman:"+ str(x))
    print ("--------------------------------------")

#end
