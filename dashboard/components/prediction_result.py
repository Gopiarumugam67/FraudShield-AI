"""
Prediction Result Component.
"""

from __future__ import annotations

import streamlit as st


def render_prediction_result(result: dict):
    """
    Display prediction results and explanation.
    """

    st.divider()

    st.header("Prediction Result")

    probability = result["probability"]

    confidence = max(
        probability,
        1 - probability,
    ) * 100

    if probability < 0.30:
        risk = "🟢 Low"

    elif probability < 0.70:
        risk = "🟡 Medium"

    else:
        risk = "🔴 High"

    # Prediction Status
    if result["prediction"] == 1:

        st.error(
            "🚨 Fraudulent Transaction Detected"
        )

    else:

        st.success(
            "✅ Legitimate Transaction"
        )

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Fraud Probability",
            f"{probability:.6f}",
        )

    with col2:

        st.metric(
            "Confidence",
            f"{confidence:.2f} %",
        )

    with col3:

        st.metric(
            "Risk Level",
            risk,
        )

    # ==========================
    # Explainability
    # ==========================

    explanation = result.get("explanation")

    if explanation is None:

        return

    st.divider()

    st.subheader("🧠 Top Influential Features")

    top_features = explanation.head(5)

    for _, row in top_features.iterrows():

        feature = row["Feature"]

        impact = row["Impact"]

        st.write(
            f"**{feature}**"
        )

        st.progress(
            min(abs(float(impact)), 1.0)
        )

        st.caption(
            f"Impact : {impact:.6f}"
        )

    with st.expander(
        "View Complete Explanation"
    ):

        st.dataframe(
            explanation,
            use_container_width=True,
        )