
import streamlit as st
import pandas as pd
import tempfile
from portfolio_analyzer import analyze_uploaded_portfolio
from etf_model_manager import ETF_MODELS
from pdf_generator import PortfolioPDFReport

st.title("Upload Portfolio for AI Analysis + PDF Export")

st.markdown("Upload a CSV file with two columns: **Ticker** and **Weight (%)**")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Portfolio")
    st.dataframe(df)

    if "Ticker" in df.columns and "Weight (%)" in df.columns:
        summary = analyze_uploaded_portfolio(df, ETF_MODELS)

        st.subheader("AI Summary and Recommendations")
        st.write(f"Total Holdings: {summary['Total Holdings']}")
        st.write(f"Total Weight: {summary['Total Weight']}%")

        st.markdown("### Overweight Holdings")
        for item in summary["Overweight Assets"]:
            st.warning(f"{item[0]} is overweight by {item[1]}%")

        st.markdown("### Underweight Holdings")
        for item in summary["Underweight Assets"]:
            st.info(f"{item[0]} is underweight by {item[1]}%")

        st.markdown("### Missing From Model")
        for m in summary["Missing from Model"]:
            st.error(f"{m} is missing from model")

        st.markdown("### Suggested Allocation Based on Model")
        for t, w in summary["Suggested Allocation"].items():
            st.write(f"{t}: {w}%")

        # Generate PDF
        if st.button("Generate PDF Report"):
            pdf = PortfolioPDFReport()
            pdf.add_portfolio_summary(summary, df)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                pdf.output(tmp.name)
                tmp.seek(0)
                st.download_button(
                    label="📄 Download PDF Report",
                    data=tmp.read(),
                    file_name="Portfolio_Analysis_Report.pdf",
                    mime="application/pdf"
                )
    else:
        st.error("CSV must contain 'Ticker' and 'Weight (%)' columns.")
