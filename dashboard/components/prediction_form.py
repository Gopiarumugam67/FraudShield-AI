"""
Prediction Form Component.
"""

from __future__ import annotations

import streamlit as st
import pandas as pd


def render_prediction_form() -> pd.DataFrame | None:
    """
    Render transaction input form.

    Returns
    -------
    pd.DataFrame | None
    """

    st.header("Transaction Details")

    values = {}

    columns = [
    "Time",
    *[f"V{i}" for i in range(1, 29)],
    "Amount",
    ]

    for i in range(0, len(columns), 2):

        col1, col2 = st.columns(2)

        with col1:

            values[columns[i]] = st.number_input(
                columns[i],
                value=0.0,
                format="%.6f",
            )

        if i + 1 < len(columns):

            with col2:

                values[columns[i + 1]] = st.number_input(
                    columns[i + 1],
                    value=0.0,
                    format="%.6f",
                )

    predict = st.button(
        "🔍 Predict Transaction",
        use_container_width=True,
    )

    if predict:

        return pd.DataFrame([values])

    return None