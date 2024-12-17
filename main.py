import os
import yfinance as yf
from news import news
import streamlit as st
from dotenv import load_dotenv

# Importa las funciones de cada módulo
from acciones import mostrar_acciones
from tecnico import mostrar_analisis_tecnico
from general import mostrar_informacion_general
from fundamental import mostrar_analisis_fundamental



# Cargamos variables de entorno
load_dotenv()
api_key = os.getenv("API_KEY")
#api_ia_key = os.getenv("API_KEY_IA")

# Iniciamos el título de la app
st.title("Stock App")

# Ponemos las pestañas principales
general, acciones = st.tabs(["Información general", "Acciones"])

with general:
    mostrar_informacion_general()

with acciones:
    # Añade los inputs en la barra lateral
    ticker = st.sidebar.text_input("Ticker")
    start_date = st.sidebar.date_input("Start date")
    end_date = st.sidebar.date_input("End date")
    df = yf.download(ticker, start=start_date, end=end_date)
    # Verifica si el ticker y las fechas están presentes antes de mostrar el contenido
    if ticker and start_date and end_date:
        sub_tab = st.selectbox("Tipo de análisis", ["Información general","News", "Análisis fundamental", "Análisis técnico"])

        if sub_tab == "Información general":
            mostrar_acciones(df=df, ticker=ticker)
        elif sub_tab == "News":
            df_news = news(ticker)
            for i in range(10):
                st.subheader(f"News {i + 1}")
                st.write(df_news["published"][i])
                st.write(df_news.loc[i,"title"])
                st.write(df_news.loc[i, "summary"])
                sentiment = df_news.loc[i, "sentiment_title"]
                st.write(f"El sentimiento del títutlo --> {sentiment}")
                news_sentiment = df_news.loc[i, "sentiment_summary"]
                st.write(f"El sentimiento de la noticia es --> {news_sentiment}")


        elif sub_tab == "Análisis fundamental":
            mostrar_analisis_fundamental(api_key, ticker)

        elif sub_tab == "Análisis técnico":
            mostrar_analisis_tecnico(ticker=ticker, df=df)
    else:
        st.write("Por favor, ingrese un ticker y seleccione un rango de fechas.")
