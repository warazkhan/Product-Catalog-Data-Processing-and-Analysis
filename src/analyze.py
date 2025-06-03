def printDatasetInfo(df):
    return df.info()
    
def getMissingValueReport(df):
    return df.isnull().sum().sort_values(ascending=False)

def getDuplicateReport(df, subsetCols):
    duplicateCount = df.duplicated(subset=subsetCols).sum()
    duplicateRows = df[df.duplicated(subset=subsetCols, keep=False)]
    return duplicateCount, duplicateRows

def describeDf(df):
    return df.describe()

def describeNumerics(df):
    numericData = df.select_dtypes(include='number').columns.tolist()
    dfDescriptiveStatics = df[numericData].describe().T
    dfDescriptiveStatics['median'] = df[numericData].median().T
    dfDescriptiveStatics['mode'] = df[numericData].mode().iloc[0]
    dfDescriptiveStatics['range'] = (dfDescriptiveStatics['max'] - dfDescriptiveStatics['min']).T
    return dfDescriptiveStatics