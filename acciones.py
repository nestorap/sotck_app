
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np


def calcular_metricas(df):
    df2 = df.copy()
    df2["% Change"] = df2["Adj Close"] / df2["Adj Close"].shift(1) - 1
    df2.dropna(inplace=True)
    
    annual_return = df2["% Change"].mean() * 252 * 100
    stdev = np.std(df2["% Change"]) * np.sqrt(252)
    
    return annual_return, stdev

def mostrar_acciones(df:pd.DataFrame, ticker:str):
    st.subheader("Información general de la acción")
    
    if df.empty:
        st.warning("No se encontraron datos para el ticker ingresado en el rango de fechas seleccionado.")
        return
    
    fig = px.line(df, x=df.index, y="Adj Close", title=ticker)
    st.plotly_chart(fig)
    
    annual_return, stdev = calcular_metricas(df)
    st.write(f"El retorno anual es {annual_return:.2f}%")
    st.write(f"La desviación estándar es {stdev * 100:.2f}%")
    st.write(f"Risk Ad. Return es {annual_return / (stdev * 100):.2f}")
