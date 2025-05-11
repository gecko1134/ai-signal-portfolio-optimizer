import streamlit as st
import pandas as pd
from portfolio_analyzer import analyze_uploaded_portfolio
from etf_model_manager import ETF_MODELS

def render_portfolio_upload():
    st.title("Upload and Analyze Portfolio")
    uploaded_file = st.file_uploader("Upload CSV with Ticker and Weight (%)", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "Ticker" in df.columns and "Weight (%)" in df.columns:
            st.dataframe(df)
            summary = analyze_uploaded_portfolio(df, ETF_MODELS)

            st.write(f"Total Holdings: {summary['Total Holdings']}")
            st.write(f"Total Weight: {summary['Total Weight']}%")
            st.subheader("Suggested Allocation")
            for t, w in summary["Suggested Allocation"].items():
                st.write(f"{t}: {w}%")