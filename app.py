#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:05:05 2023

@author: KimChanYoung
"""

import streamlit
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from datetime import datetime
from tensorflow.keras.models import load_model

streamlit.title ("Stock Trend Prediction")

user_input_ticker = streamlit.text_input ("Enter Stock Ticker", "AAPL")

start = '2010-01-01' # further modify to drop down menu 
end = '2019-12-31' 

df_downloaded = yf.download(user_input_ticker, start = start, end = end, progress=False)

# Quick Description of Data
streamlit.subheader (f"{user_input_ticker} Stock Data for {start} -- {end}")
streamlit.write (df_downloaded.describe())

#working_df = (df_downloaded.reset_index()).drop(['Date', 'Adj Close'], axis = 1)