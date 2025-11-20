"""
This is a boilerplate pipeline 'data_evaluasi'
generated using Kedro 1.0.0
"""

from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import numpy as np
import pandas as pd
import typing as tp
import logging

logger = logging.getLogger(__name__)


def eval_model(model: XGBClassifier, X_test: pd.DataFrame, y_test: pd.DataFrame):
    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    logger.info(f"Classification Report:\n{report}")
    logger.info(f"Confusion Matrix:\n{cm}")

    return report, cm


def plot_cm(cm: np.ndarray) -> Figure:
    fig = plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap="coolwarm", vmin=0, vmax=1)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    return fig  # <–– ini yang kamu return
