# Product Catalog Data Processing & Analysis

This repository contains a comprehensive project focused on data cleaning, analysis, and visualization of a product catalog dataset. It demonstrates skills in Python data engineering, SQL-style querying on pandas DataFrames, and dashboard creation with Power BI.

---

## Project Overview

This project involves:

- Downloading and exploring raw product and manufacturer data  
- Cleaning and normalizing datasets with Python and pandas  
- Performing SQL-style analysis on data using pandasql  
- Creating a Power BI dashboard to visualize key insights  

---

## How to Reproduce

### 1. Clone or Download the Repository

Download the repository as a ZIP file and extract it, or clone it using Git:

```bash 
git clone https://github.com/warazkhan/Product-Catalog-Data-Processing-and-Analysis.git
```

### 2. Install Python Dependencies with Poetry

This project uses Poetry for dependency management.

If you don’t have Poetry installed:
```bash
pip install poetry
```
Then install the dependencies:
```bash
poetry install
```
If you're using Jupyter notebooks, you can activate the Poetry environment as a kernel:
```bash
poetry shell
python -m ipykernel install --user --name=product-catalog --display-name "Python (Product Catalog)"
```

### 3. Run the Data Pipeline

Open and run the notebook:

```bash
notebooks/data_pipeline.ipynb
```

This notebook loads raw data from the `data/` folder, performs cleaning and normalization, feature engineering, analysis, and visualization. It also exports a cleaned dataset (`product_catalog_cleaned.csv`).

Alternatively, run the full pipeline from the entry script:
```bash
poetry run python src/main.py
```

### 4. Perform SQL Analysis

Open and run:
```bash
notebooks/product_catalog_sql_analysis.ipynb
```


This notebook executes SQL queries on the cleaned dataset using pandasql and presents the analysis results.

### 5. View Power BI Dashboard

Open:
```bash
dashboard/product_catalog_dashboard.pbix
```


in Power BI Desktop. If prompted, point the data source to your local `data/product_catalog_cleaned.csv`.

---

## Repository Contents

| File/Folder                                            | Description                                                    |
| ------------------------------------------------------ | -------------------------------------------------------------- |
| `dashboard/product_catalog_dashboard.pbix`             | Power BI dashboard file summarizing key project insights        |
| `data/`                                                | Folder containing raw and cleaned CSV datasets                 |
| `notebooks/data_pipeline.ipynb` | Notebook for pipeline exploration, quick stats, visualizations |
| `notebooks/product_catalog_sql_analysis.ipynb`         | Notebook demonstrating SQL analysis using pandasql             |
| `notebooks/pandas_sql_sample.ipynb`                    | Sample notebook showing pandasql usage                         |
| `src/`                                                 | Modular Python source code for pipeline components             |
| `src/main.py`                                          | Entry point script to run the full data processing pipeline    |
| `pyproject.toml`                                       | Poetry configuration and dependency file                      |
| `poetry.lock`                                          | Locked versions of installed dependencies                      |
| `.gitignore`                                           | Git ignore configuration file                                 |
| `README.md`                                            | This project documentation                                    |

---

## Project Approach

- **Data Processing:** Python scripts in the `src/` folder perform data ingestion, cleaning, merging, feature engineering, and analysis.
- **SQL Analysis:** Uses pandasql to execute SQL queries on pandas DataFrames within notebooks for flexible analysis.
- **Visualization:** Seaborn and Matplotlib are used for Python visualizations, complemented by a Power BI dashboard for a business-friendly summary.

---

## Production Considerations

To make this project production-ready, consider adding:

- Automate data ingestion with scheduled ETL pipelines.
- Add comprehensive unit and integration testing.
- Integrate logging with monitoring and alerting systems.
- Implement CI/CD pipelines for smooth deployment.
- Use secure and centralized data storage (cloud or API-based).
- Consider containerization (e.g., Docker) for environment consistency.
---

![image](https://github.com/user-attachments/assets/c2b7c7d3-1b4d-4b68-969c-ae114391abe4)


**Thank you for exploring this project!**
