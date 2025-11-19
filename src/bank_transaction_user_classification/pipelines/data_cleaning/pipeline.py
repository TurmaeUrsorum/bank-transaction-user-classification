"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import cleaning_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=cleaning_data,
                inputs="raw_data_train",
                outputs="train_df",
                name="cleaning_data_node",
            ),
            node(
                func=cleaning_data,
                inputs="raw_data_test",
                outputs="test_df",
                name="cleaning_data_test_node",
            ),
        ]
    )
