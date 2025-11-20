"""
This is a boilerplate pipeline 'data_evaluasi'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import eval_model, plot_cm


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=eval_model,
                inputs=["model_XGBClassifier", "X_test", "y_test"],
                outputs=["report", "cm"],
                name="eval_model_node",
            ),
            node(
                func=plot_cm,
                inputs="cm",
                outputs="cm_fig",
                name="plot_cm_node",
            ),
        ]
    )
