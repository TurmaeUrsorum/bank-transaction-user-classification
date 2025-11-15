"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

import pandas as pd
import numpy as np
import typing as tp


def handle_outliers_iqr(df, columns, k=1.5, method="remove"):
    df_copy = df.copy()
    mask = pd.Series(False, index=df.index)  # semua False dulu

    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - k * IQR
        upper = Q3 + k * IQR

        if method == "capping":
            # Ganti nilai outlier dengan batas bawah/atas
            df_copy[col] = np.where(
                df[col] < lower, lower, np.where(df[col] > upper, upper, df[col])
            )

        else:
            # Tandai outlier untuk detect/remove
            mask |= (df[col] < lower) | (df[col] > upper)

    if method == "detect":
        return df[mask]  # hanya outliers
    elif method == "remove":
        return df[~mask]  # data tanpa outliers
    elif method == "capping":
        return df_copy  # data dengan capping
    else:
        raise ValueError("method harus salah satu dari: 'detect', 'remove', 'capping'")


def handling_outliers(df: pd.DataFrame, params: tp.Dict) -> pd.DataFrame:
    df = df.copy()
    outliers_columns = params["columns"]
    df_train_outliers_clean = handle_outliers_iqr(
        df=df, columns=outliers_columns, k=params["k"], method=params["method"]
    )
    return df_train_outliers_clean
