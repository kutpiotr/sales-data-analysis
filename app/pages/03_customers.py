import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/sales_cleaned.csv")
    return df

df = load_data()

customer_summary = (
    df.groupby("customer_unique_id")
    .agg(
        orders_count=("order_id", "nunique"),
        total_revenue=("revenue", "sum"),
        avg_order_value=("order_value", "mean")
    )
    .sort_values("total_revenue", ascending=False)
    .reset_index()
)

top_customers = customer_summary.head(10)

st.title("Customer Analysis")

min_orders = st.slider("Minimum number of orders", min_value=1, max_value=10, value=1)

filtered_customers = customer_summary[customer_summary["orders_count"] >= min_orders]

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_customers["customer_unique_id"].astype(str), top_customers["total_revenue"])
    ax.set_title("Top 10 Customers by Revenue")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(filtered_customers["orders_count"], bins=20)
    ax.set_title("Distribution of Orders per Customer")
    st.pyplot(fig)

st.subheader("Customer summary")
st.dataframe(filtered_customers.head(50), use_container_width=True)