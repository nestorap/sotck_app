##### Esta es la aplicación de stock
# Importamos librerias
import pandas as pd
import numpy as np

# Libterías de entorno
import os
from dotenv import load_dotenv

# Librerías de stock
import yfinance as yf # Yahoo
from alpha_vantage.fundamentaldata import FundamentalData

# Librerias de graficos
import plotly.express as px

# Librerías de la app
import streamlit as st

# Cargamos variables de entorno
load_dotenv()
api_key = os.getenv("API_KEY")

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
        # Incluimos información de la data
        df2 = df.copy() # Copiamos el dataframe con el precio
        df2["% Change"] = df2.loc[:,"Adj Close"] / df2.loc[:,"Adj Close"].shift(1) - 1
        df2.dropna(inplace=True) # Borramos la fila nula que se genera en la linea anterior

        annual_return = df2.loc[:,"% Change"].mean() * 252 * 100 # Multiplicamos por 252 que son los dias laborales de año
        st.write(f"El retorno anual es {annual_return}%")
        stdev = np.std(df2.loc[:,"% Change"]) * np.sqrt(252)
        st.write(f"La desviación estandar es {stdev * 100}%")
        st.write(f"Risk Ad. Return es {annual_return/(stdev*100)}")
        # TODO
        # Tengo que incluir el riesgo, la desviación y las 10 noticias mas relevantes
    if sub_tab == "Análisis fundamental":
        # Instanciamos fundamentaldata
        fd = FundamentalData(api_key, output_format="pandas")
        st.subheader("Tabla de Balance anual")
        # Descargamos la data
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
        st.write("Cuenta de pérdidas y ganancias")
        income_statement = fd.get_income_statement_annual(ticker)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])

        # Convertimos las columnas a floats
        is1_num = is1.apply(pd.to_numeric, errors="coerce")
        styled_is1 = is1_num.style.background_gradient(cmap="coolwarm")
        st.write(styled_is1)
        st.write("Aquí añadimos la info fundamental")
        # Incluir info de alpha vantage

    if sub_tab  == "Análisis técnico":
        st.write("Aquí vemos la info técnica")
        # Incluir gráficos con distintos análisis técnicos. Pensar en incluir sección de lo que dice cada uno
