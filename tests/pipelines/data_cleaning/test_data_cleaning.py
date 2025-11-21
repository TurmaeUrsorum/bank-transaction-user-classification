"""
This is a boilerplate test file for pipeline 'data_cleaning'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

from bank_transaction_user_classification.pipelines.data_cleaning.nodes import cleaning_data
import pytest
import pandas as pd

@pytest.fixture
def df():
    return pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

def test_cleaning_data(df: pd.DataFrame):
    result = cleaning_data(df)
    assert result.isna().sum().sum() == 0
    assert result.duplicated().sum() == 0

    expected_columns = ["col1", "col2"]
    assert list(result.columns) == expected_columns
