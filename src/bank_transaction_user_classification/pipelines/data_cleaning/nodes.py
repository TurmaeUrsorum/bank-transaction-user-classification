"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import typing as tp


def cleaning_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def split_data(df: pd.DataFrame, param: tp.Dict) -> tp.Tuple:
    X = df.drop(columns=["Cluster"])
    y = df["Cluster"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=param["test_size"], random_state=param["random_state"]
    )

    train_df = X_train.copy()
    train_df["Cluster"] = y_train.values

    test_df = X_test.copy()
    test_df["Cluster"] = y_test.values

    return train_df, test_df
