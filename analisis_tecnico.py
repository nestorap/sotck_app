
# Imprtamos librerias
import numpy as np
import pandas as pd
import streamlit as st

# Librerías de stock
import yfinance as yf
from lightweight_charts.widgets import StreamlitChart

#### Funciones ######
# Media
def calculate_sma(df:pd.DataFrame, period:int=50)-> pd.DataFrame:
    return pd.DataFrame(
        {
            'time': df.index,
            f'SMA {period}' : df.loc[:,'close'].rolling(window=period).mean()
        }
    ).dropna()


# Iniciamos la app
st.title("Análisis técnico")

# Ponemos la barra de búsqueda
ticker = st.sidebar.text_input("Ticker")
start_date = st.sidebar.date_input("Start date")
end_date = st.sidebar.date_input("End date")

# Descargamos la data
df = yf.download(ticker, start=start_date, end=end_date)

# Limpiamos el df para quitar el multi index
rename_columns = {'Open' : 'open', 
                  'High':  'high', 
                  'Low' : 'low', 
                  'Close' : 'close', 
                  'Adj Close' : 'adj close', 
                  'Volume' : 'volume'}
df.rename(columns=rename_columns, inplace=True)
df.columns = df.columns.droplevel('Ticker')

## Calculamos las medias
sma50 = calculate_sma(df=df, period=50)
sma200 = calculate_sma(df=df, period=200)

# Medias para el macd
df['EMA12'] = df.loc[:,'close'].ewm(span=12, adjust=False).mean()
df['EMA26'] = df.loc[:,'close'].ewm(span=26, adjust=False).mean()
df['MACD'] = df.loc[:,'EMA12'] - df.loc[:,'EMA26']
df['signal_line'] = df.loc[:,'MACD'].ewm(span=9, adjust=False).mean()
df['histogram'] = df.loc[:,'MACD'] - df.loc[:,'signal_line']


# Pintamos el gráfico
chart = StreamlitChart(width=1325, height=800, toolbox=True)
chart.set(df)

## Medias
line50 = chart.create_line('SMA 50', color='green')
line200 = chart.create_line('SMA 200', color='purple')
line50.set(sma50)
line200.set(sma200)

# Aquí va el código para pintar el MACD
chart.load()


