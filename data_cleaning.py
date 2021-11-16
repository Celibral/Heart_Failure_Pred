# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df = pd.read_csv("C:/Users/no1ca/Documents/heart_failure_pred/heart.csv")


#remove entities with no restingBP
df = df[df.RestingBP != 0]
#remove entities with no Cholesterol
df = df[df.Cholesterol != 0]

df.to_csv("heart_cleaned.csv")