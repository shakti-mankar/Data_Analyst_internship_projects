# PROJECT DOCUMENTATION

# Real Estate Investment Advisor
### Property Market Analysis Using Python and Streamlit

## 1. Introduction

The Real Estate Investment Advisor is a data analysis project developed to explore the Indian housing market. It helps users understand property prices, sizes, locations, and other important property features through data analysis and interactive visualizations.

The project uses Python for data cleaning and Exploratory Data Analysis (EDA), while Streamlit is used to develop an interactive web application.

## 2. Problem Statement

Choosing a property can be difficult because property prices and features vary across different cities, localities, and property types.

This project aims to organize and analyze housing data so that users can explore property-related information and make more informed comparisons.

## 3. Project Objectives

- Clean and prepare the housing dataset using Python.
- Identify patterns and trends in property prices.
- Analyze property prices across different states and cities.
- Understand the relationship between property features and prices.
- Develop interactive charts and visualizations.
- Allow users to search and compare properties through a web application.

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- Visual Studio Code

## 5. Dataset Description

The project uses an Indian housing prices dataset containing 250,000 property records and 23 columns.

Important attributes include:

- State and City
- Locality
- Property Type
- BHK
- Size in Square Feet
- Price in Lakhs
- Price per Square Foot
- Year Built
- Furnished Status
- Parking Space
- Nearby Schools and Hospitals
- Public Transport Accessibility
- Amenities
- Availability Status

## 6. Data Cleaning

Data cleaning was performed using Python and Pandas.

The following checks and operations were performed:

- Checked missing values.
- Checked duplicate records.
- Checked duplicate property IDs.
- Examined invalid property sizes and prices.
- Checked floor number inconsistencies.
- Examined price-per-square-foot values.
- Reviewed numerical columns for unusual values.
- Prepared the cleaned dataset for EDA.

Suspicious floor records and potential outliers were investigated rather than automatically deleted.

## 7. Exploratory Data Analysis

EDA was performed to understand the housing dataset and identify useful patterns.

The analysis covered:

- Property price distribution.
- Property size distribution.
- Price per square foot by property type.
- Relationship between property size and price.
- Potential outliers.
- Average property prices across states and cities.
- Property age across localities.
- BHK distribution.
- Expensive localities.
- Correlation between numerical features.
- Nearby schools and hospitals.
- Furnishing status and property prices.
- Property facing direction.
- Owner type and availability status.
- Parking facilities.
- Amenities.
- Public transport accessibility.

## 8. Streamlit Application Modules

### 8.1 Dashboard Overview
Displays important statistics about the selected housing data.

### 8.2 Property Analysis
Displays property price distribution, average prices by property type, and size-versus-price analysis.

### 8.3 Location Analysis
Compares property prices and price per square foot across states and cities.

### 8.4 Investment Insights
Explores property features such as age, furnishing, parking, amenities, and transport accessibility in relation to prices.

### 8.5 Property Search
Allows users to filter properties using budget, BHK, property size, and furnishing status.

### 8.6 Property Comparison
Allows users to compare multiple properties using their property IDs.

## 9. Project Methodology

The project follows these stages:

1. Dataset collection.
2. Data inspection.
3. Data cleaning and preprocessing.
4. Exploratory Data Analysis.
5. Creation of summary files.
6. Development of the Streamlit application.
7. Integration of interactive filters and visualizations.
8. Application testing.

## 10. Project Scope and Limitations

The implemented project focuses on data cleaning, EDA, property search, property comparison, and interactive visualization.

Machine learning models and automated future-property-value predictions are not included in the current implementation.

The insights are based on the available dataset and should not be considered guaranteed investment returns or financial advice.

## 11. Conclusion

The Real Estate Investment Advisor provides an interactive way to explore Indian housing market data. It helps users understand property prices, compare locations, examine property features, and search for properties based on their preferences.

The project demonstrates how Python-based data analysis and Streamlit can be combined to develop a practical data-driven application.