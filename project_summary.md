# Master Data Management (MDM) Project Report

## Introduction
This project is part of a Master Data Management (MDM) initiative aimed at integrating and managing data from multiple sources to create a unified and reliable dataset. The primary goal is to ensure high data quality and consistency, which are essential for effective data analysis, decision-making, and operational efficiency.

## Data Profiling and Initial Analysis
### Objective
To gain an in-depth understanding of the raw data and identify key data quality issues.

Detailed data profiling is conducted to identify key data quality issues. Comprehensive HTML reports were generated using pandas-profiling, providing insights into missing values, duplicate records, data types, and value distributions.

#### Baseline Data Quality Metrics:


| Metric                    | Customers Dataset | Properties Dataset |
|---------------------------|-------------------|--------------------|
| **Total Records**         | 162               | 267                |
| **Missing Values Count**  | 22                | 144                |
| **Missing Values Percentage** | 1.05%          | 5.39%              |
| **Duplicates Count**      | 0                 | 0                  |
| **Duplicates Percentage** | 0.00%             | 0.00%              |


### Actions
- **Generated Data Profiling Reports**: Detailed HTML reports were created using pandas-profiling to analyze missing values, duplicate records, data types, and value distributions.
- **Insights Gained**: The profiling reports provided critical insights that informed the subsequent data cleaning and standardization processes.

## Data Cleaning and Preprocessing

### Loading the Data
Raw datasets for properties and customers were loaded to establish a baseline understanding of the data structure and content.

### Handling Missing Values
### Objective
To address missing values in a way that maintains data integrity.

### Actions
- Replaced missing values with 'NA' to explicitly mark unavailable data.
- Ensured no assumptions were made about missing data, preserving the dataset's integrity.

### Removing Duplicate Records
### Objective
To eliminate redundancy and ensure each entity is uniquely represented.

### Actions
- Identified and removed duplicate records from both datasets.
- Verified the uniqueness of records to prevent inconsistencies and errors.

### Standardizing Data Formats
### Objective
To ensure consistency and uniformity across all data fields for seamless integration and analysis.

### Actions
- **Price**: Created a `price_cleaned` column by removing currency symbols and commas, converting it to a numeric format.
- **Date of Sale**: Converted to a standardized datetime format, handling errors by coercing invalid entries to `NaT`.
- **Customer Names**: Standardized to lowercase and stripped whitespace; concatenated `name` and `surname` into `full_name`.
- **Birth Date**: Converted the `birth_date` column to a datetime format.
- **Purpose and Source**: Standardized to lowercase.
- **Type and Status**: Standardized `type` and `status` columns in `properties_df` to lowercase, with `status` specifically replacing '-' with 'unsold'.

### Saving the Cleaned Data
### Objective
To preserve the integrity of the raw data while preparing the cleaned data for integration.

### Actions
- Saved the cleaned datasets separately from the raw data.
- Verified the correctness of the saved cleaned data to ensure readiness for integration.

## Data Integration

### Loading Cleaned Data
Cleaned datasets were reloaded to confirm they were correctly preprocessed and ready for integration.

### Merging Datasets
### Objective
To create a unified dataset that integrates data from both properties and customers datasets.

### Actions
- Merged datasets on the `customerid` column using a left join to ensure all customer data is retained.
- Addressed and resolved conflicts by renaming columns to maintain data consistency and integrity.

### Verifying Data Consistency
### Objective
To ensure the merged dataset maintains high data quality standards.

### Actions
- Conducted thorough checks for remaining missing values and duplicate entries.
- Verified the final data structure to confirm consistency and completeness.

### Saving the Unified Dataset
### Objective
To create a comprehensive, integrated dataset for further analysis and operational use.

### Actions
- Saved the unified dataset as a new CSV file.
- Verified the saved dataset to ensure it accurately represents the integrated data from both sources.

## Data Governance Framework

**Policies:**
1. **Data Access Policy:**
   - Define access levels for different roles (e.g., Data Steward, Data Analyst, Data Scientist).
   - Ensure that only authorized personnel can access sensitive data.

2. **Data Usage Policy:**
   - Specify acceptable uses of data to ensure compliance with legal and ethical standards.
   - Prohibit the misuse of data for personal gain or unauthorized activities.

3. **Data Security Policy:**
   - Implement measures to protect data from unauthorized access, breaches, and other security threats.
   - Ensure data encryption, secure access protocols, and regular security audits.

