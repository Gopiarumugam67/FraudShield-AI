"""
Batch Prediction Component.
"""

from __future__ import annotations

import time

import pandas as pd
import streamlit as st

from src.inference.prediction_pipeline import PredictionPipeline
from dashboard.components.analytics import (
    render_analytics,
)

def render_batch_prediction():

    st.header("Batch Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"],
    )

    if uploaded_file is None:
        return None

    dataframe = pd.read_csv(uploaded_file)

    # Development only
    # Remove this line later
    dataframe = dataframe.head(200)

    st.success(
        f"Loaded {len(dataframe)} transactions."
    )

    st.dataframe(
        dataframe.head()
    )

    if st.button(
        "🚀 Predict Entire Dataset",
        use_container_width=True,
    ):

        
        pipeline = PredictionPipeline()

        X = dataframe.drop(
            columns=["Class"],
            errors="ignore",
        )

        start = time.time()

        results = pipeline.predict_batch(X)

        end = time.time()

        dataframe = pd.concat(
            [
                dataframe,
                results,
            ],
            axis=1,
        )

        st.success(
            f"✅ Prediction completed in {end - start:.2f} seconds."
        )
        st.dataframe(
            dataframe.head()
        )

        render_analytics(dataframe)
        
        csv = dataframe.to_csv(
            index=False
        )

        st.download_button(
            "⬇ Download Predictions",
            csv,
            file_name="fraud_predictions.csv",
            mime="text/csv",
        )

    return dataframe