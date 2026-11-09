
import streamlit as st
import plotly.express as px
from database import fetch_data

st.set_page_config(
    page_title="OLA Ride Insights",
    page_icon="🚕",
    layout="wide"
)

st.title("🚕 OLA Ride Insights")
st.caption("Ride-Sharing & Mobility Analytics")

# KPI Query
kpi_query = """
SELECT
    COUNT(*) AS Total_Bookings,

    SUM(CASE
        WHEN Booking_Status = 'Success'
        THEN 1 ELSE 0
    END) AS Successful_Bookings,

    SUM(CASE
        WHEN Booking_Status = 'Canceled by Customer'
        THEN 1 ELSE 0
    END) AS Customer_Cancellations,

    SUM(CASE
        WHEN Booking_Status = 'Canceled by Driver'
        THEN 1 ELSE 0
    END) AS Driver_Cancellations,

    SUM(CASE
        WHEN Booking_Status = 'Success'
        THEN Booking_Value ELSE 0
    END) AS Successful_Revenue

FROM ola_dataset;
"""

try:
    data = fetch_data(kpi_query)
    row = data.iloc[0]

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Bookings",
        f"{int(row['Total_Bookings']):,}"
    )

    col2.metric(
        "Successful Bookings",
        f"{int(row['Successful_Bookings']):,}"
    )

    col3.metric(
        "Customer Cancellations",
        f"{int(row['Customer_Cancellations']):,}"
    )

    col4.metric(
        "Driver Cancellations",
        f"{int(row['Driver_Cancellations']):,}"
    )

    st.divider()

    # Revenue KPI
    st.subheader("Revenue Analysis")

    st.metric(
        "Successful Booking Revenue",
        f"₹{float(row['Successful_Revenue'] or 0):,.2f}"
    )

    # Booking Status Chart
    st.subheader("Booking Status Breakdown")

    status_query = """
    SELECT
        Booking_Status,
        COUNT(*) AS Total
    FROM ola_dataset
    GROUP BY Booking_Status
    ORDER BY Total DESC;
    """

    status_data = fetch_data(status_query)

    fig = px.pie(
        status_data,
        names="Booking_Status",
        values="Total",
        title="Booking Status Breakdown",
        hole=0.4
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except Exception as e:
    st.error(f"Unable to load dashboard: {e}")
