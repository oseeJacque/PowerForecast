import datetime
from sources.featuring import add_consumption_average
from prediction import test_prediction
from sources.model import split
from viems.my_data import my_data_with_another_feautures
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Formatage de la date
def process_date(date):
    if date.year > 2017:
        new_date = date.replace(year=2017)
    else:
        new_date = date
    return new_date

#Combinaison de la date et l'heure
def combine_date_and_time(date, time):
    datetime_str = f"{date} {time}"
    return datetime_str 

#formate prediction 
def prediction_model(predict):
    if len(predict)==0:
        return 0
    else:
        return predict[0]


def get_feature_and_predict():

    #Creation des données de test 
    data= my_data_with_another_feautures()
    database_train, database_test=split(data, alpha=.8)
    #Get DateTime columns for prediction dataframe 
    prediction=pd.DataFrame(database_test["DateTime"])

    database_test.set_index("DateTime",inplace=True)
    database_train.set_index("DateTime",inplace=True)
    
    #Detection des tagets
    tag1=database_test["Zone 1 Power Consumption"]
    tag2=database_test["Zone 2 Power Consumption"]
    tag3=database_test["Zone 3 Power Consumption"]
    
    
    database_test=add_consumption_average(database_test, rolling_hours=1)
    database_train=add_consumption_average(database_train, rolling_hours=1)

    #Reformatage de la colonne DayofWeek
    database_test['WeekOfYear'] = database_test['WeekOfYear'].astype(int)
    database_train['WeekOfYear'] = database_train['WeekOfYear'].astype(int)

    database_test.drop(["Zone 1 Power Consumption","Zone 2 Power Consumption","Zone 3 Power Consumption"],axis=1,inplace=True)
    database_train.drop(["Zone 1 Power Consumption","Zone 2 Power Consumption","Zone 3 Power Consumption"],axis=1,inplace=True)
    
    
    

    # Centrer le titre
    predict_value=[]
    choix_zone= "ZONE 1"
    choix =st.selectbox("ZONE DE CONSOMMATION", ["ABOMEY-CALAVI", "COTONOU","PORTO-NOVO"]) #Action de l'utilisateur
    #Encodage des zones 
    if choix == "ABOMEY-CALAVI": 
        choix_zone="ZONE 1" 
    elif choix == "COTONOU":
        choix_zone="ZONE 2" 
    else:
        choix_zone="ZONE 3"
        

    # Demander à l'utilisateur de saisir une date entre la date minimale et la date maximale
    min_date = datetime.date(2023, 1, 1)
    selected_date = st.date_input("Sélectionnez une date", min_value=min_date,)
    selected_date=process_date(selected_date)
    #Demande de l'heure 
    default_time = datetime.time(0, 0)
    selected_time = st.time_input("Sélectionnez une heure", step=600 ,value=default_time )
    
    # Bouton de prédiction
    if st.button("Prévision"):
        columns=get_feature(database_test=database_test,database_train=database_train,selected_date=selected_date,selected_time=selected_time)
        predict_value=test_prediction(columns,taget_name=choix_zone)
        # Création des deux colonnes
        col1, col2 = st.columns([1, 1])

        # Texte à afficher dans la première colonne
        with col1:
            col1.markdown(
                "<div style='border: 1px solid gray; padding: 10px;border-radius: 10px; padding: 10px;'>"
                "<h3 style='text-align: center;'>Prévision</h3>"
                f"<h4>ZONE: {choix}</h4>"
                f"<h4>DATE: {selected_date}</h4>"
                f"<h4>HEURE: {selected_time}</h4>"
                f"<h4 style='font-size: 30px;'>CONSOMMATION : {prediction_model(predict_value)} KW</h4>"
                "</div>",
                unsafe_allow_html=True
            )
            

        # Contenu de la deuxième colonne
        with col2:
            # Ajoutez ici le contenu que vous souhaitez afficher dans la deuxième colonne
            st.write("Contenu de la deuxième colonne")



def get_feature(database_test,database_train,selected_date,selected_time,zone=1):   
    database_test.reset_index(inplace=True)
    database_train.reset_index(inplace=True)
    data_for_col= database_test.loc[(database_test.DateTime == combine_date_and_time(selected_date,selected_time))]
    if data_for_col.shape[0]==0 :
        data_for_col= database_train.loc[(database_train.DateTime == combine_date_and_time(selected_date,selected_time))]
    if zone == 1: 
        pass
        data_for_col.drop(["DateTime","Z2_Mean_Consumption_1H","Z3_Mean_Consumption_1H"],axis=1,inplace=True)
    return data_for_col
    
    
def plot_prediction(df_test, data, tag_name):
    data["predictions"] = test_prediction(feeatures=df_test,taget_name= tag_name)
    fig, ax = plt.subplots()
    ax.plot(data["DateTime"], data["predictions"])
    ax.set_xlabel('Date de consommation')
    ax.set_ylabel('Quantité  de consommation')
    ax.set_title('Graphique')
    # Affichage du graphique dans Streamlit
    st.pyplot(fig)
    

    

if __name__ == "__main__":
    get_feature_and_predict()