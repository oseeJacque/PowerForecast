from sources.data_getter import load_dataset
from sources.featuring import create_datetime_features
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


    
np.random.seed(42)
data = {
    'Colonne1': np.random.randint(0, 100, 100),
    'Colonne2': np.random.rand(100)
}

# Créer le DataFrame
df = pd.DataFrame(data)


def exploration():
    st.title("Exploration")
    st.subheader("Une petite description")

    # Layout en lignes
    col1, col2, col3 = st.columns([1, 1, 1])

    # Ligne 1 - Colonnes distinctes
    with col1:
        st.subheader("ZONE 1")
        afficher_graphique1()

    with col2:
        st.subheader("ZONE 2")
        afficher_graphique2()

    with col3:
        st.subheader("ZONE 3")
        afficher_graphique3()

    # Ligne 2 - Une colonne
    st.subheader("Graphique 4")
    afficher_graphique4()

    # Lignes suivantes - Au moins une colonne
    st.subheader("Graphiques supplémentaires")
    afficher_graphiques_supplementaires()

#Consommation de la zone1
def afficher_graphique1():
    # Graphique 1
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Mettre la column DateTime comme une 
    data.reset_index(inplace=True)
    
    # Afficher l'histogramme
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    sns.histplot(data=data, x="Zone 1 Power Consumption", stat="percent", kde=True, ax=ax)

    ax.set_xlabel('Power consumption (KW)')
    ax.set_ylabel('Pourcentage de répartition (%)')
    ax.set_title("Histogramme de la consommation d'énergie zone 1")
    # Augmenter la taille de la police des légendes
    ax.legend(fontsize=16)
    # Afficher le graphe dans Streamlit
    st.pyplot(fig)
    
    #Consommation de la zone2
def afficher_graphique2():
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Mettre la column DateTime comme une 
    data.reset_index(inplace=True)
    
    # Afficher l'histogramme
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    sns.histplot(data=data, x="Zone 2 Power Consumption", stat="percent", kde=True, ax=ax)

    ax.set_xlabel('Power consumption (KW)')
    ax.set_ylabel('Pourcentage de répartition (%)')
    ax.set_title("Histogramme de la consommation d'énergie zone 2")
    # Augmenter la taille de la police des légendes
    ax.legend(fontsize=12)
    # Afficher le graphe dans Streamlit
    st.pyplot(fig)


def afficher_graphique3():
    # Graphique 3
    #Consommation de la zone1 3
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Mettre la column DateTime comme une 
    data.reset_index(inplace=True)
    
    # Afficher l'histogramme
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1)
    sns.histplot(data=data, x="Zone 3 Power Consumption", stat="percent", kde=True, ax=ax)

    ax.set_xlabel('Power consumption (KW)')
    ax.set_ylabel('Pourcentage de répartition (%)')
    ax.set_title("Histogramme de la consommation d'énergie zone 3")
    # Augmenter la taille de la police des légendes
    ax.legend(fontsize=12)
    # Afficher le graphe dans Streamlit
    st.pyplot(fig)


def afficher_graphique4():
    # Graphique 4
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Mettre la column DateTime comme une 
    data.reset_index(inplace=True)
    
    # Afficher le graphique
    plt.figure(figsize=(16, 8))
    data_feature = data[["Zone 1 Power Consumption", "Zone 2 Power Consumption", "Zone 3 Power Consumption"]]
    sns.boxplot(data=data_feature)
    
    # Ajouter un titre et un sous-titre
    plt.title("Boxplot des consommations par zone")
    plt.xlabel("Zone")
    plt.ylabel("Power Consumption (KW)")
    
    st.pyplot(plt)


def afficher_graphiques_supplementaires():
    
    # Graphique 5
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Mettre la column DateTime comme une 
    data.reset_index(inplace=True)
    # Calculer la somme de consommation pour chaque zone
    zone1_total = data["Zone 1 Power Consumption"].sum()
    zone2_total = data["Zone 2 Power Consumption"].sum()
    zone3_total = data["Zone 3 Power Consumption"].sum()

    # Créer les labels et les valeurs pour le pie chart
    labels = ["Zone 1", "Zone 2", "Zone 3"]
    values = [zone1_total, zone2_total, zone3_total]

    # Créer le pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Assurer que le pie chart est un cercle

    # Ajouter un titre
    ax.set_title("Répartition de la consommation d'énergie par zone au cours de l'année 2017")

    # Afficher le pie chart dans Streamlit
    st.pyplot(fig)




