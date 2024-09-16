import pandas as pd
import yfinance as yf
from datetime import datetime
import plotly.express as px
import streamlit as st

@st.cache
def load_data(start_date, end_date, selected_tickers):
    df_list = []

    for ticker in selected_tickers:
        data = yf.download(ticker, start=start_date, end=end_date)
        df_list.append(data)

    df = pd.concat(df_list, keys=selected_tickers, names=['Ticker', 'Date'])
    df = df.reset_index()

    df['MA10'] = df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0, drop=True)
    df['MA20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)
    df['Volatility'] = df.groupby('Ticker')['Close'].pct_change().rolling(window=10).std().reset_index(0, drop=True)

    return df

def main():
    st.title("Tech Stocks Performance Analysis")

    # Date selection
    start_date = st.date_input("Start Date", datetime.now() - pd.DateOffset(months=3))
    end_date = st.date_input("End Date", datetime.now())

    if start_date >= end_date:
        st.error("End Date must be greater than Start Date.")
        return

    # Stock selection
    selected_tickers = st.multiselect("Select Stocks", ['AAPL', 'MSFT', 'NFLX', 'GOOG','AMZN','NVDA','TSLA','META','ADBE'])

    if not selected_tickers:
        st.warning("Please select at least one stock.")
        return

    df = load_data(start_date, end_date, selected_tickers)

    # Plot stock market performance
    fig1 = px.line(df, x='Date', y='Close', color='Ticker', title="Stock Market Performance for the Selected Dates")
    st.plotly_chart(fig1)

    # Plot stock prices
    fig2 = px.area(df, x='Date', y='Close', color='Ticker',
                   facet_col='Ticker',
                   labels={'Date': 'Date', 'Close': 'Closing Price', 'Ticker': 'Company'},
                   title='Stock Prices for Selected Stocks')
    st.plotly_chart(fig2)

    # Volatility
    fig3 = px.line(df, x='Date', y='Volatility',
                   color='Ticker',
                   title='Volatility of Selected Stocks')
    st.plotly_chart(fig3)

if __name__ == '__main__':
    main()
