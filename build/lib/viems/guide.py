from sources.featuring import create_datetime_features
from sources.data_getter import load_dataset
import streamlit as st

def guide():
   # Code de la page de détails
    st.title("Documentation")
    st.write("""Les données utilisées dans ce projet sont collectées à partir de [source des données]. 
             Elles comprennent des informations sur la consommation d'énergie passée, les facteurs météorologiques, les jours fériés, etc.
             """)
    
    st.write(" ***Affichage des 5 premières observations de la base de données***")
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Afficharge par de la consommation par moi
    data.reset_index(inplace=True)
    st.write(data.head())

    st.write("""
        ### Compréhension des Caractéristiques
        **'DateTime'** : Cette colonne représente la date et l'heure à laquelle les données ont été enregistrées. Elle sert d'indicateur temporel pour chaque observation.

        **'Temperature'** : Cette colonne indique la température enregistrée à un moment donné. Elle est mesurée en degrés Celsius (°C) .

        **'Humidity'** : Cette colonne représente le niveau d'humidité ambiant enregistré lors de chaque observation. L'humidité est exprimée en pourcentage et indique la quantité de vapeur d'eau présente dans l'air.
            
        **'Wind Speed'** : Cette colonne indique la vitesse du vent enregistrée au moment de la mesure. La vitesse du vent est mesurée en mètres par seconde (m/s)
            
        **'general diffuse flows'** : Cette colonne peut faire référence à un flux de lumière diffusée dans l'environnement (Question sur cette colonne)
            
        **'diffuse flows'** : De manière similaire à la colonne précédente, cette colonne peut faire référence à un autre type de flux diffus. (les données de retour de flux pas très important)
            
        **'Zone 1 Power Consumption'** : Cette colonne indique la puissance de consommation électrique enregistrée dans la zone 1. Elle représente la quantité d'électricité consommée à un moment donné dans cette zone spécifique.
            
        **'Zone 2 Power Consumption'** : Cette colonne représente la puissance de consommation électrique enregistrée dans la zone 2. Elle indique la quantité d'électricité consommée à un moment donné dans cette zone spécifique.
            
        **'Zone 3 Power Consumption'** : Cette colonne indique la puissance de consommation électrique enregistrée dans la zone 3. Elle représente la quantité d'électricité consommée à un moment donné dans cette zone spécifique. 

        ## Algorithme de prédiction
        Nous utilisons [algorithme utilisé] pour prédire la consommation d'énergie future.
        Cet algorithme est entraîné sur des données historiques pour estimer la demande énergétique future en fonction de différents paramètres.

        ## Contact
        Pour toute question ou suggestion, veuillez contacter [nos adresses e-mails].
        """)