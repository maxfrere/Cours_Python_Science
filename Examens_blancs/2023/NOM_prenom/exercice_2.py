import numpy as np
import matplotlib.pyplot as plt

# Quesstion 1
x_array = np.arange(-10,10,0.1)

# Quesstion 2
def  function_exo2(x_array, a, b):
    return a*x_array**3+(1/(b*x_array))

# Quesstion 3

plt.figure()
plt.title("Graphique Exo 2 : courbe et  sa dérivé")
plt.plot(x_array,function_exo2(x_array, 5, 2), label="Courbe")
plt.xlabel("Absice x")
plt.ylabel("$f(x)=ax^3+\frac{1}{bx}$")
plt.xlim(-10,10)
plt.ylim(-40,40)
plt.grid()


# Question 4
def derivate_func_exo2(x_array, a, b):
    return 3*a*x_array**2-(1/(b*x_array**2))

plt.plot(x_array,derivate_func_exo2(x_array, 5, 2), label="Dérivé")
plt.legend()
plt.show()

# Question 5
plt.figure()
plt.title("Graphique Exo 2 : Variation de b")
b_array = np.arange(1,10,1)
for b_value in b_array:
    plt.plot(x_array,function_exo2(x_array, 2, b_value), label=f"b={b_value}")
plt.xlabel("Absice x")
plt.ylabel("$f(x)=ax^3+\frac{1}{bx}$")
plt.xlim(-10,10)
plt.ylim(-20,20)
plt.grid()


# Question 6
y_array = function_exo2(x_array, 2, 5)
start_idx = 80 # 10 par unité -2 est l'indice 10*8
end_idx = -80
y_array[start_idx:end_idx] = 5
plt.plot(x_array,y_array, label="valeur forcé")
plt.legend()
plt.show()
