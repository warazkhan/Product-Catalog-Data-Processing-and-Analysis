import numpy as np
import pandas as pd
from config import badValues

def cleanBadValues(
    df: pd.DataFrame,
    badValuesList: list = badValues,
    objectColumns: list = None,
    numericColumns: list = None
) -> pd.DataFrame:

    foundBad = False
    if objectColumns is None:
        objectColumns = df.select_dtypes(include='object').columns.tolist()
    
    for col in objectColumns:
        df[col] = df[col].str.strip()
        if df[col].isin(badValuesList).any():
            foundBad = True
            df[col] = df[col].replace(badValuesList, np.nan)

    if numericColumns is None:
        numericColumns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    for col in numericColumns:
        if (df[col] == 0).any():
            foundBad = True
            df[col] = df[col].replace(0, np.nan)

    if foundBad:
        print("Bad values detected and replaced!")
    else:
        print("No bad values found!")

    return df

def dropRowsMissingKeys(df: pd.DataFrame, keyColumns: list) -> pd.DataFrame:
    df = df.dropna(subset=keyColumns)
    return df

def dropFullyNullColumns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(axis=1, how='all')
    return df