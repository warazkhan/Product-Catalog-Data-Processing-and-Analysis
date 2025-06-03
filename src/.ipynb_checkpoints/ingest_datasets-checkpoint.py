import pandas as pd

def loadCsv(filePath, separator=';'):

    try:
        df = pd.read_csv(filePath, sep=separator)
        print(f"Loaded {filePath} with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print(f"File not found: {filePath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading {filePath}: {str(e)}")
        return pd.DataFrame()
