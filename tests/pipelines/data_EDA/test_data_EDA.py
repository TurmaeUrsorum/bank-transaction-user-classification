"""
This is a boilerplate test file for pipeline 'data_EDA'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

from bank_transaction_user_classification.pipelines.data_EDA.nodes import (
    plot_skewness_check,
    plot_outliers_check,
    plot_correlation_heatmap,
    plot_transaction_type,
    plot_login_attempt,
    plot_location,
    plot_channel,
    plot_customer_occupation,
    cramers_v,
    cramer_v_matrix,
)
import pytest
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.figure as mpl_fig
import numpy as np


@pytest.fixture
def df_numeric():
    return pd.DataFrame(
        {"LoginAttempts": [1, 2, 3, 1, 2, 3], "col2": [4, 5, 6, 4, 5, 6]}
    )


@pytest.fixture
def df_categorical():
    return pd.DataFrame(
        {
            "TransactionType": ["A", "B", "A", "C", "A", "B", "A", "C"],
            "Location": ["A", "B", "A", "C", "B", "A", "D", "E"],
            "Channel": ["A", "B", "A", "C", "B", "A", "D", "E"],
            "CustomerOccupation": ["A", "B", "A", "C", "B", "A", "D", "E"],
        }
    )

@pytest.fixture
def df_cramers():
    df = pd.DataFrame({
        "TransactionType": ["A", "B", "A", "B"],
        "Location": ["L1", "L2", "L1", "L2"],
        "Channel": ["C1", "C1", "C2", "C2"],
        "CustomerOccupation": ["O1", "O1", "O2", "O2"],
    })
    return df


def test_plot_skewness(df_numeric: pd.DataFrame):
    fig = plot_skewness_check(df_numeric)

    # testing output type
    assert isinstance(fig, Figure)

    # testing output shape plot
    assert len(fig.axes) == len(df_numeric.columns)

    # testing subplot
    for ax in fig.axes:
        assert len(ax.patches) > 0 or len(ax.lines) > 0

    plt.close(fig)


def test_plot_outliers(df_numeric: pd.DataFrame):
    fig = plot_outliers_check(df_numeric)
    ax = fig.axes[0]

    # testing output type
    assert isinstance(fig, Figure)

    # boxplot element core check
    assert len(ax.patches) == 1

    # Whisker / median lines check
    # seaborn boxplot menghasilkan > 5 garis (whiskers, caps, median)
    assert len(ax.lines) >= 5

    plt.close(fig)


def test_plot_correlation_heatmap(df_numeric: pd.DataFrame):
    fig = plot_correlation_heatmap(df_numeric)

    assert isinstance(fig, Figure)  # return type
    assert len(fig.axes) >= 1  # hanya 1 heatmap
    assert fig.axes[0].get_title() == "Correlation Heatmap for Numeric Columns"
    plt.close(fig)


def test_plot_transaction(df_categorical: pd.DataFrame):
    fig = plot_transaction_type(df_categorical)

    # Check output type
    assert isinstance(fig, Figure)

    # Barplot: exactly 1 Axes expected
    assert len(fig.axes) >= 1

    ax = fig.axes[0]

    # Check title
    assert ax.get_title() == "Transaction Type Distribution"

    # Check number of bars (unique categories)
    bars = ax.patches
    assert len(bars) == df_categorical["TransactionType"].nunique()
    plt.close(fig)


def test_plot_login_attempt(df_numeric: pd.DataFrame):
    fig = plot_login_attempt(df_numeric)

    # Check output type
    assert isinstance(fig, Figure)

    # Barplot: exactly 1 Axes expected
    assert len(fig.axes) >= 1

    ax = fig.axes[0]

    # Check title
    assert ax.get_title() == "Login Attempt Distribution"

    # Check number of bars (unique categories)
    bars = ax.patches
    assert len(bars) == df_numeric["LoginAttempts"].nunique()
    plt.close(fig)


def test_plot_location(df_categorical: pd.DataFrame):
    fig = plot_location(df_categorical)

    # Check returned type
    assert isinstance(fig, mpl_fig.Figure)

    # Access the axes where bars exist
    ax = fig.axes[0]

    # Check title
    assert ax.get_title() == "Top 5 Locations"

    # Bars check: unique locations = 5 -> plot all 5
    bars = ax.patches
    assert len(bars) == min(5, df_categorical["Location"].nunique())

    # x-axis label check (optional)
    assert ax.get_xlabel() == "Count"
    plt.close(fig)

def test_plot_channel(df_categorical: pd.DataFrame):
    fig = plot_channel(df_categorical)

    # Check returned type
    assert isinstance(fig, mpl_fig.Figure)

    # Access the axes where bars exist
    ax = fig.axes[0]

    # Check title
    assert ax.get_title() == "Channel Distribution"

    # x-axis label check (optional)
    assert ax.get_xlabel() == "Channel"
    plt.close(fig)

def test_plot_customer_occupation(df_categorical: pd.DataFrame):
    fig = plot_customer_occupation(df_categorical)

    # Check returned type
    assert isinstance(fig, mpl_fig.Figure)

    # Access the axes where bars exist
    ax = fig.axes[0]

    # Check title
    assert ax.get_title() == "Customer Occupation Distribution"

    # x-axis label check (optional)
    assert ax.get_xlabel() == "CustomerOccupation"
    plt.close(fig)

def test_cramers_v_no_association():
    x = pd.Series(["A", "A", "B", "B"])
    y = pd.Series(["C", "D", "C", "D"])

    v = cramers_v(x, y)

    assert isinstance(v, float)
    assert np.isclose(v, 0.0, atol=1e-6)  # no association


def test_cramers_v_perfect_association():
    x = pd.Series(["A", "A", "B", "B"])
    y = pd.Series(["X", "X", "Y", "Y"])

    v_yes = cramers_v(x, y)

    assert isinstance(v_yes, float)
    assert 0.0 <= v_yes <= 1.0  # valid range


def test_cramers_v_range():
    x = pd.Series(["A", "A", "B", "B", "A"])
    y = pd.Series(["X", "Y", "X", "Y", "X"])

    v = cramers_v(x, y)

    assert 0.0 <= v <= 1.0

def test_cramer_v_matrix(df_cramers: pd.DataFrame):

    fig = cramer_v_matrix(df_cramers)

    # Check the return type
    assert isinstance(fig, mpl_fig.Figure)

    # Heatmap + colorbar => at least 1 axis exists
    assert len(fig.axes) >= 1

    # Validate title
    ax = fig.axes[0]
    assert ax.get_title() == "Cramer's V Correlation (Categorical Variables)"

    # Extract heatmap data from the first axes
    heatmap = ax.collections[0]
    data_array = heatmap.get_array().data # type: ignore

    # Matrix shape must be 4x4 (jumlah cat_cols)
    assert data_array.shape == (4, 4)

    # All values harus dalam range 0–1
    assert np.all((data_array >= 0) & (data_array <= 1)) # type: ignore


