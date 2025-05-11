
import streamlit as st
import yfinance as yf

def render_technical_analysis():
    st.title("Technical Analysis Dashboard")
    ticker = st.text_input("Enter Ticker Symbol", value="SPY")
    data = yf.download(ticker, period="6mo", interval="1d")
    if not data.empty:
        st.line_chart(data["Close"])
    else:
        st.error("Failed to load data. Check ticker symbol.")
