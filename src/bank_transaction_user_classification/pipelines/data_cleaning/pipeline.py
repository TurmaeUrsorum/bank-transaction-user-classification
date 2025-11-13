"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import cleaning_data, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=cleaning_data,
                inputs="raw_data_train",
                outputs="cleaned_data",
                name="cleaning_data_node",
            ),
            node(
                func=split_data,
                inputs=["cleaned_data", "params:Splitting"],
                outputs=["train_df", "test_df"],
                name="split_data_node",
            ),
        ]
    )
