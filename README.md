# Take home assignment

Welcome to the nexMart take home assignment for the **Data Analyst** role!

![DA image](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2M1cGZidjQwNTVmdWVjY3hraGFpMXN4djRzN3hvcTE2cjNldGVkaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JWuBH9rCO2uZuHBFpm/giphy.gif)

nexMart as a company enables the digitalisation of the hardware and industrial supply sector by providing a comprehensive range of data services to manufacturers and retailers. To do so, a lot of external input data needs to be ingested, transformed and delivered. One process step in this chain of operations is to handle and analyse a variety of data formats and contents.

As the second step in the interview process for this role, we kindly ask you to take on a coding assignment plus some related questions and submit it to us for review.

The coding assignment consists of 3 main parts:

1. Data Processing with Python + Pandas or PySpark
2. Data Analysis with SQL
3. Data Visualization with Power BI

## Instructions

> Important ⚠️
>
> The deliverable must be in English. We know candidates might speak other languages (which is awesome!), but to keep things simple for the reviewers, let's stick to good old English here.

- Download the files from this repo's data folder
- Create your own private project repo on GitHub with the downloaded data
- Work on the assignment. Please make sure to balance your efforts between the 3 parts (ex. avoid using Power BI for the data pipeline, or precomputing SQL questions using pandas, leaving the SQL part as a simple `SELECT * FROM X`...)
- The solution needs to be reproducible locally on our side. Please make sure to include all necessary files & instructions to be able to do so
- Once you are satisfied with your solution, please give the `nxcodingassignment` GitHub user access to your repo and notify us (email below) about your submission

## Deliverable expectations

- A `README.md` file with clear instructions on how to reproduce your solution of the coding assignment
- A data pipeline using Pandas or PySpark in a functionalized Python script
  - [optional] Use of PEP8 standard is a plus
- SQL queries that answer the questions listed below, their results and small explanations about the obtained output
- A Power BI file (`.pbix`) for a one-pager dashboard
- The dependency management is taken care of (ex. `requirements.txt` or `pyproject.toml`)
- [optional] Bonus question answered is considered a plus

## Assignment

"Studies show that a 10% improvement in data quality can lead to a 5-10% increase in sales".

Based on this statement, you are asked to conduct an analysis of our product catalog data. Your objective is to prove to our internal business stakeholders that our customers (manufacturers/retailers) would benefit from an improvement in their data quality, using the provided catalog data (located in the [data](/data/) directory)

> Note :notebook:
>
> To avoid any confusion on the terms of "good" or "bad" data quality for this assignment, consider that any sensible information brings value, regardless of the format and length.
> Examples:
>
> - product short description: "screwdriver 10mm, round head, 20cm" (data quality is "good")
> - product short description: "screwdriver" (data quality is "good")
> - product short description: `null` (data quality is "bad")
> - product short description: "N/A" (data quality is "bad")

For this task, you will have 3 CSV files from [ampshare](https://ampshare.com/de/de/produktkatalog/) (located in the [data](/data/) directory) to run your analysis:

- product_descriptions: contains the product descriptions (multilanguage)
- product_properties: contains the product properties
- manufacturers: contains the manufacturer's information (id and name)

Be aware that the data was directly exported from a legacy system setup with a live database. So, it is raw and you may find some inconsistencies. Therefore, you will also need to do some data cleaning before starting the analysis.

### 1) Python + Pandas or PySpark

In this section, you shall create a data pipeline to clean, standardize the schema and format the data (if necessary) to the format that you think is best for the analysis. You can use either Pandas or PySpark to do so.

Here is some important info:

- columns used to join tables are a must, all records that contain `null` values on these columns must be discarded from the analysis
  - product_descriptions: `Articlenumber`
  - product_properties: `Manufacturernumber`, `Articlenumber`
  - manufacturers: `Manufacturernumber`
- bad quality data should be normalized (to `null`), ex. `N/A`, `None`, `'`, etc.

### 2) SQL

In this section, you shall use SQL to answer the following questions:

- Which manufacturers have the biggest improvement potential in their data quality in absolute and relative numbers?
- What product variable/column (description or property) usually contains data of good quality per manufacturer? And what is the % of good quality records per variable/column and manufacturer?
- Which other interesting insights did you find? Please give us a short explanation together with the SQL statement used to retrieve it.

> Note :notebook:
>
> As long as your solution is reproducible and the execution steps are clear and documented, you can use any tool or technology to run your SQL queries. If you do not have any preference, we recommend using `pandasql` for querying directly the `pandas` dataframes (sample notebook [here](notebooks/pandasql_sample.ipynb)) or [Spark temporary views](https://spark.apache.org/docs/3.5.5/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.createOrReplaceTempView.html) if you chose `PySpark`.

### 3) Power BI

In this section, you shall create a dashboard in Power BI. This part is open to your creativity, you can develop any visualization that you think is relevant for the analysis. The only requirements for this part are:

- The dashboard must consist of only one page
- The data used in the dashboard must be the output of the data pipeline from the first part of the assignment
- Your audience will be composed of business users and technical users. Make sure to create a dashboard that is easy to understand and that provides insights to both audiences

The Power BI file must be submitted to the repository with the rest of the code. Additionally, you shall give a short dashboard presentation of max. 10 minutes during the technical interview. 

## Bonus question

If this assignment was part of a real project, what modules/steps/pieces are missing in your deliverable that would be necessary for a production environment?

## Last notes

As this is a selection process exercise, we do not expect a full-blown solution to save the candidate’s time. That being said, it is important for us to see notions to evaluate the seniority of the candidate, which means we expect code of basic production quality (not MVP standard, ex. leave out unit testing). Evaluation criteria include the compliance with the delivery expectations, logical thinking, code and documentation quality.

Any technical questions regarding the assignment can be submitted to this email address: <coding.assignment@nexmart.com>. For all other questions, please refer to your recruiter contact.
