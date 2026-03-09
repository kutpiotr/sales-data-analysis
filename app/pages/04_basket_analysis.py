import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

@st.cache_data
def load_pairs():
    df = pd.read_csv("data/processed/top_product_pairs.csv")
    return df

top_pairs = load_pairs()

st.title("Market Basket Analysis")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_pairs["product_pair"].astype(str), top_pairs["count"])
ax.set_title("Top Product Pairs Bought Together")
st.pyplot(fig)

st.subheader("Top product pairs")
st.dataframe(top_pairs)