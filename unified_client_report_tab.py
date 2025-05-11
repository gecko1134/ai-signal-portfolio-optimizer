import streamlit as st
import pandas as pd
from behavioral_questionnaire import QUESTIONS, calculate_behavior_score
from portfolio_analyzer import analyze_uploaded_portfolio
from etf_model_manager import ETF_MODELS
from combined_pdf_generator import CombinedPDFReport
import tempfile

def render_unified_report():
    st.title("Unified Client Report")

    responses = []
    raw_responses = []

    st.subheader("Step 1: Behavioral Questionnaire")
    for q in QUESTIONS:
        choice = st.radio(q["question"], list(q["options"].keys()), key=q["question"])
        responses.append(q["options"][choice])
        raw_responses.append((q["question"], choice))

    st.subheader("Step 2: Upload Client Portfolio")
    uploaded_file = st.file_uploader("Upload CSV (Ticker, Weight %)", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "Ticker" in df.columns and "Weight (%)" in df.columns:
            st.dataframe(df)
            summary = analyze_uploaded_portfolio(df, ETF_MODELS)
        else:
            st.error("CSV must contain 'Ticker' and 'Weight (%)'")
            return
    else:
        st.stop()

    if st.button("Generate Unified Client PDF Report"):
        profile, score = calculate_behavior_score(responses)
        if profile == "Steady Sam":
            recs = ["Conservative allocation", "Strong income focus", "Quarterly or annual communication"]
        elif profile == "Anxious Alex":
            recs = ["Moderate allocation", "Risk reduction strategies", "Regular check-ins"]
        else:
            recs = ["Growth-oriented allocation", "Tactical overlays", "Minimal communication unless needed"]

        pdf = CombinedPDFReport()
        pdf.add_behavior_section(profile, score, recs, raw_responses)
        pdf.add_portfolio_section(summary, df)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            pdf.output(tmp.name)
            tmp.seek(0)
            st.download_button("📄 Download Unified Client Report", tmp.read(), file_name="Unified_Client_Report.pdf")