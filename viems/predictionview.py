import streamlit as st

def get_feature_and_predict():
    st.header("Prediction")
    st.title("Interface de prédiction")

    # Informations de prédiction
    st.header("Veuillez saisir les informations pour la prediction")
    wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=100.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=1.0)
    temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)


    # Validation des informations
    if st.button("Prédire",):
        if wind_speed is None or humidity is None or temperature is None:
            st.error("Veuillez entrer toutes les informations.")
        else:
            # Effectuer la prédiction ici
            st.success("Prédiction effectuée avec succès !")

if __name__ == "__main__":
    get_feature_and_predict()