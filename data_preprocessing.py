# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:18:05 2019

@author: acer
"""

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as pyt


#getting the data from the file 

#IMPORTANT NOTE RAINFALL_MAIN_CSV HAS  DATA OF DENGUE CASES AS WELL
rainfall_filename = "__rainfall_main.csv"
rainfall = pd.read_csv(rainfall_filename)

temp_filename = "temp_India_1901_2016_main.csv"
temp = pd.read_csv(temp_filename)

pop_den_filename = "population_density_main.csv"
pop_den = pd.read_csv(pop_den_filename)


combine = pd.concat([rainfall.iloc[0:,0:2] ,rainfall.iloc[0:,14:]],axis=1)

temp = temp.iloc[0:,13:]
temp.rename(columns={"ANNUAL":"ANNUAL_TEMP"})

repeat = temp 

for i in range(35):
    repeat = repeat.append(temp,ignore_index=True)  


#rainfall and temperature AND DENGUE CASES   4212 rows x 13 columns
combine = pd.concat([combine,repeat],axis=1)

#COMBINE = RAINFALL AND TEMPERATURE AND DENGUE 
#POP_DEN = SEX RATIO AND POPULATION DENSITY STATE WISE IN DIFFERENT REGIONS 


