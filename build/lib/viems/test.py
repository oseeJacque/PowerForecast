from sources.data_analysis import display_consumption_period
from sources.featuring import create_datetime_features
from sources.data_getter import load_dataset
import streamlit as st



def main():
    #Charger la donnée
    data = load_dataset("../Datasets/Tetuan_City_power_consumption.csv")
    #ajouter denouvelle variable a la data (hour,dayofWeek,Month,Year,DayofYear,WeekOfYear)
    data=create_datetime_features(data)
    
    #Afficharge par de la consommation par jour
    data.reset_index(inplace=True)
    st.write(data)
    display_consumption_period(data, figsize=(20, 15), start_date="2017-01-01" , end_date="2017-12-30")

if __name__ == "__main__":
    main()
    





