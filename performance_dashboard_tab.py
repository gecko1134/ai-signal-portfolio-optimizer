
import streamlit as st
from performance_tracker import get_performance_tracking

def render_performance_dashboard():
    st.title("AI Performance Dashboard & Behavioral Insights")

    portfolio_type = st.selectbox("Select Portfolio Type", ["Growth", "Income", "Balanced"])
    market_ytd = st.number_input("Market YTD Return (%)", value=8.0, step=0.1) / 100
    current_ytd = st.number_input("Your Portfolio YTD Return (%)", value=5.0, step=0.1) / 100

    if st.button("Evaluate Performance"):
        results = get_performance_tracking(portfolio_type, current_ytd, market_ytd)

        st.subheader("Performance Summary")
        st.metric("Base Target Return", f"{results['Base Target Return']}%")
        st.metric("Projected Annual Return", f"{results['Projected Annual Return']}%")
        st.metric("Return Delta vs Target", f"{results['Return Delta vs Target']}%")
        st.metric("Behavioral Risk Alert", results['Behavioral Risk Alert'])

        st.subheader("Risk & Capture Metrics")
        st.write(f"Upside Capture: **{results['Upside Capture (%)']}%**")
        st.write(f"Downside Capture: **{results['Downside Capture (%)']}%**")
