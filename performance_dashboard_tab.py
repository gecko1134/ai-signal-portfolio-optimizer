import streamlit as st
from performance_tracker import get_performance_tracking

def render_performance_dashboard():
    st.title("Performance Dashboard")

    portfolio_type = st.selectbox("Portfolio Type", ["Growth", "Income", "Balanced"])
    market_ytd = st.number_input("Market YTD Return (%)", value=8.0) / 100
    current_ytd = st.number_input("Your Portfolio YTD Return (%)", value=6.0) / 100

    if st.button("Evaluate"):
        results = get_performance_tracking(portfolio_type, current_ytd, market_ytd)
        for k, v in results.items():
            st.write(f"{k}: {v}")