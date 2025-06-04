import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

def printBasicInfo(df: pd.DataFrame, dfName: str) -> None:
    logger.info(f"Dataset '{dfName}' contains {df.shape[0]} rows and {df.shape[1]} columns.")
    buffer = []
    df.info(buf=buffer := [])
    for line in buffer:
        logger.info(line)
    logger.info("")


def checkMissingValues(df: pd.DataFrame) -> pd.Series:
    missing = df.isnull().sum()
    logger.info("Missing values per column:\n%s", missing[missing > 0])
    return missing


def checkDuplicates(df: pd.DataFrame, subsetCols: list) -> int:
    dupCount = df.duplicated(subset=subsetCols).sum()
    if dupCount > 0:
        logger.warning(f"Found {dupCount} duplicate rows based on columns: {subsetCols}")
    else:
        logger.info("No duplicates found.")
    return dupCount


def describeNumeric(df: pd.DataFrame) -> pd.DataFrame:
    desc = df.describe()
    logger.info("Descriptive statistics:\n%s", desc)
    return desc