import streamlit as st

def objectifs():
   # Ajouter du code CSS personnalisé
   st.markdown(
      """
      <style>
      body {
         background-image: linear-gradient(to right top, #c9f1fd, #d2f2fe, #dbf3ff, #e5f4ff, #eef6ff);
         background-repeat: no-repeat;
         background-size: cover;
         background-attachment: fixed;
      }
      h1 {
         font-size: 100px;
         color: #80a5b7;
         transform: rotate(-45deg);
         position: fixed;
         top: 40%;
         left: 25%;
      }
      </style>
      """,
      unsafe_allow_html=True
   )
   st.markdown("## OBJECTIFS")
   st.markdown("1. **Prédire la consommation électrique future :** L'objectif principal est de développer un modèle capable de prédire la consommation électrique à Tétouan en utilisant des variables météorologiques et d'autres facteurs pertinents. Cela permettra d'estimer la demande énergétique future et d'aider à la planification de l'approvisionnement en électricité.")
   st.markdown("2. **Comprendre l'influence des variables météorologiques :** En analysant les relations entre les variables météorologiques telles que la température, l'humidité, la vitesse du vent, etc., et la consommation électrique, le projet vise également à mieux comprendre comment ces facteurs influencent la demande d'électricité.")

   st.markdown("## UTILITES")
   st.markdown("1. **Gestion de la demande énergétique**")
   st.markdown("2. **Planification et optimisation du réseau électrique**")
   st.markdown("3. **Tarification et facturation**")
   st.markdown("4. **Sensibilisation à la consommation énergétique**")

   st.markdown("## USAGES")
   st.markdown("1. **Prévisions de demande pour les opérations de maintenance**")
   st.markdown("2. **Analyse de la charge de travail pour les entreprises**")
   st.markdown("3. **Évaluation de l'impact des politiques d'économie d'énergie**")
   st.markdown("4. **Aide à la prise de décision pour les investissements énergétiques**")
   st.markdown("5. **Optimisation des ressources**")
   st.markdown("6. **Anticipation des pannes et des problèmes techniques**")
   st.markdown("7. **Gestion des pics de demande**")
   st.markdown("8. **Prévisions financières**")
   st.markdown("9. **Gestion de la qualité de service**")
