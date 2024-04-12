# assignment5_data_pipline_ind
# Abigail Akua Sika Boateng

# Data Pipeline Readme

## Table of Contents
- [Overview](#overview)
- [Necessary Libraries, Tools, and Frameworks](#necessary-libraries-tools-and-frameworks)
- [Data Ingestion and Schema Evolution](#data-ingestion-and-schema-evolution)
- [Incremental Updates](#incremental-updates)
- [Data Transformation](#data-transformation)
- [Scalability and Parallel Processing](#scalability-and-parallel-processing)
- [Data Storage](#data-storage)
- [Fault Tolerance](#fault-tolerance)
- [Documentation](#documentation)
- [Running the Pipeline](#running-the-pipeline)
- [Maintaining the Pipeline](#maintaining-the-pipeline)

## Overview
This document outlines the design and implementation of a data pipeline for processing and managing data from CSV and JSON files. The pipeline is built to handle various requirements, including data ingestion, schema evolution, incremental updates, data transformation, scalability, fault tolerance, and documentation.

## Necessary Libraries, Tools, and Frameworks
- **Python**: Programming language used for scripting and data manipulation.
- **Pandas**: Python library for data manipulation and analysis, used for handling CSV and JSON files and performing data transformations.
- **MySQL**: Relational database management system used for storing the processed data.
- **MySQL Connector**: Python library for connecting to MySQL from Python scripts.
- **Git**: Version control system used for managing project codebase.
- **Markdown**: Lightweight markup language used for writing documentation.

## Data Ingestion and Schema Evolution
- Implemented a data ingestion mechanism using Python scripts and Pandas library to load data from both CSV and JSON files.
- Handled schema evolution scenarios by dynamically generating SQL statements to create tables based on the data schema.

## Incremental Updates
- Designed the pipeline to support incremental updates using Python scripts and Pandas library, allowing it to process only new or modified records since the last execution.
- Considered scenarios where data is continuously updated, ensuring efficient processing without reprocessing already processed data.

## Data Transformation
- Utilized Pandas library for data transformations, enriching orders and delivery data with user information and calculating aggregate metrics such as total transaction amount per user. 

## Scalability 
- Designed the pipeline to be scalable making the pipeline efficient in managing growing data and processes
 
## Data Storage
- Chose MySQL as the database solution to store the processed data due to its scalability,  data structure, and query requirements.
- Implemented the storage mechanism using MySQL Connector library for efficient retrieval and querying of the data.

## Fault Tolerance
- Implemented fault-tolerant mechanisms within the Python scripts to handle failures during data processing
- Ensured the pipeline can recover gracefully from errors without losing processed data, providing robustness and reliability.

## Documentation
- Includes instructions on how to run and maintain the pipeline, ensuring ease of use and maintenance for future development.

## Running the Pipeline
## Prerequisites
- Python
- Pandas
- MySQL
- Necessary libraries

## Steps

1. **Clone the Repository**
   - Clone the repository containing the data pipeline scripts to your local machine.

2. **Execute Data Preparation Scripts**
   - Run the respective `.ipynb` files to update the CSV files with the latest data and save them.

3. **Update MySQL Connection Parameters**
   - Open the `import.py` and `import2.py` scripts for market1 and market2, respectively.
   - Update the MySQL connection parameters to match your MySQL server configuration.

4. **Establish MySQL Connection**
   - Open your terminal or command prompt.
   - Run the following command to establish a connection to the MySQL database:
     ```
     mysql -u username -p database_name < script_file.sql
     ```
     Replace `username`, `database_name`, and `script_file.sql` with the appropriate values.

5. **Execute Database Schema Script**
   - Run the script to build and model the data schema in MySQL.
   - This script will create the necessary tables and define their structure.

6. **Run Data Ingestion Scripts**
   - Execute the `import.py` and `import2.py` scripts to ingest data into MySQL from the updated CSV and JSON files.
   - These scripts will import the data into the corresponding tables in the database.

7. **Monitor Execution**
   - Monitor the execution of the pipeline and handle any errors or exceptions gracefully.
   - Ensure that the data ingestion process completes successfully without any issues.


## Maintaining the Pipeline
- Regularly monitor data ingestion and processing to ensure smooth operation.
- Handle any changes in data schema or requirements by updating the pipeline accordingly.
- Continuously optimize the pipeline for performance, scalability, and reliability based on evolving needs.
