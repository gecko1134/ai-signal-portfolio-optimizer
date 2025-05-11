import streamlit as st
import yfinance as yf

def render_technical_analysis():
    st.title("Technical Analysis")
    ticker = st.text_input("Enter Ticker", "SPY")

    if st.button("Get Chart"):
        data = yf.download(ticker, period="6mo", interval="1d")
        if not data.empty:
            st.line_chart(data["Close"])
        else:
            st.error("No data found.")