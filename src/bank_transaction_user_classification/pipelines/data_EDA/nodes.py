"""
This is a boilerplate pipeline 'data_EDA'
generated using Kedro 1.0.0
"""

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import seaborn as sns
import pandas as pd
import numpy as np


def df_numeric_convert(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=["float64", "int64"])


def df_categorical_convert(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=["object"])


def plot_skewness_check(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_numeric = df_numeric_convert(df)
    fig = plt.figure(figsize=(20, 10))

    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 3, i + 1)

        sns.histplot(
            data=pd.DataFrame({col: df_numeric[col]}), x=col, ax=ax, bins=20, kde=True
        )

        ax.set_title(col)

    return fig


def plot_outliers_check(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_numeric = df_numeric_convert(df)
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 3, i + 1)
        sns.boxplot({col: df_numeric[col]}, ax=ax)
        ax.set_title(col)
    return fig


def plot_correlation_heatmap(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_numeric = df_numeric_convert(df)

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(df_numeric.corr(), cmap="YlGnBu", annot=True, linewidths=0.5, ax=ax)

    ax.set_title("Correlation Heatmap for Numeric Columns")

    return fig


def plot_transaction_type(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_categorical = df_categorical_convert(df)

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.barplot(
        x=df_categorical["TransactionType"].value_counts().index,
        y=df_categorical["TransactionType"].value_counts().values,
        palette="rocket",
        alpha=0.8,
    )

    ax.set_title("Transaction Type Distribution")

    return fig


def plot_login_attempt(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_numeric = df_numeric_convert(df)

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.barplot(
        x=df_numeric["LoginAttempts"].value_counts().index,
        y=df_numeric["LoginAttempts"].value_counts().values,
        palette="rocket",
        alpha=0.8,
    )

    ax.set_title("Login Attempt Distribution")

    return fig


def plot_location(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_categorical = df_categorical_convert(df)

    fig = plt.figure(figsize=(20, 10))

    top5 = (
        df_categorical["Location"].value_counts().sort_values(ascending=False).head(5)
    )

    plt.barh(
        top5.index.to_numpy(),
        top5.to_numpy(),
        alpha=0.8,
        height=0.7,
    )

    plt.xlabel("Count")
    plt.title("Top 5 Locations")
    return fig


def plot_channel(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_categorical = df_categorical_convert(df)

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.barplot(
        x=df_categorical["Channel"].value_counts().index,
        y=df_categorical["Channel"].value_counts().values,
        palette="rocket",
        alpha=0.8,
    )

    ax.set_title("Channel Distribution")

    return fig


def plot_customer_occupation(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_categorical = df_categorical_convert(df)

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.barplot(
        x=df_categorical["CustomerOccupation"].value_counts().index,
        y=df_categorical["CustomerOccupation"].value_counts().values,
        palette="rocket",
        alpha=0.8,
    )

    ax.set_title("Customer Occupation Distribution")

    return fig


def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))


def cramer_v_matrix(df: pd.DataFrame) -> Figure:
    df = df.copy()
    df_categorical = df_categorical_convert(df)
    cat_cols = ["TransactionType", "Location", "Channel", "CustomerOccupation"]

    matrix = pd.DataFrame(
        np.zeros((len(cat_cols), len(cat_cols))), index=cat_cols, columns=cat_cols
    )

    for col1 in cat_cols:
        for col2 in cat_cols:
            if col1 != col2:
                matrix.loc[col1, col2] = cramers_v(
                    df_categorical[col1], df_categorical[col2]
                )

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)  # <- paksa semua ke fig yang sama

    sns.heatmap(matrix, annot=True, cmap="coolwarm", vmin=0, vmax=1, ax=ax)
    ax.set_title("Cramer's V Correlation (Categorical Variables)")
    fig.tight_layout()
    return fig
