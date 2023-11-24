#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import des librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Chargement des données
data = pd.read_csv("L3_TPE_data_clean.csv",index_col=0,header=0,infer_datetime_format=True)

# séparer le temps des valeurs
time_array = data.index.values
air_temperature_array = data["T_air"].values

# Question 1:


# Question 2:
#Solution Numpu


# Solution pandas élégante


# Question 3:

# Question 4:


# Question 5:

