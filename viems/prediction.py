import xgboost as xgb
import os
from my_data import my_data_with_another_feautures
import streamlit as st


def make_prediction(features, target_column):
    if target_column == "ZONE 1":
        target_column = "model0"
    elif target_column == "ZONE 2":
        target_column = "model1"
    else:
        target_column = "model2"
    # Charger le modèle enregistré correspondant à la colonne cible
    current_path=current_path = os.getcwd()
    model_path = os.path.join(current_path,f"models/{target_column}.dat")  # Chemin du modèle enregistré
    model = xgb.Booster()
    model.load_model(model_path)
    
    # Faire la prédiction avec les features fournies
    dmatrix = xgb.DMatrix(features)
    predictions = model.predict(dmatrix)
    
    return predictions


def test_prediction(feeatures,taget_name):
    #Charger la donnée
    data = my_data_with_another_feautures()
    feature=data 
    feature.drop(["Zone 1 Power Consumption","Zone 2 Power Consumption","Zone 3 Power Consumption","DateTime"],axis=1,inplace=True)
    feature['WeekOfYear'] = feature['WeekOfYear'].astype(int) 
    predict=make_prediction(features=feeatures, target_column = taget_name)
    st.write(f"la prediction est {predict}")
    return predict
    
if __name__ == "__main__":
    test_prediction()
    
    