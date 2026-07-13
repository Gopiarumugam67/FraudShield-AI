"""
Generate readable explanations.
"""

from __future__ import annotations

import pandas as pd
import numpy as np



class ExplanationGenerator:
    """
    Convert SHAP values into a readable dataframe.
    """

    def generate(
        self,
        transaction: pd.DataFrame,
        shap_values,
    ) -> pd.DataFrame:

        values = np.array(shap_values)

        # Handle different SHAP output formats
        if values.ndim == 3:
            values = values[:, :, 1]

        if values.ndim == 2:
            values = values[0]

        explanation = pd.DataFrame(
            {
                "Feature": transaction.columns.tolist(),
                "Impact": values.tolist(),
            }
        )

        explanation["Absolute"] = explanation["Impact"].abs()

        explanation = explanation.sort_values(
            "Absolute",
            ascending=False,
        )

        explanation = explanation.drop(
            columns="Absolute"
        )

        explanation.reset_index(
            drop=True,
            inplace=True,
        )

        return explanation