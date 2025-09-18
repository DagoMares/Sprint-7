import pandas as pd
import plotly.express as px
import streamlit as st


# Revisión de la existencia del archivo antes de leerlo
import os
file_path = r"C:\\Users\\hunte\\OneDrive\\Escritorio\\Documentos\\TTen\\Sprint-7\\vehicles_us.csv"
if os.path.exists(file_path):
    car_data = pd.read_csv(file_path)
else:
    print(f"File not found: {file_path}")


st.header('Autos de segunda mano en venta')  # Título de la aplicación

# Checkbox para mostrar el histograma
hist_button = st.checkbox(
    'Desplegar histograma del kilometraje de los vehículos')

# Checkbox para mostrar el gráfico de dispersión
disper_button = st.checkbox(
    'Desplegar gráfico de dispersión del kilometraje vs precio')

if hist_button:
    # Selección del número de clases para el histograma
    number_bins = st.slider('Elije en no. de clases', 1, 100, 30)

    # Creación del histograma
    fig = px.histogram(car_data, x="odometer", labels={"odometer": "Kilometraje", "count": "Frecuencia"},
                       nbins=number_bins, title="Histograma del kilometraje de los vehículos")
    fig.update_layout(yaxis_title="Frecuencia")

    # Mostrar el histograma en la aplicación
    st.plotly_chart(fig, use_container_width=True)

if disper_button:
    # Crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price", color="type",
                      labels={
                          "odometer": "Kilometraje",
                          "price": "Precio (USD)",
                          "type": "Tipo de vehículo"
                      })
    fig2.update_layout(title="Dispersión del precio vs kilometraje")
    # Mostrar el gráfico de dispersión en la aplicación
    st.plotly_chart(fig2, use_container_width=True)
