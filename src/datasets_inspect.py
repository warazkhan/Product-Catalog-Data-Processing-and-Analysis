import pandas as pd

def printBasicInfo(df: pd.DataFrame, dfName: str) -> None:
    print(f"Dataset '{dfName}' contains {df.shape[0]} rows and {df.shape[1]} columns.\n")
    print(df.info())
    print("\n")

def checkMissingValues(df: pd.DataFrame) -> pd.Series:
    return df.isnull().sum()

def checkDuplicates(df: pd.DataFrame, subsetCols: list) -> int:
    return df.duplicated(subset=subsetCols).sum()

def describeNumeric(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe()