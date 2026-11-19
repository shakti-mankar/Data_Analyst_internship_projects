
import mysql.connector
import pandas as pd
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_data(query):
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        return pd.DataFrame(rows, columns=columns)

    finally:
        connection.close()
