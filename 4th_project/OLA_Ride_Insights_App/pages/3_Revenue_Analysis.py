from ui import load_css, page_header

load_css()


import streamlit as st
import plotly.express as px
from database import fetch_data

st.set_page_config(page_title="Revenue Analysis", layout="wide")
st.title("Revenue Analysis")

st.subheader("Revenue by Payment Method")

payment_query = """
SELECT
    Payment_Method,
    ROUND(SUM(Booking_Value), 2) AS Total_Revenue
FROM ola_dataset
WHERE Booking_Status = 'Success'
GROUP BY Payment_Method
ORDER BY Total_Revenue DESC;
"""

payment_df = fetch_data(payment_query)

if not payment_df.empty:
    fig1 = px.bar(
        payment_df,
        x="Payment_Method",
        y="Total_Revenue",
        title="Revenue by Payment Method",
        text_auto=True
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.dataframe(payment_df, use_container_width=True)

st.divider()

st.subheader("Top 5 Customers by Booking Value")

customer_query = """
SELECT
    Customer_ID,
    COUNT(Booking_ID) AS Total_Rides,
    ROUND(SUM(Booking_Value), 2) AS Total_Booking_Value
FROM ola_dataset
WHERE Booking_Status = 'Success'
GROUP BY Customer_ID
ORDER BY Total_Booking_Value DESC
LIMIT 5;
"""

customer_df = fetch_data(customer_query)

if not customer_df.empty:
    fig2 = px.bar(
        customer_df,
        x="Customer_ID",
        y="Total_Booking_Value",
        title="Top 5 Customers by Total Booking Value",
        text_auto=True
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.dataframe(customer_df, use_container_width=True)

st.divider()

st.subheader("Daily Revenue")

daily_query = """
SELECT
    Date,
    ROUND(SUM(Booking_Value), 2) AS Daily_Revenue
FROM ola_dataset
WHERE Booking_Status = 'Success'
GROUP BY Date
ORDER BY Date;
"""

daily_df = fetch_data(daily_query)

if not daily_df.empty:
    daily_df["Date"] = daily_df["Date"].astype(str)

    fig3 = px.line(
        daily_df,
        x="Date",
        y="Daily_Revenue",
        title="Daily Revenue Trend",
        markers=True
    )
    st.plotly_chart(fig3, use_container_width=True)