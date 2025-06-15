import pandas as pd
import numpy as np

def calculateProductVolume(df, depthCol='Depth m', widthCol='Width m', lengthCol='Length m'):
    df['Volume_m3'] = df[depthCol] * df[widthCol] * df[lengthCol]
    return df

def categorizeLength(df, lengthCol='Length m'):
    bins=[0, 0.3, 0.5, 1.0]
    labels=['Small', 'Medium', 'Large']
    df['Product_length_category'] = pd.cut(df[lengthCol], bins=bins, labels=labels)
    return df

def engineerFeatures(df):
    df = calculateProductVolume(df)
    df = categorizeLength(df)
    return df