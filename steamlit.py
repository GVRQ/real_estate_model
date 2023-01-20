# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.externals import joblib

# Load the model
model = joblib.load('real_estate_model.pkl')

# Create a function to predict the price of a property
def predict_price(location, sqft, bath, bhk):
    input_features = [location, sqft, bath, bhk]
    price = model.predict([input_features])
    return price

# Create a Streamlit app
def app():
    st.title('Real Estate Price Predictor')
    location = st.text_input('Enter the location of the property')
    sqft = st.number_input('Enter the square footage of the property')
    bath = st.number_input('Enter the number of bathrooms in the property')
    bhk = st.number_input('Enter the number of bedrooms in the property')
    submit = st.button('Submit')

    if submit:
        result = predict_price(location, sqft, bath, bhk)
        st.success('The predicted price of the property is: {}'.format(result))

if __name__ == '__main__':
    app()