"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 1.0.0
"""

from xgboost import XGBClassifier
import joblib
import logging
import pandas as pd
import typing as tp

logger = logging.getLogger(__name__)


def data_conf(
    df_train: pd.DataFrame, df_test: pd.DataFrame
) -> tp.Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.DataFrame]:
    X_train = df_train.drop(columns=["Cluster"])
    y_train = df_train["Cluster"]

    X_test = df_test.drop(columns=["Cluster"])
    y_test = df_test["Cluster"]

    y_test = y_test.to_frame(name="Cluster")

    return X_train, X_test, y_train, y_test


def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    params: tp.Dict,
) -> XGBClassifier:
    clf_model = XGBClassifier(
        random_state=params["random_state"],
        eval_metric=params["eval_metric"],
        use_label_encoder=params["use_label_encoder"],
        n_estimators=params["n_estimators"],
        learning_rate=params["learning_rate"],
        max_depth=params["max_depth"],
        min_samples_split=params["min_samples_split"],
        min_samples_leaf=params["min_samples_leaf"],
        subsample=params["subsample"],
        colsample_bytree=params["colsample_bytree"],
    )
    clf_model.fit(X_train, y_train)
    logger.info(f"Train accuracy: {clf_model.score(X_train, y_train)}")
    logger.info(f"Test accuracy: {clf_model.score(X_test, y_test)}")
    return clf_model
