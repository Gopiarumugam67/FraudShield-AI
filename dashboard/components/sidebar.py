"""
Sidebar component for FraudShield AI Dashboard.
"""

from __future__ import annotations

import streamlit as st


def render_sidebar() -> str:
    """
    Render dashboard sidebar.

    Returns
    -------
    str
        Selected prediction mode.
    """

    with st.sidebar:

        st.image(
            "https://img.icons8.com/color/96/security-checked.png",
            width=70,
        )

        st.title("FraudShield AI")

        st.caption(
            "Enterprise Credit Card Fraud Detection"
        )

        st.divider()

        prediction_mode = st.radio(
            "Prediction Mode",
            [
                "Single Transaction",
                "Batch Prediction",
            ],
        )

        st.divider()

        st.markdown("### Model")

        st.success("Random Forest")

        st.divider()

        st.markdown("### Version")

        st.info("v1.0.0")

    return prediction_mode