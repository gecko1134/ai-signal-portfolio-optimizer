import streamlit as st
from performance_tracker import get_performance_tracking

def render_performance_comparison():
    st.title("Compare Hold vs Change")

    portfolio_type = st.selectbox("Portfolio Type", ["Growth", "Income", "Balanced"])
    market_ytd = st.number_input("Market YTD Return (%)", value=8.0) / 100
    hold_ytd = st.number_input("Hold Strategy YTD Return (%)", value=5.0) / 100
    new_ytd = st.number_input("Change Strategy YTD Return (%)", value=6.5) / 100

    hold = get_performance_tracking(portfolio_type, hold_ytd, market_ytd)
    new = get_performance_tracking(portfolio_type, new_ytd, market_ytd)

    st.subheader("Hold Scenario")
    for k, v in hold.items():
        st.write(f"{k}: {v}")

    st.subheader("Change Scenario")
    for k, v in new.items():
        st.write(f"{k}: {v}")