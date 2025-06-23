import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la aplicación
st.header('Análisis de Anuncios de Venta de Vehículos en EE.UU.')

# Botón para construir un histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para la variable "odometer" (kilometraje)')
    fig_hist = px.histogram(df, x='odometer', title='Distribución del Kilometraje (Odometer)')
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('🔍 Gráfico de dispersión: Precio vs. Año del modelo')
    fig_scatter = px.scatter(
        df, x='model_year', y='price', color='condition',
        title='Relación entre el Precio y el Año del Modelo',
        labels={'model_year': 'Año del Modelo', 'price': 'Precio (USD)'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)