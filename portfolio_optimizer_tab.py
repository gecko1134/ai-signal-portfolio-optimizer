
import streamlit as st
from etf_model_manager import ETF_MODELS, suggest_replacements

def render_optimizer():
    st.title("AI Portfolio Optimizer")

    model_name = st.selectbox("Select ETF Portfolio Model", list(ETF_MODELS.keys()))
    current_portfolio = ETF_MODELS.get(model_name, {})

    st.subheader("Current Portfolio Allocation")
    for etf, weight in current_portfolio.items():
        st.write(f"{etf}: {weight*100:.1f}%")

    st.subheader("AI Optimization Suggestions")
    recommendations = suggest_replacements(model_name)

    if recommendations:
        for etf, replacement in recommendations.items():
            st.warning(f"Consider replacing {etf} with {replacement}")
    else:
        st.success("No replacements needed. Portfolio is optimized.")