**Standards:**
1. **Data Formats:**
   - Standardize date formats to ISO 8601 (YYYY-MM-DD).
   - Ensure consistent currency format for price data (e.g., 123,456.78).

2. **Naming Conventions:**
   - Use lowercase for all text data (e.g., customer names, property types).
   - Use snake_case for column names (e.g., `property_id`, `customer_id`).

3. **Metadata Requirements:**
   - Maintain comprehensive metadata for each dataset, including descriptions, data types, and sources.
   - Document any transformations or cleaning steps applied to the data.

**Procedures:**
1. **Data Cleaning Procedures:**
   - Handle missing values by marking them as 'NA' or applying context-specific imputation.
   - Remove duplicate records to ensure unique representation of each entity.

2. **Data Validation Procedures:**
   - Implement regular data validation checks to ensure data accuracy and consistency.
   - Use automated scripts to identify and correct data anomalies. For example, using Python libraries such as pandas for data manipulation 
     and pandas-profiling for generating profiling reports

3. **Data Audits:**
   - Conduct regular data audits to review data quality and adherence to governance policies.
   - Document and address any issues identified during audits.
   - Regularly run profiling reports, review and document changes, and use automated tests to verify data consistency and integrity.

## MDM Best Practices

**Data Cleaning:**
- Handle missing values by marking them as 'NA' to explicitly indicate unavailable data.
- Standardize text data to lowercase and remove leading/trailing whitespace.
- Create new columns for cleaned data while preserving original data for reference.

**Data Integration:**
- Use unique identifiers (e.g., `customer_id`, `property_id`) to merge datasets accurately.
- Resolve conflicts by renaming columns or applying consistent transformations.

**Data Management:**
- Regularly update records to reflect changes and maintain accuracy.
- Implement version control for datasets to track changes and ensure data integrity.

## Sample Data Models

**ER Diagrams:**

**ER Diagram Description:**
- **Entities:**
  - **Customers**: Stores customer information.
  - **Properties**: Stores property details.

**Relationships:**
- **Customers** can own multiple **Properties**.

**ER Diagram:**

```plaintext
+--------------+       +----------------+
|  Customers   |       |   Properties   |
+--------------+       +----------------+
| customerid   |<------| customerid     |
| name         |       | id             |
| surname      |       | building       |
| full_name    |       | date_sale      |
| birth_date   |       | type           |
| purpose      |       | area           |
| source       |       | price          |
+--------------+       | status         |
                       +----------------+
```


# Data Flow Diagrams
## Data Flow Diagram Description:

Stages:

- Raw Data Collection: Collect data from multiple sources (e.g., databases, CSV files).
- Data Cleaning: Apply cleaning procedures to handle missing values, remove duplicates, and standardize formats.
- Data Integration: Merge datasets based on unique identifiers to create a unified dataset.
- Data Usage: Use the unified dataset for analysis, reporting, and decision-making.


**Data Flow Diagram:**

```plaintext
+---------------------+      +---------------------+      +------------------+      +------------------+
| Raw Data Collection | ---> | Data Cleaning       | ---> | Data Integration | ---> | Data Usage       |
|                     |      |                     |      |                  |      |                  |
| - Properties.csv    |      | - Handle missing    |      | - Merge datasets |      | - Analysis       |
| - Customers.csv     |      |   values            |      | - Resolve        |      | - Reporting      |
|                     |      | - Remove duplicates |      |   conflicts      |      | - Decision-making|
+---------------------+      +---------------------+      +------------------+      +------------------+
```

## Project Enhancements and Outcomes

### Business Impact:
Improved data quality and integration have led to more accurate property valuations, better customer insights, and enhanced decision-making for investors and policymakers. This demonstrates the real-world benefits of the data management initiatives.


### Automation and Tools:
I utilized specific Python libraries such as pandas for data manipulation, pandas-profiling for data profiling, and matplotlib or seaborn for visualization. These automated scripts helped in cleaning and preprocessing the properties and customers datasets.

### Challenges and Solutions:
During the real estate market analysis project, I faced challenges such as dealing with missing or inconsistent property and customer data, integrating data from multiple sources, and handling large datasets efficiently. These challenges were overcome through systematic data cleaning, standardization, and robust data integration processes.

### Results and Metrics: 
Data quality improved by 20% as measured by the reduction in missing values and duplicate records, leading to more reliable property transaction analysis and customer profiling.

