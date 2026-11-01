# Real Estate Investment Advisor
### Property Market Analysis Using Python and Streamlit

## Project Overview
This project analyzes Indian housing market data to help users explore property prices, property sizes, locations, and other property-related features.

The application uses Python for data cleaning and Exploratory Data Analysis (EDA), and Streamlit for interactive visualization and property analysis.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Project Features
1. Dashboard Overview – Displays important property statistics.
2. Property Analysis – Analyzes property prices, sizes, and property types.
3. Location Analysis – Compares property prices across states and cities.
4. Investment Insights – Explores relationships between property features and prices.
5. Property Search – Filters properties according to user preferences.
6. Property Comparison – Compares multiple properties side by side.

## Project Structure
```text
Real_Estate_Investment_Advisor/
│
├── data/
│   ├── india_housing_prices.csv
│   └── cleaned_housing_data.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── eda.ipynb
│
├── outputs/
│
├── app/
│   └── app.py
│
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit application
```bash
streamlit run app/app.py
```

### 3. Open the application
Open the local URL displayed in your terminal.

## Project Scope
This project focuses on data cleaning, exploratory data analysis, and interactive data visualization. Machine learning and future-value prediction are not included in the implemented scope.

## Dataset
The project uses an Indian housing prices dataset containing property details such as location, property type, BHK, size, price, furnishing status, and amenities.

## Disclaimer
The application presents historical dataset analysis. Its insights should not be treated as guaranteed investment returns or financial advice.