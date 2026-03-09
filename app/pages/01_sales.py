import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/sales_cleaned.csv")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    return df

df = load_data()

st.title("Sales Analysis")

min_date = df["order_purchase_timestamp"].min().date()
max_date = df["order_purchase_timestamp"].max().date()

date_range = st.date_input(
"Select date range",
value=(min_date, max_date),
min_value=min_date,
max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = df[
        (df["order_purchase_timestamp"].dt.date >= start_date) &
        (df["order_purchase_timestamp"].dt.date <= end_date)
    ].copy()
else:
    filtered_df = df.copy()

filtered_df["order_month"] = filtered_df["order_purchase_timestamp"].dt.to_period("M").astype(str)

monthly_sales = (
    filtered_df.groupby("order_month")
    .agg(
        revenue=("revenue", "sum"),
        orders=("order_id", "nunique")
    )
    .reset_index()
)

sales_revenue = filtered_df["revenue"].sum()
sales_orders = filtered_df["order_id"].nunique()

col1, col2 = st.columns(2)
col1.metric("Revenue in selected range", f"{sales_revenue:,.2f}")
col2.metric("Orders in selected range", sales_orders)

col3, col4 = st.columns(2)

with col3:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_sales["order_month"], monthly_sales["revenue"])
    ax.set_title("Monthly Revenue")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)

with col4:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_sales["order_month"], monthly_sales["orders"])
    ax.set_title("Number of Orders Over Time")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)

st.subheader("Monthly sales table")
st.dataframe(monthly_sales, use_container_width=True)