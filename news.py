# Librerías
import numpy as np
import pandas as pd
from stocknews import StockNews

def news(ticker):
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    return df_news


