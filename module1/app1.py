import streamlit as st 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data=np.random.normal(size=1000)
data=pd.DataFrame(data,columns=["Dist"])

#Afficher quelques choses
st.write(data.head()) 

#Afficher un histogramme
fig, ax = plt.subplots()
ax.hist(data.Dist)
st.pyplot() 

#Recuperer du texte et rendre le graph dyynamique 
n_bins = st.number_input(
    label = "Choisissez un nombre de bins", 
    min_value=10, 
    value=20
) 
ax.hist(data.Dist, bins = n_bins)