
import streamlit as st
import tempfile
from behavioral_questionnaire import QUESTIONS, calculate_behavior_score
from pdf_generator import PDFReport

st.title("Client Behavioral Questionnaire with PDF Export")

responses = []
raw_responses = []

for q in QUESTIONS:
    choice = st.radio(q["question"], list(q["options"].keys()), key=q["question"])
    responses.append(q["options"][choice])
    raw_responses.append((q["question"], choice))

if st.button("Submit Assessment"):
    profile, score = calculate_behavior_score(responses)
    st.success(f"Identified Behavioral Profile: **{profile}** (Score: {score})")

    st.markdown("### Recommended Action")
    if profile == "Steady Sam":
        recs = ["Conservative allocation", "Strong income focus", "Quarterly or annual communication"]
        st.write(" - Conservative allocation with strong income focus and clear communication.")
    elif profile == "Anxious Alex":
        recs = ["Moderate allocation", "Risk reduction strategies", "Regular check-ins"]
        st.write(" - Moderate allocation with regular reviews and risk-reducing tactics.")
    elif profile == "Confident Casey":
        recs = ["Aggressive growth focus", "Tactical overlays", "Minimal communication unless needed"]
        st.write(" - Growth-oriented allocation with occasional updates and tactical flexibility.")
    else:
        recs = ["Standard portfolio plan"]

    if st.button("Generate PDF Summary"):
        pdf = PDFReport()
        pdf.add_client_profile(profile, score, recs, raw_responses)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            pdf.output(tmp.name)
            tmp.seek(0)
            st.download_button(
                label="📄 Download Behavioral Summary PDF",
                data=tmp.read(),
                file_name="Behavioral_Profile_Report.pdf",
                mime="application/pdf"
            )
