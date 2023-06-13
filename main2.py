import streamlit as st

def main():
    
# Logo
    logo_menu = "assets/logo_menu.png"
    st.sidebar.image(logo_menu, use_column_width=False, width=300)

    page_bg_img = """
    <style> [data-testid="stSidebar"] {
        background: linear-gradient(90deg, #5675a3, rgba(161,195,221,1))
    </style> 
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Menu de navigation latéral
#    st.sidebar.header("Menu")
    selected_page = st.sidebar.selectbox("Sélectionnez une page", ["Accueil", "Prédictions", "Analyse", "Documentation"])

# Changer la couleur du menu latéral
#    st.set_theme({'sidebar.backgroundColor': '#F8F8F8', 'sidebar.textColor': '#333333'})

    # Votre code pour chaque page sélectionnée
    if selected_page == "Accueil":
        afficher_accueil()
    elif selected_page == "Prédictions":
        afficher_predictions()
    elif selected_page == "Analyse":
        afficher_analyse()
    elif selected_page == "Documentation":
        afficher_documentation()


def afficher_accueil():

    # Titre de la page d'accueil
    st.markdown("<h1 style='text-align: center;'>Powerforecast - Prédiction de la consommation d'énergie</h1>", unsafe_allow_html=True)

    # Chargement et affichage de l'image
    image = 'assets/powerforecast.png'
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



def afficher_predictions():
    # Code pour la page des prédictions
    st.sidebar.header("Prédictions")
    pass

def afficher_analyse():
    # Code pour la page d'analyse
    st.sidebar.header("Analyse")
    pass

def afficher_documentation():

    # Code de la page de détails
    st.title("Documentation")
    st.write("""Les données utilisées dans ce projet sont collectées à partir de [source des données]. 
             Elles comprennent des informations sur la consommation d'énergie passée, les facteurs météorologiques, les jours fériés, etc.
             """)
    
    st.write(" ***Affichage des 50 premières observations de la base de données***")
    # dataframe ici#

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

if __name__ == '__main__':
    main()
