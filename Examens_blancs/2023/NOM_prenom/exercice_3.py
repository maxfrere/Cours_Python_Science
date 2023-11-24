# Question 1
import numpy as np

temperature_array = np.fromfile("temperature_array.dat")
time_array = np.fromfile("time_array_min.dat")

# Question 2
plt.figure()
plt.title("Graphique Exo 3 : question 1")
plt.plot(temperature_array, label="Température")
plt.xlabel("Temps (min)")
plt.ylabel("température (°C)")
plt.grid()

# Question 3
maximum = temperature_array.max()
minimim = temperature_array.min()
loc_max = np.where(temperature_array==maximum)[0][0]
loc_min = np.where(temperature_array==minimim)[0][0]
print(f"Maximum : {maximum} à {loc_max} minutes,\nMinimum : {minimim} à {loc_min} minutes,\n")

# Question 4
moyenne = temperature_array.mean()
deviation = temperature_array.std()
print(f"Valeur moyenne sur la journé : {round(moyenne,3)} avec une déviation standard : {round(deviation,3)}")

# Question 5
def integral(temperature_array):
    int_sum=0
    for idx, value in enumerate(temperature_array[:-1]):
        int_sum+= 60*((value+temperature_array[idx+1])/2) #Attention dx est de 60 secondes
    return int_sum

print(f"Intégral de {integral(temperature_array)} °C.s")
