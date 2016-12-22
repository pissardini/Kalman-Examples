#******************************************************************
# FILE: kalman_simple_1D_loop.py
# DESCRIPTION: This program presents a simplified version of Kalman Filter
# with loop for instructive comprehension.
# VERSION: 0.0.1
# AUTHOR: R.S. Pissardini
# LICENSE: MIT License. 
#******************************************************************/

def Kalman_Gain (error_est, error_meas):
    k = error_est/(error_est+ error_meas)
    return k

def Current_State (state_prev, k, measure):
    state_curr = state_prev + k * (measure - state_prev)
    return state_curr

def Current_Estimative (error_prev, k ):
    error_curr = (1 - k) * error_prev
    return error_curr

# begin 

estimated_error = previous_error = 2
measure_error = 1
initial_state = previous_state = 28

measures = [32, 35, 33]

# Loop

for new_measure in measures:

    k             = Kalman_Gain (previous_error, measure_error)
    current_state = Current_State (previous_state,k, new_measure)
    current_error = Current_Estimative (previous_error, k )

    print([round(k,2),round(current_state,2),round(current_error,2)])
    
    previous_state = current_state
    previous_error = current_error

#end
