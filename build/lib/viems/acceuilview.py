import streamlit as st

def acceuil():
    # Titre de la page d'accueil
    st.markdown("<h1 style='text-align: center;'>Powerforecast - Prédiction de la consommation d'énergie</h1>", unsafe_allow_html=True)

    # Chargement et affichage de l'image
    image = '../assets/powerforecast.png'
    st.image(image, caption='', use_column_width=True)

    # Description du projet
    st.write("""
        Bienvenue sur Powerforecast, un projet de prédiction de la consommation d'énergie.
        Ce projet vise à prédire la demande d'énergie en utilisant des modèles de machine learning avancés.
        Explorez les fonctionnalités et les prédictions de Powerforecast pour mieux comprendre et anticiper la consommation d'énergie.

        **Informations importantes :**
        - Données utilisées : Base de données de consommation d'electricité de la ville de Tétouan au Maroc.
        - Auteurs : [Nos noms]
        - Date : 10 au 14 juin 2023

        ***Pour commencer, sélectionnez l'une des options dans la barre latérale.***
        """)