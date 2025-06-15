import numpy as np
import logging
from config import manufacturersFile, productDescriptionsFile, productPropertiesFile, outputCleanedFile, badValues
from ingest_datasets import loadCsv
from clean import cleanBadValues, dropRowsMissingKeys, dropFullyNullColumns
from merge import mergeCatalogTables
from engineer import engineerFeatures
from analyze import describeDf, printDatasetInfo, getMissingValueReport, getDuplicateReport, describeNumerics
from visualize import plotCorrelationHeatmap, plotFrequencyGridSmart, plotBoxplotGrid

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def runPipeline(exportCleaned=True, visualMode=True):
    # Load raw datasets
    logger.info("Loading Manufacturers data...")
    manufacturersDf = loadCsv(manufacturersFile)
    printDatasetInfo(manufacturersDf)
    logger.info("Descriptive statistics:")
    logger.info(describeDf(manufacturersDf))

    logger.info("Loading Product Descriptions data...")
    productDescriptionsDf = loadCsv(productDescriptionsFile)
    printDatasetInfo(productDescriptionsDf)
    logger.info("Descriptive statistics:")
    logger.info(describeDf(productDescriptionsDf))

    logger.info("Loading Product Properties data...")
    productPropertiesDf = loadCsv(productPropertiesFile)
    printDatasetInfo(productPropertiesDf)
    logger.info("Descriptive statistics:")
    logger.info(describeDf(productPropertiesDf))

    # Drop rows with missing required join keys
    productPropertiesDf.dropna(subset=['Articlenumber', 'Manufacturernumber'], inplace=True)
    manufacturersDf.dropna(subset=['Manufacturernumber'], inplace=True)
    manufacturersDf = dropFullyNullColumns(manufacturersDf)
    productPropertiesDf = dropFullyNullColumns(productPropertiesDf)

    # Clean datasets
    logger.info("Cleaning Manufacturers data...")
    manufacturersDf = cleanBadValues(manufacturersDf, badValues)

    logger.info("Cleaning Product Descriptions data...")
    productDescriptionsDf = cleanBadValues(productDescriptionsDf, badValues)

    logger.info("Cleaning Product Properties data...")
    productPropertiesDf = cleanBadValues(productPropertiesDf, badValues)

    # Merge datasets
    logger.info("Merging datasets...")
    mergedDf = mergeCatalogTables(productDescriptionsDf, productPropertiesDf, manufacturersDf)

    # Feature engineering
    logger.info("Creating engineered features...")
    engineeredDf = engineerFeatures(mergedDf)

    # Analyze
    logger.info("Analyzing data...")
    printDatasetInfo(engineeredDf)

    logger.info("Missing value report:")
    logger.info("\n%s", getMissingValueReport(engineeredDf))

    dupCount, dupRows = getDuplicateReport(engineeredDf, ['Articlenumber'])
    logger.info(f"Duplicate Articlenumber count: {dupCount}")

    logger.info("Descriptive statistics (numeric columns):")
    logger.info("\n%s", describeNumerics(engineeredDf))

    # Visualize
    if visualMode:
        logger.info("Generating visualizations...")
        plotCorrelationHeatmap(engineeredDf)
        plotFrequencyGridSmart(engineeredDf, title="Frequencies and Distributions of Variables")
        plotBoxplotGrid(engineeredDf, title="Outliers Detection in Variables")

    # Export cleaned dataset
    if exportCleaned:
        logger.info(f"Exporting cleaned dataset to: {outputCleanedFile}")
        engineeredDf.to_csv(outputCleanedFile, index=False)

    logger.info("Pipeline execution completed successfully.")
    return engineeredDf