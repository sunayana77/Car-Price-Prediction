import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('Car Price Prediction')


present_price = st.number_input("Present price NPR")
kms_driven = st.number_input("Total km driven")
owner = st.selectbox("Number of Owners",(0,1,2,3))
no_year = st.number_input("Age")
fuel_type =  st.selectbox("Select Fuel type",("Diesel","Petrol","CNG"))
seller_type = st.selectbox("Select Seller type",("Dealer","Individual"))
transmission = st.selectbox("Select Transmission",("Manual","Automatic"))

converted_price = present_price/100000

fuel_type_petrol = False
fuel_type_diesel = False

if fuel_type == "Petrol":
    fuel_type_petrol = True
elif fuel_type == "Diesel":
    fuel_type_diesel = True

seller_type_individual = False

if seller_type == "Individual":
    seller_type_individual = True

transmission_Manual = False

if transmission == "Manual":
    transmission_Manual = True

@st.cache_resource
def load_model():
    model = pickle.load(open('random_forest_regression_model.sav','rb'))
    return model

loaded_model = load_model()

input_data = [converted_price,kms_driven,owner,no_year,fuel_type_diesel,fuel_type_petrol,seller_type_individual,transmission_Manual]


if st.button("Car Price"):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)

    st.write(f'The predicted price of the car is: {prediction[0]*100000:.2f} ')

