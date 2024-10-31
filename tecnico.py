
import numpy as np
#import talib as ta
import pandas as pd
import pandas_ta as ta
import streamlit as st
import plotly.express as px


def mostrar_analisis_tecnico(ticker:str, df:pd.DataFrame):
    st.subheader(f"Análisis técnico de {ticker}")
    df1 = pd.DataFrame()
    wind_list = df1.ta.indicators(as_list=True)
#    st.write(wind_list)
    technical_indicator = st.selectbox("Indicadores técnicos", options=wind_list)
    method = technical_indicator
    indicator = pd.DataFrame(getattr(ta, method)(
        low=df["Low"],
        close=df["Close"],
        high=df["High"],
        open=df["Open"],
        volume=df["Volume"],
        )
            )
    indicator["Close"] = df["Close"]
    figw_ind_new = px.line(indicator)
    st.plotly_chart(figw_ind_new)
    st.write(indicator)
    # Añadir el análisis técnico según sea necesario.
