import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/sales_cleaned.csv")
    return df

df = load_data()

top_products = (
    df.groupby("product_id")
    .agg(
        revenue=("revenue", "sum"),
        quantity=("product_id", "count")
    )
    .sort_values("revenue", ascending=False)
    .head(10)
    .reset_index()
)

category_sales = (
    df.groupby("product_category_name")
    .agg(
        revenue=("revenue", "sum"),
        quantity=("product_id", "count")
    )
    .sort_values("revenue", ascending=False)
    .head(10)
    .reset_index()
)

st.title("Product Analysis")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_products["product_id"].astype(str), top_products["revenue"])
    ax.set_title("Top 10 Products by Revenue")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(category_sales["product_category_name"].astype(str), category_sales["revenue"])
    ax.set_title("Top 10 Categories by Revenue")
    st.pyplot(fig)

st.subheader("Top products")
st.dataframe(top_products)

st.subheader("Top categories")
st.dataframe(category_sales)