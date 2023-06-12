import pandas as pd 
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt


st.title("APPLICATION DE DISTRIBUTION NORMALE")
data=np.random.normal(size=1000)
data=pd.DataFrame(data,columns=["Dist"])


fig, ax=plt.subplots()

#Recuperer du texte et rendre le graph dyynamique 
n_bins = st.number_input(
    label = "Choisissez un nombre de bins", 
    min_value=10, 
    value=20
) 
ax.hist(data.Dist,bins=n_bins)
graph_title = st.text_input(label="Donner un nom à cet hystographe") 
plt.title(graph_title)
st.pyplot(fig)
