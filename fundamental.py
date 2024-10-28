import streamlit as st
from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd

def obtener_balance_sheet(fd, ticker):
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    return bs

def obtener_income_statement(fd, ticker):
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    return is1.apply(pd.to_numeric, errors="coerce")

def mostrar_analisis_fundamental(api_key, ticker):
    fd = FundamentalData(api_key, output_format="pandas")
    st.subheader("Tabla de Balance anual")
    
    balance_sheet = obtener_balance_sheet(fd, ticker)
    st.write(balance_sheet)
    
    st.write("Cuenta de pérdidas y ganancias")
    income_statement = obtener_income_statement(fd, ticker)
    styled_is1 = income_statement.style.background_gradient(cmap="coolwarm")
    st.write(styled_is1)
