import numpy as np
from config import manufacturersFile, productDescriptionsFile, productPropertiesFile, outputCleanedFile
from ingest_datasets import loadCsv
from clean import cleanBadValues, dropRowsMissingKeys, dropFullyNullColumns
from merge import mergeCatalogTables
from engineer import engineerFeatures
from analyze import describeDf, printDatasetInfo, getMissingValueReport, getDuplicateReport, describeNumerics
from visualize import plotCorrelationHeatmap, plotFrequencyGridSmart, plotBoxplotGrid

badValues = ["None", "none", "null", "Null", "n/a", "N/A", "NA", "", " ", "-", "--", "'", "undefined", "missing", "<blank>", "???", "\n", "\t"]

def runPipeline(exportCleaned=True, visualMode=True):
    
    # Load raw datasets
    print("\nLoading Manufacturers data...")
    manufacturersDf = loadCsv(manufacturersFile)
    printDatasetInfo(manufacturersDf)
    print("\nDescriptive Statics...")
    print(describeDf(manufacturersDf))
    
    print("\nLoading Product Descriptions data...")
    productDescriptionsDf = loadCsv(productDescriptionsFile)
    printDatasetInfo(productDescriptionsDf)
    print("\nLoading Product Properties data...")
    productPropertiesDf = loadCsv(productPropertiesFile)
    printDatasetInfo(productPropertiesDf)

    # Drop rows with missing required join keys
    productPropertiesDf.dropna(subset=['Articlenumber', 'Manufacturernumber'], inplace=True)
    manufacturersDf.dropna(subset=['Manufacturernumber'], inplace=True)
    manufacturersDf = dropFullyNullColumns(manufacturersDf)
    productPropertiesDf = dropFullyNullColumns(productPropertiesDf)

    # Clean datasets
    print("\nCleaning Manufacturers data...")
    manufacturersDf = cleanBadValues(manufacturersDf, badValues)
    print("\nCleaning Product Descriptions data...")
    productDescriptionsDf = cleanBadValues(productDescriptionsDf, badValues)
    print("\nCleaning Product Properties data...")
    productPropertiesDf = cleanBadValues(productPropertiesDf, badValues)
    
    # Merge datasets
    print("\nMerging Manufacturers data, Product Descriptions data and Product Properties data...")
    mergedDf = mergeCatalogTables(productDescriptionsDf, productPropertiesDf, manufacturersDf)

    # Feature engineering
    print("\nCreating engineered features...")
    engineeredDf = engineerFeatures(mergedDf)

    # Analyze
    print("\nAnalyzing data...")
    printDatasetInfo(mergedDf)
    print("\nMissing Values in dataset...")
    print(getMissingValueReport(engineeredDf))
    dupCount, dupRows = getDuplicateReport(engineeredDf, ['Articlenumber'])
    print(f"\nDuplicate Articlenumber count: {dupCount}")
    print("\nDescriptive Statics...")
    print(describeNumerics(engineeredDf))

    # Visualize
    if visualMode:
        print("\nVisualizing data...")
        plotCorrelationHeatmap(engineeredDf)
        plotFrequencyGridSmart(engineeredDf, title="Frequencies and Distributions of Variables")
        plotBoxplotGrid(engineeredDf, title="Outliers Detection in Variables")
        
    # Export cleaned dataset
    if exportCleaned:
        print(f"\nExporting cleaned dataset to: {outputCleanedFile}")
        engineeredDf.to_csv(outputCleanedFile, index=False)

    print("\nPipeline execution completed successfully")
    return engineeredDf