"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import handling_outliers

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
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
        )
    ])
