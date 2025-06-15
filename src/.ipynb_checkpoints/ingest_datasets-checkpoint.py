import pandas as pd
import csv

def loadCsv(filePath, fallbackSep=';', encoding='utf-8'):
    try:
        with open(filePath, 'r', encoding=encoding) as f:
            sample = f.read(2048)
            f.seek(0)
            try:
                dialect = csv.Sniffer().sniff(sample)
                separator = dialect.delimiter
            except csv.Error:
                separator = fallbackSep

        df = pd.read_csv(filePath, sep=separator, encoding=encoding)
        print(f"Loaded {filePath} with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df

    except FileNotFoundError:
        print(f"File not found: {filePath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading {filePath}: {str(e)}")
        return pd.DataFrame()
