import streamlit as st
from datetime import datetime
import pandas as pd
import requests

API_url = "http://localhost:8000"

def monthly_analytics_tab():
    # Fetch data from the API
    response = requests.get(f"{API_url}/monthly_summary/")
    
    # Check if the API call was successful
    if response.status_code != 200:
        st.error(f"Failed to fetch data from the server. Status code: {response.status_code}")
        return
    
    monthly_summary = response.json()
    
    # Check if the response is empty or invalid
    if not monthly_summary or not isinstance(monthly_summary, list):
        st.warning("No data found for monthly expenses.")
        return
    
    # Create a DataFrame from the API response
    try:
        df = pd.DataFrame(monthly_summary)
        df.rename(columns={
            "expense_month": "Month Number",
            "month_name": "Month Name",
            "total": "Total"
        }, inplace=True)
        
        # Sort by month number
        df_sorted = df.sort_values(by="Month Number", ascending=False)
        df_sorted.set_index("Month Number", inplace=True)

        # Display the title
        st.title("Expense Breakdown By Months")

        # Display the bar chart
        st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], width=0, height=0, use_container_width=True)

        # Format the Total column
        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

        # Display the table
        st.table(df_sorted.sort_index())
    
    except Exception as e:
        st.error(f"An error occurred while processing the data: {e}")