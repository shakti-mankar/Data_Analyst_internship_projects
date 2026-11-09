from ui import load_css, page_header

load_css()



import streamlit as st
import plotly.express as px
from database import fetch_data

st.set_page_config(page_title="Ratings Analysis", layout="wide")
st.title("Ratings Analysis")

rating_query = """
SELECT
    Vehicle_Type,
    ROUND(AVG(Driver_Ratings), 2) AS Average_Driver_Rating,
    ROUND(AVG(Customer_Rating), 2) AS Average_Customer_Rating
FROM ola_dataset
WHERE Booking_Status = 'Success'
GROUP BY Vehicle_Type
ORDER BY Vehicle_Type;
"""

rating_df = fetch_data(rating_query)

if not rating_df.empty:
    st.subheader("Average Ratings by Vehicle Type")

    st.dataframe(rating_df, use_container_width=True)

    fig1 = px.bar(
        rating_df,
        x="Vehicle_Type",
        y=["Average_Driver_Rating", "Average_Customer_Rating"],
        barmode="group",
        title="Driver vs Customer Ratings"
    )
    st.plotly_chart(fig1, use_container_width=True)

st.divider()

st.subheader("Driver Ratings Distribution")

driver_query = """
SELECT
    Driver_Ratings,
    COUNT(*) AS Total
FROM ola_dataset
WHERE Driver_Ratings IS NOT NULL
GROUP BY Driver_Ratings
ORDER BY Driver_Ratings;
"""

driver_df = fetch_data(driver_query)

if not driver_df.empty:
    fig2 = px.bar(
        driver_df,
        x="Driver_Ratings",
        y="Total",
        title="Driver Ratings Distribution",
        text_auto=True
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("Customer Ratings Distribution")

customer_query = """
SELECT
    Customer_Rating,
    COUNT(*) AS Total
FROM ola_dataset
WHERE Customer_Rating IS NOT NULL
GROUP BY Customer_Rating
ORDER BY Customer_Rating;
"""

customer_df = fetch_data(customer_query)

if not customer_df.empty:
    fig3 = px.bar(
        customer_df,
        x="Customer_Rating",
        y="Total",
        title="Customer Ratings Distribution",
        text_auto=True
    )
    st.plotly_chart(fig3, use_container_width=True)