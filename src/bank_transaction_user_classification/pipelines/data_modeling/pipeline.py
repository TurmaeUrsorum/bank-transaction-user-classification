"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import data_conf, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=data_conf,
                inputs=["train_df_final_cleaned", "test_df_final_cleaned"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="data_conf_node",
            ),
            node(
                func=train_model,
                inputs=[
                    "X_train",
                    "X_test",
                    "y_train",
                    "y_test",
                    "params:XGBClassifier",
                ],
                outputs="model_XGBClassifier",
                name="train_model_node",
            )
        ]
    )
