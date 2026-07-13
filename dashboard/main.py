"""
FraudShield AI Dashboard.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from src.inference.prediction_pipeline import PredictionPipeline

from dashboard.components.sidebar import render_sidebar
from dashboard.components.prediction_form import render_prediction_form
from dashboard.components.prediction_result import (
    render_prediction_result,
)
from dashboard.components.batch_prediction import (
    render_batch_prediction,
)
from dashboard.components.explainability import (
    render_explanation,
)

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ FraudShield AI")

prediction_mode = render_sidebar()

# =====================================
# Batch Prediction
# =====================================

if prediction_mode == "Batch Prediction":

    render_batch_prediction()

    st.stop()

# =====================================
# Single Prediction
# =====================================

st.markdown(
    "### Credit Card Fraud Detection System"
)

pipeline = PredictionPipeline()

transaction = render_prediction_form()

if transaction is not None:

    result = pipeline.predict(
        transaction
    )

    # Prediction Result
    render_prediction_result(
        result
    )
    render_explanation(result)
