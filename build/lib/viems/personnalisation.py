from sources.data_analysis import display_consumption_daily
from sources.data_analysis import display_consumption_monthly
from sources.featuring import create_datetime_features
from sources.data_getter import load_dataset
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Recuperation de la dataset
#data=load_dataset()
#Générer un DataFrame aléatoire
np.random.seed(42)
data = {
    'Jours': np.random.randint(1, 32, 100),
    'Mois': np.random.randint(1, 13, 100),
    'Période': np.random.randint(1, 6, 100)
}
df = pd.DataFrame(data)

def personnalisation():
    st.title("Interface de personnalisation")
    choix = st.radio("Choix", ("Jours", "Mois", "Période"))

    if choix == "Période":
        st.subheader("Période sélectionnée")
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Début de la période")
            debut_periode = st.date_input("Sélectionnez la date de début")

        with col2:
            st.subheader("Fin de la période")
            fin_periode = st.date_input("Sélectionnez la date de fin")

        consommation_periodique(date_debut =debut_periode ,date_fin =fin_periode )

    elif choix == "Jours":
        st.markdown("---")
        # Demander à l'utilisateur de saisir un entier entre 0 et 7
        day_num = st.number_input("Entrez un le jour", min_value=0, max_value=7, step=1)
        if day_num == 0:
            day_num = "all" 
        consommation_par_jour(nbr_jour=day_num)
        
    elif choix == "Mois":
        st.markdown("---")

        # Demander à l'utilisateur de saisir un entier entre 0 et 12
        month_num = st.number_input("Entrez le moi", min_value=0, max_value=12, step=1)
        if month_num == 0:
            month_num = "all" 
        consommation_par_moi(nbr_mois=month_num)
    

#Consommattion par jour
def consommation_par_jour(nbr_jour):
     #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Afficharge par de la consommation par moi
    data.reset_index(inplace=True)
    display_consumption_daily(df_data=data, figsize=(20, 15), day_num=nbr_jour)   


#Consommation par moi 
def consommation_par_moi(nbr_mois):
     #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Afficharge par de la consommation par moi
    data.reset_index(inplace=True)
    display_consumption_monthly(df_data=data, figsize=(20, 15), month_num=nbr_mois)
    

def consommation_periodique(date_debut,date_fin):
    print(date_debut)
    print(date_fin)
    pass
    
if __name__ == "__main__":
    personnalisation()
