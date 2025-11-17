"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import handling_outliers, feature_engineering


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=handling_outliers,
                inputs=["train_df", "params:handling_outliers"],
                outputs="train_df_cleaned",
                name="train_df_cleaned_node",
            ),
            node(
                func=handling_outliers,
                inputs=["test_df", "params:handling_outliers"],
                outputs="test_df_cleaned",
                name="test_df_cleaned_node",
            ),
            node(
                func=feature_engineering,
                inputs="train_df_cleaned",
                outputs="feature_eng_train",
                name="feature_eng_train_node",
            ),
            node(
                func=feature_engineering,
                inputs="test_df_cleaned",
                outputs="feature_eng_test",
                name="feature_eng_test_node",
            ),
        ]
    )
