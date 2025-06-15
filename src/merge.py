import pandas as pd

def mergeCatalogTables(productDescriptionsDf, productPropertiesDf, manufacturersDf):
    mergedDf = pd.merge(productDescriptionsDf, productPropertiesDf, on='Articlenumber', how='inner')
    mergedDf = pd.merge(mergedDf, manufacturersDf, on='Manufacturernumber', how='inner')
    return mergedDf