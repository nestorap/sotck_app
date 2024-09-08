##### Esta es la aplicación de stock
# Importamos librerias
import pandas as pd
import numpy as np

# Librerías de stock
import yfinance as yf # Yahoo
# Vantage

# Librerias de graficos
import plotly.express as px

# Librerías de la app
import streamlit as st

# Iniciamos el título de la app
st.title("Stock App")

# Ponemos las pestañas principales
general, acciones = st.tabs(["Información general", "Acciones"])

with general:
    st.header("Información general")



with acciones:
    st.header("Acciones")
    st.subheader("Información general de la acción")
    # Añadimos el buscador del ticker
    ticker = st.sidebar.text_input("Ticker") # Buscamos el ticker
    start_date = st.sidebar.date_input("Start date") # Fecha primera
    end_date = st.sidebar.date_input("End date") # Fecha final

    # Leemos la data
    df = yf.download(ticker, start=start_date, end=end_date)

    # Subpestañas
    sub_tab = st.selectbox("Tipo de análisis", ["Información general", "Análisis fundamental", "Análisis técnico"])
    if sub_tab == "Información general":
        st.write("Aquí va la info general")
        fig = px.line(df, x=df.index, y=df.loc[:,"Adj Close"], title=ticker)
        st.plotly_chart(fig)
        # TODO
        # Tengo que incluir el riesgo, la desviación y las 10 noticias mas relevantes
    if sub_tab == "Análisis fundamental":
        st.write("Aquí añadimos la info fundamental")
        # Incluir info de alpha vantage

    if sub_tab  == "Análisis técnico":
        st.write("Aquí vemos la info técnica")
        # Incluir gráficos con distintos análisis técnicos. Pensar en incluir sección de lo que dice cada uno
