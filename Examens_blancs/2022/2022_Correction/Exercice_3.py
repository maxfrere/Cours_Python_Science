0#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import des librairies
import numpy as np
import matplotlib.pyplot as plt


# Question 2 :
def derive_u(value_u, tau,e):
    return value_u*(-1/tau)+e/tau

def derive_u(value_u,value_t, tau,e,eps):
    return value_u*(-1/(eps*tau*value_t))+e/(tau*value_t)

# Question 3 :
def euler_explicite(derive,
                    initial_y_value,initial_x_value,
                    dx,final_time,
                    tau, e):
    array_x=np.arange(initial_x_value,final_time,dx)
    array_y=np.zeros(len(array_x))
    array_y[0]=initial_y_value
    for idx,value_x in enumerate(array_x[:-1]):
        value_y  =array_y[idx]
        array_y[idx+1]= array_y[idx] + derive(value_y,value_x,tau,e,0.01)
    return array_x,array_y

# Question 4 :
figure = plt.figure()
plt.title("Circuit RC")
list_dx=[0.1,0.01,0.001]
final_time=2
for value_dx in list_dx:
    time_array,value_array = euler_explicite(derive_u,
                                             5,1
                                             ,value_dx,final_time,
                                             57,20)
    plt.plot(time_array, value_array, label=f"dx = {value_dx}")


plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()
