"""
Analytics Component.
"""

from __future__ import annotations

import pandas as pd
import streamlit as st
import plotly.express as px

def render_analytics(dataframe: pd.DataFrame):

    st.divider()

    st.header("📊 Analytics")

    total = len(dataframe)

    fraud = int(dataframe["Prediction"].sum())

    legitimate = total - fraud

    fraud_rate = (fraud / total) * 100 if total else 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Records",
            total,
        )

    with col2:
        st.metric(
            "Fraud",
            fraud,
        )

    with col3:
        st.metric(
            "Legitimate",
            legitimate,
        )

    with col4:
        st.metric(
            "Fraud Rate",
            f"{fraud_rate:.2f}%",
        )

        st.divider()

        st.subheader("🥧 Fraud Distribution")

        distribution = dataframe["Prediction"].value_counts()

        labels = {
            0: "Legitimate",
            1: "Fraud",
        }

        fig = px.pie(
            names=[labels[x] for x in distribution.index],
            values=distribution.values,
            hole=0.45,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )
        st.subheader("📈 Fraud Probability Distribution")

        fig = px.histogram(
            dataframe,
            x="Fraud Probability",
            nbins=30,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

        st.subheader("📊 Prediction Counts")

        counts = dataframe["Prediction"].value_counts()

        fig = px.bar(

            x=[
                "Legitimate",
                "Fraud",
            ],

            y=[
            counts.get(0, 0),
            counts.get(1, 0),
            ],

            labels={
            "x": "Prediction",
            "y": "Count",
            },
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )