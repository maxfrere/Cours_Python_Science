#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import des librairies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Chargement des données
data = pd.read_csv("RH_data_clean.csv",index_col=0,header=0,infer_datetime_format=True)

# separer le temps des valeurs
time_array = data.index.values
RH_array = data["RH"].values


