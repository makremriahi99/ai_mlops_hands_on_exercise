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

st.sidebar.header("Filters")
all_sexes = sorted(df["sex"].unique())
sexes = st.sidebar.multiselect("Sex", all_sexes, default=all_sexes)
age_min, age_max = st.sidebar.slider("Age", 17, 90, (17, 90))

filtered = df[df["sex"].isin(sexes) & df["age"].between(age_min, age_max)]

if filtered.empty:
    st.warning("No people match these filters.")
    st.stop()

col1, col2 = st.columns(2)
col1.metric("People", f"{len(filtered):,}")
col2.metric("Share earning >50K", f"{filtered['income_gt50k'].mean() * 100:.1f}%")

st.dataframe(filtered.head(100))
st.subheader("Share earning >50K by category")
cat_cols = ["education", "marital_status", "occupation", "relationship", "race", "workclass", "sex"]
group_col = st.selectbox("Group by", cat_cols)

rate = filtered.groupby(group_col)["income_gt50k"].mean() * 100
st.bar_chart(rate, horizontal=True, x_label="% earning >50K", y_label=group_col)