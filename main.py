
import streamlit as st
from dotenv import load_dotenv
import os

# Importa las funciones de cada módulo
from general import mostrar_informacion_general
from acciones import mostrar_acciones
from fundamental import mostrar_analisis_fundamental
from tecnico import mostrar_analisis_tecnico

# Cargamos variables de entorno
load_dotenv()
api_key = os.getenv("API_KEY")

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
    
    # Verifica si el ticker y las fechas están presentes antes de mostrar el contenido
    if ticker and start_date and end_date:
        sub_tab = st.selectbox("Tipo de análisis", ["Información general", "Análisis fundamental", "Análisis técnico"])
        
        if sub_tab == "Información general":
            mostrar_acciones(ticker, start_date, end_date)
        
        elif sub_tab == "Análisis fundamental":
            mostrar_analisis_fundamental(api_key, ticker)
        
        elif sub_tab == "Análisis técnico":
            mostrar_analisis_tecnico()
    else:
        st.write("Por favor, ingrese un ticker y seleccione un rango de fechas.")
