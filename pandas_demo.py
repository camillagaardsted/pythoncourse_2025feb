# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:55:10 2024

@author: Camilla

Short demo of the pandas package 
A package in python where we work with data in something called a dataframe
"""

import pandas as pd

import matplotlib.pyplot as plt
filename=r'C:\PythonCourse225\MPF_subset_data.csv'
df=pd.read_csv(filename,header=[0,1])

df.columns=['Sol', 'LocalTime', 'DecimalSol', 'T1', 'T2','T3']


print('T1 mean',df.T1.mean())
print('T2 mean',df.T2.mean())
print('T3 mean',df.T3.mean())

df.hist()

df['T1']


plt.show()


# lunch until 12.45






