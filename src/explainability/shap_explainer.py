"""
SHAP Explainer for FraudShield AI.
"""

from __future__ import annotations

import shap
import pandas as pd
import numpy as np

class SHAPExplainer:
    """
    Wrapper around SHAP TreeExplainer.
    """

    def __init__(self, model):

        self.explainer = shap.TreeExplainer(model)

    def explain(self, transaction):

        shap_values = self.explainer.shap_values(transaction)

        print("\n==============================")
        print(type(shap_values))
        print(np.array(shap_values).shape)
        print("==============================\n")

        return shap_values