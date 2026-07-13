"""
Explainability Component.
"""

from __future__ import annotations

import streamlit as st
import plotly.express as px


def render_explanation(result: dict) -> None:

    explanation = result.get("explanation")

    if explanation is None:
        st.warning("Explanation not available.")
        return

    st.divider()
    st.header("🧠 AI Explainability")

    st.markdown(
        "Top features influencing the model prediction."
    )

    explanation = explanation.head(10)

    st.dataframe(
        explanation,
        width="stretch",
    )

    fig = px.bar(
        explanation,
        x="Impact",
        y="Feature",
        orientation="h",
        color="Impact",
        color_continuous_scale="RdYlGn_r",
        title="Top Feature Contributions",
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=500,
    )

    st.plotly_chart(
        fig,
        width="stretch",
    )