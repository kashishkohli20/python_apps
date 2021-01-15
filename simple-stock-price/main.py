import yfinance as yf
import streamlit as st
import pandas as pd

# header of the web application
st.write("""
# Simple Stock Price App

Showing the ***volume*** and ***closing prices*** of Google

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historic data for the ticker
tickerDf = tickerData.history(period='1d', start='2010-05-01', end='2020-09-01')

# visualizing the close price and volume
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)