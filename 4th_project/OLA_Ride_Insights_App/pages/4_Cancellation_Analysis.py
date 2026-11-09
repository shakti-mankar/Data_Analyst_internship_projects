from ui import load_css, page_header

load_css()


import streamlit as st
import plotly.express as px
from database import fetch_data

st.set_page_config(page_title="Cancellation Analysis", layout="wide")
st.title("Cancellation Analysis")

cancellation_query = """
SELECT
    Booking_Status,
    COUNT(*) AS Total_Cancellations
FROM ola_dataset
WHERE Booking_Status IN (
    'Canceled by Customer',
    'Canceled by Driver'
)
GROUP BY Booking_Status;
"""

cancel_df = fetch_data(cancellation_query)

if not cancel_df.empty:
    fig1 = px.pie(
        cancel_df,
        names="Booking_Status",
        values="Total_Cancellations",
        title="Customer vs Driver Cancellations",
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.dataframe(cancel_df, use_container_width=True)

st.divider()

st.subheader("Customer Cancellation Reasons")

customer_reason_query = """
SELECT
    Canceled_Rides_by_Customer AS Cancellation_Reason,
    COUNT(*) AS Total
FROM ola_dataset
WHERE Booking_Status = 'Canceled by Customer'
  AND Canceled_Rides_by_Customer IS NOT NULL
GROUP BY Canceled_Rides_by_Customer
ORDER BY Total DESC;
"""

customer_reason_df = fetch_data(customer_reason_query)

if not customer_reason_df.empty:
    fig2 = px.bar(
        customer_reason_df,
        x="Cancellation_Reason",
        y="Total",
        title="Customer Cancellation Reasons",
        text_auto=True
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.dataframe(customer_reason_df, use_container_width=True)

st.divider()

st.subheader("Driver Cancellation Reasons")

driver_reason_query = """
SELECT
    Canceled_Rides_by_Driver AS Cancellation_Reason,
    COUNT(*) AS Total
FROM ola_dataset
WHERE Booking_Status = 'Canceled by Driver'
  AND Canceled_Rides_by_Driver IS NOT NULL
GROUP BY Canceled_Rides_by_Driver
ORDER BY Total DESC;
"""

driver_reason_df = fetch_data(driver_reason_query)

if not driver_reason_df.empty:
    fig3 = px.bar(
        driver_reason_df,
        x="Cancellation_Reason",
        y="Total",
        title="Driver Cancellation Reasons",
        text_auto=True
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.dataframe(driver_reason_df, use_container_width=True)    