# data-pipeline
*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : JAGAN PADHIARY

*INTERN ID* : CT04DR268

*DOMAIN* : DATA SCIENCE

*DURATION* : 4 WEEKS
#  Data Pipeline Development

## Project Overview
This project demonstrates an **end-to-end data pipeline** built using **Python**, **Pandas**, and **Scikit-learn**.  
The goal is to **extract**, **transform**, and **load (ETL)** data efficiently — preparing it for further analysis or model training.  

It covers all major preprocessing steps, including:
- Handling missing values  
- Scaling numeric data  
- Encoding categorical variables  
- Saving the processed dataset for downstream use  

---

## Features
- Automatic detection of **numeric** and **categorical** columns  
- **Imputation** of missing values (mean for numeric, most frequent for categorical)  
- **Standard scaling** for numeric features  
- **One-hot encoding** for categorical features  
- **End-to-end pipeline** for clean, reusable preprocessing  
- Final cleaned dataset saved as `processed_data.csv`

---

##  Tech Stack
- **Python 3.13.5**
- **Pandas**
- **Scikit-learn**

---
Data_Pipeline_Project
│
├── data_pipeline.py # Main Python script for data pipeline
├── processed_data.csv # Output file with cleaned & transformed data
└── README.md # Project documentation


---

##  How It Works

### Step 1: Import Libraries
Essential libraries like Pandas and Scikit-learn are imported for data handling and preprocessing.

### Step 2: Extract Data
A sample dataset is created directly in the script (simulating data extraction).

### Step 3: Transform Data
The pipeline handles:
- Missing value imputation  
- Feature scaling  
- Categorical encoding  

### Step 4: Load Data
Processed data is saved into `processed_data.csv`.

---

##  Example Output

Example of the **processed data** saved:

| Feature_1 | Feature_2 | Feature_3 | ... | target |
|------------|------------|------------|-----|---------|
| 0.12 | -0.35 | 1.0 | ... | 1 |
| -1.22 | 0.87 | 0.0 | ... | 0 |
## Future Improvements

Add feature selection and normalization steps

Integrate with a real-world dataset (CSV or database)

Save preprocessing pipeline using joblib for model training

---
##  Project Structure
<img width="902" height="355" alt="Image" src="https://github.com/user-attachments/assets/95af96da-bc8c-4f44-8347-92f41d4121fb" />

## After cleaned dataset saved as`processed_data.csv` 
<img width="494" height="122" alt="Image" src="https://github.com/user-attachments/assets/63a224dd-4a39-41e8-b67c-9cfcc18bf941" />
