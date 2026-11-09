from ui import load_css, page_header

load_css()



import streamlit as st
import plotly.express as px
from database import fetch_data

st.set_page_config(page_title="OLA Overview", layout="wide")
st.title("OLA Ride Insights – Overview")
st.caption("Overall ride booking performance")

kpi_query = """
SELECT
    COUNT(*) AS Total_Bookings,
    SUM(CASE WHEN Booking_Status = 'Success' THEN 1 ELSE 0 END) AS Successful_Bookings,
    SUM(CASE WHEN Booking_Status = 'Canceled by Customer' THEN 1 ELSE 0 END) AS Customer_Cancellations,
    SUM(CASE WHEN Booking_Status = 'Canceled by Driver' THEN 1 ELSE 0 END) AS Driver_Cancellations,
    SUM(CASE WHEN Booking_Status = 'Success' THEN Booking_Value ELSE 0 END) AS Successful_Revenue
FROM ola_dataset;
"""

kpi = fetch_data(kpi_query)

if not kpi.empty:
    data = kpi.iloc[0]

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Bookings", f"{int(data['Total_Bookings']):,}")
    c2.metric("Successful Bookings", f"{int(data['Successful_Bookings']):,}")
    c3.metric("Successful Revenue", f"₹{data['Successful_Revenue']:,.2f}")

    c4, c5 = st.columns(2)
    c4.metric("Customer Cancellations", f"{int(data['Customer_Cancellations']):,}")
    c5.metric("Driver Cancellations", f"{int(data['Driver_Cancellations']):,}")

st.divider()

status_query = """
SELECT Booking_Status, COUNT(*) AS Total
FROM ola_dataset
GROUP BY Booking_Status
ORDER BY Total DESC;
"""

status_data = fetch_data(status_query)

if not status_data.empty:
    fig = px.pie(
        status_data,
        names="Booking_Status",
        values="Total",
        title="Booking Status Breakdown",
        hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Booking Data")
st.dataframe(status_data, use_container_width=True)