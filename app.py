import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Title
st.set_page_config(page_title="Business Dashboard", layout="wide")

st.title("📊 Interactive Business Dashboard")

# Sample Data
data = {
    "Month": [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "Sales": [
        12000,15000,18000,17000,
        22000,25000,24000,28000,
        30000,32000,35000,40000
    ],

    "Customers": [
        120,150,170,160,
        210,240,235,270,
        300,320,350,390
    ],

    "Profit": [
        2500,3200,4000,3700,
        5000,6200,6000,7200,
        8000,8500,9500,11000
    ]
}

df = pd.DataFrame(data)

# Sidebar Filter
st.sidebar.header("Filters")

selected_months = st.sidebar.multiselect(
    "Select Months",
    df["Month"],
    default=df["Month"]
)

filtered_df = df[df["Month"].isin(selected_months)]

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"₹{filtered_df['Sales'].sum():,}"
    )

with col2:
    st.metric(
        "Customers",
        f"{filtered_df['Customers'].sum():,}"
    )

with col3:
    st.metric(
        "Profit",
        f"₹{filtered_df['Profit'].sum():,}"
    )

# Sales Trend
st.subheader("Sales Trend")

fig1 = px.line(
    filtered_df,
    x="Month",
    y="Sales",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# Customer Growth
st.subheader("Customer Growth")

fig2 = px.bar(
    filtered_df,
    x="Month",
    y="Customers"
)

st.plotly_chart(fig2, use_container_width=True)

# Profit Trend
st.subheader("Profit Trend")

fig3 = px.area(
    filtered_df,
    x="Month",
    y="Profit"
)

st.plotly_chart(fig3, use_container_width=True)

# Data Table
st.subheader("Dataset")

st.dataframe(filtered_df)

# Insights
st.subheader("Key Insights")

st.success("""
• Sales increased steadily throughout the year.

• Customer growth contributed to higher revenue.

• Q4 generated maximum profit.

• Sales and profit show strong positive correlation.
""")