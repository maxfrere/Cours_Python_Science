import numpy as np
import matplotlib.pyplot as plt

# Question 1
def euler_explicite(derive,
                    initial_x_value,initial_y_value,
                    dx,final_time):
    array_x=np.arange(initial_x_value,final_time,dx)
    array_y=np.zeros(len(array_x))
    array_y[0]=initial_y_value
    for idx,value_x in enumerate(array_x[:-1]):
        value_y  =array_y[idx]
        array_y[idx+1]= array_y[idx] + derive(value_x,value_y)
    return array_x,array_y

#  Question 2
def derive(x,y):
    return np.cos(np.exp(-x/6))/12-(1/2*y)

#  Question 3
dx_array = [0.01,0.1,0.1,1]
x_0 = 5
y_0 = 25
final_time = 10

plt.figure()
plt.title("Résolution EDO")
for value in dx_array:
    x_array, y_array = euler_explicite(derive,
                            x_0,y_0,
                            value,final_time)
    plt.plot(x_array, y_array,label=f"dx={value}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
