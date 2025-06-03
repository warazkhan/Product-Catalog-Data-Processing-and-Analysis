# File paths
manufacturersFile = '../data/manufacturers.csv'
productDescriptionsFile = '../data/product_descriptions.csv'
productPropertiesFile = '../data/product_properties.csv'
outputCleanedFile = '../data/product_catalog_cleaned.csv'

# List of bad values to normalize to NaN
badValues = ["None", "none", "null", "Null", "n/a", "N/A", "NA", "", " ", "-", "--", "'", "undefined", "missing", "<blank>", "???", "\n", "\t"]