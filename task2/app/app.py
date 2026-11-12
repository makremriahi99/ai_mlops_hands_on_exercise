"""Streamlit app to explore the cleaned Adult Census Income data."""
import os

import streamlit as st

from cleaning import load_clean

DATA_PATH = os.getenv("DATA_PATH", "datasets/census_income.csv")


@st.cache_data
def get_data():
    return load_clean(DATA_PATH)


st.title("Adult Census Income explorer")
df = get_data()
st.write(f"{len(df)} people in the cleaned dataset")
st.dataframe(df.head(100))