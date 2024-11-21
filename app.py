import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos")

# Encabezado
st.header("Dashboard de Vehículos")

# Checkbox para histograma
show_hist = st.checkbox('Mostrar Histograma de Precios')
if show_hist:
    fig_hist = px.histogram(car_data, x='price', nbins=50, title='Distribución de Precios')
    st.plotly_chart(fig_hist)

# Checkbox para gráfico de dispersión
show_scatter = st.checkbox('Mostrar Relación Precio vs Año')
if show_scatter:
    fig_scatter = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año del Modelo')
    st.plotly_chart(fig_scatter)