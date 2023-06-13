
from sources.featuring import add_consumption_average
from sources.data_getter import load_dataset
from sources.featuring import create_datetime_features
import streamlit as st

def my_data_with_another_feautures():
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    data = add_consumption_average(df_data = data, rolling_hours=1)
    #Mettre DateTime comme une Column'
    data.reset_index(inplace=True)
    return data 

