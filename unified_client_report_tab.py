
import streamlit as st
import pandas as pd
import tempfile
from modules.behavioral_questionnaire import QUESTIONS, calculate_behavior_score
from modules.etf_model_manager import ETF_MODELS
from modules.portfolio_analyzer import analyze_uploaded_portfolio
from modules.combined_pdf_generator import CombinedPDFReport

st.title("Generate Unified Client Report")

st.header("Step 1: Complete Behavioral Questionnaire")
responses = []
raw_responses = []

for q in QUESTIONS:
    choice = st.radio(q["question"], list(q["options"].keys()), key=q["question"])
    responses.append(q["options"][choice])
    raw_responses.append((q["question"], choice))

st.header("Step 2: Upload Portfolio File")
uploaded_file = st.file_uploader("Upload CSV (Ticker, Weight %)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "Ticker" in df.columns and "Weight (%)" in df.columns:
        st.dataframe(df)
        portfolio_summary = analyze_uploaded_portfolio(df, ETF_MODELS)
    else:
        st.error("CSV must contain 'Ticker' and 'Weight (%)' columns.")
        df = None
        portfolio_summary = None
else:
    df = None
    portfolio_summary = None

if st.button("Generate Unified PDF Report"):
    if df is not None and portfolio_summary is not None:
        profile, score = calculate_behavior_score(responses)
        if profile == "Steady Sam":
            recs = ["Conservative allocation", "Strong income focus", "Quarterly or annual communication"]
        elif profile == "Anxious Alex":
            recs = ["Moderate allocation", "Risk reduction strategies", "Regular check-ins"]
        elif profile == "Confident Casey":
            recs = ["Aggressive growth focus", "Tactical overlays", "Minimal communication unless needed"]
        else:
            recs = ["Standard portfolio plan"]

        pdf = CombinedPDFReport()
        pdf.add_behavior_section(profile, score, recs, raw_responses)
        pdf.add_portfolio_section(portfolio_summary, df)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            pdf.output(tmp.name)
            tmp.seek(0)
            st.download_button(
                label="📄 Download Unified Client Report PDF",
                data=tmp.read(),
                file_name="Unified_Client_Report.pdf",
                mime="application/pdf"
            )
    else:
        st.error("Please complete all steps above before generating the report.")
