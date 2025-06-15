# File paths
manufacturersFile = '../data/manufacturers.csv'
productDescriptionsFile = '../data/product_descriptions.csv'
productPropertiesFile = '../data/product_properties.csv'
outputCleanedFile = '../data/product_catalog_cleaned.csv'

# List of bad values to normalize to NaN
badValues = ["None", "none", "null", "Null", "n/a", "N/A", "", " ", "-", "--", "'", "undefined", "missing", "<blank>", "???", "\n", "\t"]
numericColumnsWithZeroAsNA = ['Depth m', 'Width m', 'Length m', 'Weight kg']