"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
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


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["AmountToBalanceRatio"] = df["TransactionAmount"] / (df["AccountBalance"] + 1e-6)

    # Flag login attempts
    df["MultipleLoginFlag"] = (df["LoginAttempts"] > 1).astype(int)

    # Kategori umur
    # df["AgeGroup"] = pd.cut(
    #     df["CustomerAge"], bins=[0, 29, 50, 100], labels=["Young", "Adult", "Senior"]
    # )

    return df


# def handling_imputer(df: pd.DataFrame, params: tp.Dict) -> tp.Tuple:
#     df = df.copy()

#     numeric_columns = params["numeric_columns"]
#     categorical_columns = params["categorical_columns"]

#     # ambil konfigurasi imputer
#     numeric_cfg = params["simple_imputer_numeric"]
#     categorical_cfg = params["simple_imputer_categorical"]

#     # 1. Imputer
#     numeric_imputer = SimpleImputer(strategy=numeric_cfg["strategy"])
#     categorical_imputer = SimpleImputer(strategy=categorical_cfg["strategy"])

#     numeric_imputed = numeric_imputer.fit_transform(df[numeric_columns])
#     categorical_imputed = categorical_imputer.fit_transform(df[categorical_columns])

#     return (numeric_imputed, categorical_imputed)


def encoder_scaler(
    numeric_df: pd.DataFrame, categorical_df: pd.DataFrame, params: tp.Dict
) -> tp.Tuple[pd.DataFrame, pd.DataFrame]:
    one_hot_cfg = params["one_hot_encoder"]
    one_hot_encoder = OneHotEncoder(sparse_output=one_hot_cfg["sparse"])
    one_hot_array = one_hot_encoder.fit_transform(categorical_df)

    one_hot_df = pd.DataFrame(
        one_hot_array,
        columns=one_hot_encoder.get_feature_names_out(categorical_df.columns),
    )

    scaler = StandardScaler()
    numeric_scaled = scaler.fit_transform(numeric_df)

    numeric_scaled_df = pd.DataFrame(numeric_scaled, columns=numeric_df.columns)

    return one_hot_df, numeric_scaled_df


def data_preproses(df: pd.DataFrame, params: tp.Dict) -> pd.DataFrame:
    df = df.copy()

    # original_index = df.index

    numeric_columns = params["numeric_columns"]
    categorical_columns = params["categorical_columns"]

    # numeric_imputed, categorical_imputed = handling_imputer(df, params)

    # numeric_df = pd.DataFrame(numeric_imputed, columns=numeric_columns)
    # categorical_df = pd.DataFrame(categorical_imputed, columns=categorical_columns)

    onehot_df, numeric_scaled_df = encoder_scaler(
        df[numeric_columns], df[categorical_columns], params
    )

    df_combined = pd.concat([numeric_scaled_df, onehot_df], axis=1)

    df_cluster = df[["Cluster"]]

    # df_cluster = df_cluster.loc[df_combined.index]

    df_final = pd.concat([df_cluster, df_combined], axis=1)

    return df_final


def final_data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna()
    df["Cluster"] = df["Cluster"].astype(int)
    return df
