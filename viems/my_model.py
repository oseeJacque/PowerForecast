import xgboost as xgb
import os
from my_data import my_data_with_another_feautures
import streamlit as st

#Entraînement et sauvagarde du model
def train_and_save_model(X, y, n_estimators, model_name, model_dir="models"):
    current_path=current_path = os.getcwd()
    st.write(current_path)
    # Création du dossier pour enregistrer les modèles
    if not os.path.exists(model_dir):
        model_dir_path=os.path.join(current_path,model_dir)
        os.makedirs(model_dir_path)
        
    # Création du modèle XGBoost
    model = xgb.XGBRegressor(n_estimators=n_estimators)
    
    # Entraînement du modèle sur les données
    model.fit(X, y)
    
    #Enregistrement du modèle
    model_path = os.path.join(model_dir, f"{model_name}.dat")
    model.save_model(model_path)
    
    return model 

#Creation du model
def creation_du_model():
    #Charger la donnée
    data = my_data_with_another_feautures()
    
    #Enregistrement des target dans une variable 
    taget1 = data["Zone 1 Power Consumption"] #Model 1
    taget2 = data["Zone 2 Power Consumption"] #Model 2
    taget3 = data["Zone 3 Power Consumption"] #Model 3

    #prise des columns à l'exception 
    features = data
    features.drop(["Zone 1 Power Consumption","Zone 2 Power Consumption","Zone 3 Power Consumption","DateTime"],axis=1,inplace=True)
    features['WeekOfYear'] = features['WeekOfYear'].astype(int)
    st.write(features)
    
    list_targets= [taget1,taget2,taget3]
    i=0
    for taget in list_targets: 
        model = train_and_save_model(features, taget, n_estimators=1500, model_name= f"model{i}", model_dir="models") 
        i+=1
        st.write(f"model {i}")
        st.write(model) 




if __name__ == "__main__":
    creation_du_model()
    



