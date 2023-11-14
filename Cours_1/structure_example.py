#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Short descriptive sentance.
"""

### Import Space ###

import numpy as np
import matplotlib.pyplot as plt

### Global Var/stat ###

SIGMA = 5.67037e-8 #W/m²K**4

### Function/Class Space ###

def Flux_radiative_from_temperature(temperature,emissivity=1):
    """Will compute the radiative flux from black body law

    Args:
        temperature (array): The given temperature in Kelvin
        emissivity (array): The emissivity of the surface

    Returns:
        flux (array): The resulting radiative flux (W)
    """

    flux = SIGMA*emissivity*temperature**4
    return flux

### Running Script Space ###

if __name__ == '__main__':
    array_temperature = np.arange(300,500,1)

    figure = plt.figure()
    plt.title("Flux d'émission d'un corps noir")
    plt.plot(array_temperature,
             Flux_radiative_from_temperature(array_temperature),
             label="Corps noir")
    plt.xlabel("Température (K)")
    plt.ylabel("Flux radiatif (W)")
    plt.grid()
    plt.show()