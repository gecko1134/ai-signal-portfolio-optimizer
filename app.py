
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

if not st.session_state.authenticated:
    st.title("🔐 Login Required")
    password = st.text_input("Enter password to continue", type="password")
    login_button = st.button("Login")
    if login_button:
        if password == "admin123":
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Incorrect password.")
else:
    st.sidebar.title("📊 Navigation")
    PAGES = {
        "Unified Client Report": render_unified_report,
        "Client Behavioral Questionnaire": render_behavior_quiz,
        "Upload & Analyze Portfolio": render_portfolio_upload,
        "AI Portfolio Optimizer": render_optimizer,
        "AI Performance Dashboard": render_performance_dashboard,
        "Performance: Change vs Hold": render_performance_comparison,
        "Technical Analysis": render_technical_analysis
    }
    selection = st.sidebar.radio("Choose a page", list(PAGES.keys()))
    PAGES[selection]()
