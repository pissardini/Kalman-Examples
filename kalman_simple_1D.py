#******************************************************************
# FILE: kalman_1D_simple.py
# DESCRIPTION: This program presents a simplified version of Kalman Filter
# without iteration for instructive comprehension.
# VERSION: 0.0.1
# AUTHOR: R.S. Pissardini
# LICENSE: MIT License. 
#******************************************************************/

def Kalman_Gain (error_est, error_meas):
    k = error_est/(error_est+ error_meas)
    return k

def Current_State(state_prev, k, measure):
    state_curr = state_prev + k * (measure - state_prev)
    return state_curr

def Current_Estimative(error_prev, k ):
    error_curr = (1 - k) * error_prev
    return error_curr

initial_state = 28
measure = 32
estimated_error = 2
measure_error = 1

k             = Kalman_Gain (estimated_error, measure_error)
current_state = Current_State(initial_state,k, measure)
current_error = Current_Estimative(estimated_error, k )

print([round(k,2),round(current_state,2),round(current_error,2)])

#end
