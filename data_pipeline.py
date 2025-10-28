# ============================================================
# INTERNSHIP TASK - 1
# DATA PIPELINE DEVELOPMENT
# ------------------------------------------------------------
# Objective:
# As a beginner, your goal is to build a simple pipeline
# that reads data, cleans it, transforms it, and saves it again.
# We’ll use two main Python tools:
# - Pandas: For handling data
# - Scikit-learn: For data preprocessing automation
# ============================================================

# STEP 1: Import the required libraries
# -----------------------------------------
# Pandas: Used for data handling (loading, viewing, saving)
# Scikit-learn: Used for preprocessing data (cleaning, scaling, encoding)

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

print(" Libraries imported successfully!")

# STEP 2: Extract - Load your data
# -----------------------------------------
# Here we create a small sample dataset for learning purposes.
# In real cases, you will load your dataset using pd.read_csv("filename.csv")

data = {
    'Age': [25, 30, None, 22, 28],
    'Salary': [50000, 54000, 58000, None, 52000],
    'Department': ['HR', 'Finance', 'IT', 'HR', None],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'target': [1, 0, 1, 0, 1]  # Target column (for output)
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

print("\n Step 2: Raw Data Loaded Successfully!")
print(df)

#  STEP 3: Understand your data
# -----------------------------------------
# This step helps us see what kind of data we have and if there are missing values.

print("\n Dataset Information:")
print(df.info())  # Info about data types and null values

print("\n Missing Values:")
print(df.isnull().sum())  # Count missing values in each column

#  STEP 4: Separate features (X) and target (y)
# -----------------------------------------
# X → All input columns except the target
# y → The target column (output we want to keep or predict)

X = df.drop("target", axis=1)
y = df["target"]

# Identify which columns are numeric and which are categorical
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

print("\n Numeric Columns:", list(numeric_features))
print(" Categorical Columns:", list(categorical_features))

#  STEP 5: Create preprocessing steps
# -----------------------------------------
# We'll handle missing values and make data ready for machine learning.

# Numeric columns:
# - Fill missing values with mean
# - Scale values so they are in a similar range
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Categorical columns:
# - Fill missing values with most frequent value
# - Convert text labels into numbers using OneHotEncoder
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Combine both numeric and categorical transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# STEP 6: Build a complete pipeline
# -----------------------------------------
# This pipeline will automatically handle all preprocessing steps.

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])

# Fit the pipeline on the data and transform it
X_transformed = pipeline.fit_transform(X)

print("\n Step 6: Data transformation completed!")

# STEP 7: Convert the transformed data back to a DataFrame
# -----------------------------------------
# After transformation, we convert the output array into a new DataFrame.

# Convert NumPy array to DataFrame
X_transformed_df = pd.DataFrame(
    X_transformed.toarray() if hasattr(X_transformed, "toarray") else X_transformed
)

# Combine transformed features with target column
processed_df = pd.concat([X_transformed_df, y.reset_index(drop=True)], axis=1)

print("\n Step 7: Processed DataFrame Created:")
print(processed_df.head())

# STEP 8: Load - Save the cleaned data to a CSV file
# -----------------------------------------
# This file can now be used for analysis or machine learning.

processed_df.to_csv("processed_data.csv", index=False)

print("\n Step 8: ETL Process Completed Successfully!")
print(" Cleaned file saved as 'processed_data.csv'")
