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
    
    
    
    ########################### Interface #######################

    # Centrer le titre
    predict_value=0
    choix =st.selectbox("ZONE DE PREDICTION", ["ZONE 1", "ZONE 2","ZONE 3"]) #Action de l'utilisateur
 
    min_date = datetime.date(2023, 1, 1)

    # Demander à l'utilisateur de saisir une date entre la date minimale et la date maximale
    selected_date = st.date_input("Sélectionnez une date", min_value=min_date,)
    selected_date=process_date(selected_date)
    #Demande de l'heure 
    default_time = datetime.time(0, 0)
    selected_time = st.time_input("Sélectionnez une heure", step=600 ,value=default_time )
    st.write(f"L'heure sélectionnée est : {selected_time}") 
    
    # Bouton de prédiction
    if st.button("Prédire"):
        columns=get_feature(database_test=database_test,database_train=database_train,selected_date=selected_date,selected_time=selected_time)
        predict_value=test_prediction(columns,taget_name=choix)
        st.write(predict_value)

        
    
    # Affichage du texte centré
    st.markdown("<h2 style='text-align: center';> CONSOMMATION PREDITE:</h2>", unsafe_allow_html=True)
    
    """
    if choix == "ZONE 1":
        plot_prediction(df_test=database_test,data=prediction,tag_name="tag1")
        
        pass 
    elif choix == "ZONE 2":
        plot_prediction(df_test=database_test,data=prediction,tag_name="tag2")
        pass
     
    else :
        plot_prediction(df_test=database_test,data=prediction,tag_name="tag3")
        pass
"""

def get_feature(database_test,database_train,selected_date,selected_time,zone=1):   
    database_test.reset_index(inplace=True)
    database_train.reset_index(inplace=True)
    data_for_col= database_test.loc[(database_test.DateTime == combine_date_and_time(selected_date,selected_time))]
    if data_for_col.shape[0]==0 :
        data_for_col= database_train.loc[(database_train.DateTime == combine_date_and_time(selected_date,selected_time))]
    #data_for_col
    if zone == 1: 
        pass
        data_for_col.drop(["DateTime","Z2_Mean_Consumption_1H","Z3_Mean_Consumption_1H"],axis=1,inplace=True)
    return data_for_col
    st.write(data_for_col)
 
    
    

def plot_prediction(df_test, data, tag_name):
    data["predictions"]=test_prediction(feeatures=df_test,taget_name= tag_name)
    fig, ax = plt.subplots()
    ax.plot(data["DateTime"], data["predictions"])
    ax.set_xlabel('Date de consommation')
    ax.set_ylabel('Quantité  de consommation')
    ax.set_title('Graphique')
    # Affichage du graphique dans Streamlit
    st.pyplot(fig)
    

    

if __name__ == "__main__":
    get_feature_and_predict()