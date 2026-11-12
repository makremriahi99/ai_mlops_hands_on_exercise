"""Cleaning steps from the Task 1 notebook, reused by the app."""
import numpy as np
import pandas as pd


def load_clean(path):
    """Read the raw census CSV and apply the Task 1 cleaning."""
    df = pd.read_csv(path, skipinitialspace=True)
    df["income"] = df["income"].str.rstrip(".")
    df["income_gt50k"] = (df["income"] == ">50K").astype(int)
    df = df.replace("?", np.nan)
    df = df.drop_duplicates()
    df.columns = df.columns.str.replace("-", "_")
    df = df.drop(columns=["fnlwgt"])
    df["capital_gain_topcoded"] = (df["capital_gain"] == 99999).astype(int)
    return df


if __name__ == "__main__":
    df = load_clean("datasets/census_income.csv")
    assert df.shape == (48790, 16), df.shape
    print("OK", df.shape)