import numpy as np
import pandas as pd
import logging
from config import badValues

logging.basicConfig(
    level=logging.INFO,  
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

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
        logger.info("Bad values detected and replaced in the dataset.")
    else:
        logger.info("No bad values found in the dataset.")

    return df


def dropRowsMissingKeys(df: pd.DataFrame, keyColumns: list) -> pd.DataFrame:
    initial_shape = df.shape
    df = df.dropna(subset=keyColumns)
    dropped_rows = initial_shape[0] - df.shape[0]
    logger.info(f"Dropped {dropped_rows} rows missing required keys: {keyColumns}")
    return df


def dropFullyNullColumns(df: pd.DataFrame) -> pd.DataFrame:
    initial_cols = df.shape[1]
    df = df.dropna(axis=1, how='all')
    dropped_cols = initial_cols - df.shape[1]
    logger.info(f"Dropped {dropped_cols} fully null columns.")
    return df
