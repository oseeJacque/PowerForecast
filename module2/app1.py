import pandas as pd 
import streamlit as st 
import numpy as np 
import plotly.epress as px 

st.title('Initialisation à la visualisation des donnéees')
st.subheader("SOKE Osée")
st.markdown("### Ceci est un markdown")

#Data_path 
path_data="../Datasets/Tetuan_City_power_consumption.csv"
data=pd.read_csv(path_data)
st.write(data.head()) 

#Trcer un diagramme lineaire ,juste un plot
st.line_chart(data[data.columns[1]]) 


#Tracer un diagramme à bar 
st.bar_chart(data["Zone 1 Power Consumption"],)

"""Tracer les graphique avec les librairies et le pandas"""

st.sidebar.header("Sidebar Header")

st.header("Columns") #Titré une column
cols = st.columns(3) #Déclarer  de trois columns
cols[0].write("Column 1")  #Ajouter n élément à la columnd
cols[1].write("Column 2")  #Ajouter un second élément à la column
cols[2].write("Column 3") 

#Construction de nuage de point interactif 
fig = px.bar(
    data_frame=data[data["Zone 1 Power Consumption"]], 
    
    )
