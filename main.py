
import streamlit as st
from unified_client_report_tab import render_unified_report
from client_behavioral_quiz_tab import render_behavior_quiz
from portfolio_upload_tab import render_portfolio_upload
from portfolio_optimizer_tab import render_optimizer
from performance_dashboard_tab import render_performance_dashboard
from performance_comparison_tab import render_performance_comparison
from technical_analysis_tab import render_technical_analysis

st.set_page_config(page_title="Signal Dashboard", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "continue_to_dashboard" not in st.session_state:
    st.session_state.continue_to_dashboard = False

if not st.session_state.authenticated:
    st.title("Welcome to the Signal System")
    password = st.text_input("Enter password to continue", type="password")
    if password == "admin123":
        st.session_state.authenticated = True
        st.success("✅ Access granted. Click below to continue.")
    elif password:
        st.error("❌ Incorrect password.")
    st.stop()

if not st.session_state.continue_to_dashboard:
    st.title("Welcome to the Signal System")
    st.success("✅ Access granted.")
    if st.button("Continue to Dashboard"):
        st.session_state.continue_to_dashboard = True
    else:
        st.stop()

PAGES = {
    "Unified Client Report": render_unified_report,
    "Client Behavioral Questionnaire": render_behavior_quiz,
    "Upload & Analyze Portfolio": render_portfolio_upload,
    "AI Portfolio Optimizer": render_optimizer,
    "AI Performance Dashboard": render_performance_dashboard,
    "Performance: Change vs Hold": render_performance_comparison,
    "Technical Analysis": render_technical_analysis
}

st.sidebar.title("📊 Navigation")
selection = st.sidebar.radio("Choose a page", list(PAGES.keys()))
PAGES[selection]()
