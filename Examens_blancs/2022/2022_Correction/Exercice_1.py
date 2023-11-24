#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import des librairies
import numpy as np
import matplotlib.pyplot as plt

# Question 1:
time_array = np.arange(0,2,0.001)

# Question 2 :
def exp_1(time_array,A,tau):
    result = (1-A)*np.exp(-time_array/tau)
    return result

# Question 3 :
# Solution basique
exp_array_1 = exp_1(time_array,2,0.2)
exp_array_2 = exp_1(time_array,5,0.2)
exp_array_3 = exp_1(time_array,2,0.05)
exp_array_4 = exp_1(time_array,5,0.05)

# Solution élégante
list_couple = [(2,0.2),(5,0.2),(2,0.05),(5,0.05)]
list_of_array = []
for value in list_couple:
    list_of_array.append(exp_1(time_array,value[0],value[1]))

# Question 4 :
# Solution basique
figure = plt.figure()
plt.title("Refroidisssement thermique (basique)")
plt.plot(time_array,exp_array_1,label=u"A=2,$tau$=0.1")
plt.plot(time_array,exp_array_2,label=u"A=5,$tau$=0.01")
plt.plot(time_array,exp_array_3,label=u"A=2,$tau$=0.1")
plt.plot(time_array,exp_array_4,label=u"A=5,$tau$=0.01")
plt.legend()
plt.grid()
plt.show() # Attention ce dernier met en pause le programe tant que pas fermer usuelement a metttre à la toute fin du script

# Solution élégante
figure = plt.figure()
plt.title("Refroidisssement thermique (élégant)")
for idx,value in enumerate(list_couple):
    plt.plot(time_array, list_of_array[idx], label=f"A={value[0]},$tau$={value[1]}")
plt.legend()
plt.grid()

