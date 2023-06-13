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
        st.subheader("Graphique 1")
        afficher_graphique1()

    with col2:
        st.subheader("Graphique 2")
        afficher_graphique2()

    with col3:
        st.subheader("Graphique 3")
        afficher_graphique3()

    # Ligne 2 - Une colonne
    st.subheader("Graphique 4")
    afficher_graphique4()

    # Lignes suivantes - Au moins une colonne
    st.subheader("Graphiques supplémentaires")
    afficher_graphiques_supplementaires()


def afficher_graphique1():
    # Graphique 1
    fig, ax = plt.subplots()
    ax.hist(df["Colonne1"])
    ax.set_title("Histogramme de Colonne1")
    st.pyplot(fig)


def afficher_graphique2():
    # Graphique 2
    fig, ax = plt.subplots()
    ax.scatter(df["Colonne2"], df["Colonne1"])
    ax.set_title("Nuage de points de Colonne2 vs Colonne1")
    st.pyplot(fig)


def afficher_graphique3():
    # Graphique 3
    fig, ax = plt.subplots()
    sns.boxplot(data=df[["Colonne1", "Colonne2"]])
    ax.set_title("Boxplot de Colonne1 et Colonne2")
    st.pyplot(fig)


def afficher_graphique4():
    # Graphique 4
    fig, ax = plt.subplots()
    df["Colonne1"].value_counts().plot(kind="bar")
    ax.set_title("Comptage des catégories de Colonne1")
    st.pyplot(fig)


def afficher_graphiques_supplementaires():
    # Graphiques supplémentaires
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Graphique 5
    axes[0, 0].plot(df["Colonne1"])
    axes[0, 0].set_title("Ligne de Colonne1")

    # Graphique 6
    axes[0, 1].boxplot(df["Colonne2"])
    axes[0, 1].set_title("Boxplot de Colonne2")

    # Graphique 7
    axes[1, 0].scatter(df["Colonne1"], df["Colonne2"])
    axes[1, 0].set_title("Nuage de points de Colonne1 vs Colonne2")

    # Graphique 8
    axes[1, 1].hist2d(df["Colonne2"], df["Colonne1"])
    axes[1, 1].set_title("Histogramme 2D de Colonne2 vs Colonne1")

    st.pyplot(fig)



