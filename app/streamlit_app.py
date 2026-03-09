import streamlit as st
import pandas as pd

st.set_page_config(
page_title="Sales Data Analysis Dashboard",
page_icon="📊",
layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/sales_cleaned.csv")
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    return df

df = load_data()

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_unique_id"].nunique()
avg_order_value = df.groupby("order_id")["revenue"].sum().mean()

min_date = df["order_purchase_timestamp"].min().date()
max_date = df["order_purchase_timestamp"].max().date()

st.title("Sales Data Analysis Dashboard")
st.markdown("Interaktywny dashboard prezentujący analizę danych sprzedażowych sklepu internetowego.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"{total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Average Order Value", f"{avg_order_value:,.2f}")

st.markdown("---")

col5, col6 = st.columns(2)
col5.info(f"Date range: {min_date} — {max_date}")
col6.info(f"Rows in dataset: {len(df):,}")

st.subheader("Dataset preview")
st.dataframe(df.head(20), use_container_width=True)

st.markdown("---")
st.write("Use the navigation panel on the left to explore detailed analyses of sales, products, customers, and basket patterns.")