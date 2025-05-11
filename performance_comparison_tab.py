
import streamlit as st
from performance_tracker import get_performance_tracking

def render_performance_comparison():
    st.title("Performance: Change vs Hold Scenario Comparison")

    portfolio_type = st.selectbox("Select Portfolio Type", ["Growth", "Income", "Balanced"])
    market_ytd = st.number_input("Market YTD Return (%)", value=7.0, step=0.1) / 100

    st.subheader("Scenario 1: No Change (Current Allocation)")
    current_ytd_return_hold = st.number_input("Current YTD Return (Hold Scenario) %", value=4.5, step=0.1) / 100
    results_hold = get_performance_tracking(portfolio_type, current_ytd_return_hold, market_ytd)

    st.subheader("Scenario 2: Make Changes (Revised Allocation)")
    current_ytd_return_change = st.number_input("Expected YTD Return (Adjusted Scenario) %", value=6.5, step=0.1) / 100
    results_change = get_performance_tracking(portfolio_type, current_ytd_return_change, market_ytd)

    st.markdown("### Comparison Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Hold Scenario")
        for k, v in results_hold.items():
            st.write(f"{k}: {v}")
    with col2:
        st.markdown("#### Adjusted Scenario")
        for k, v in results_change.items():
            st.write(f"{k}: {v}")
