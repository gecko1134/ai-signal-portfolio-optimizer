
import streamlit as st
import importlib

st.set_page_config(page_title="Client Signal Dashboard", layout="wide")

# Basic login simulation
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("Welcome to the Signal System Dashboard")
    st.markdown("🔐 Please enter your password to continue.")
    password = st.text_input("Password", type="password")
    if password == "admin123":  # You can change this password
        st.session_state.authenticated = True
        st.success("Access granted. Loading dashboard...")
        st.experimental_rerun()
    elif password:
        st.error("Incorrect password.")
    st.stop()

# Navigation
PAGES = {
    "Unified Client Report": "unified_client_report_tab",
    "Client Behavioral Questionnaire": "client_behavioral_quiz_tab",
    "Upload & Analyze Portfolio": "portfolio_upload_tab",
    "AI Portfolio Optimizer": "portfolio_optimizer_tab",
    "AI Performance Dashboard": "performance_dashboard_tab",
    "Performance: Change vs Hold": "performance_comparison_tab",
    "Technical Analysis": "technical_analysis_tab"
}

st.sidebar.title("📊 Navigation")
selection = st.sidebar.radio("Choose a page", list(PAGES.keys()))
page = importlib.import_module(f"streamlit_app.{PAGES[selection]}")
