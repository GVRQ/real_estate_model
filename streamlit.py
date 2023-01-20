import streamlit as st
from static.property_types import PROPERTY_TYPES
from static.locations import LOCATIONS
from static.df_cols import DF_COLS
import pandas as pd
import pickle

def load_model():
    return pickle.load(open('finalized_model.p', 'rb'))

def predict(response_dict):
    # initialize all columns with 0
    d = {k:[0] for k in DF_COLS}

    # update corresponding columns using submitted form values
    d[f'location_{response_dict["location"]}'] = [1]
    d[f'property_type{response_dict["property_type"]}'] = [1]
    d['beds'] = [int(response_dict['beds'])]
    d['baths'] = [int(response_dict['baths'])]
    d['size_sqft'] = [int(response_dict['size_sqft'])] 
    d['pool'] = [int(response_dict['pool'])]   
    d['balcony'] = [int(response_dict['balcony'])]
    d['maid'] = [int(response_dict['maid'])]
    d['gym'] = [int(response_dict['gym'])]
    d['brand_new'] = [int(response_dict['brand_new'])]
    d['burj_view'] = [int(response_dict['burj_view'])]
    d['furnished'] = [int(response_dict['furnished'])]
    d['sea_view'] = [int(response_dict['sea_view'])]
    d['beach'] = [int(response_dict['beach'])]

    X_pred = pd.DataFrame(d)
    loaded_model = load_model()
    y_pred = loaded_model.predict(X_pred).item()

    return y_pred

def main():
    st.title("Real Estate Price Predictor")

    location = st.selectbox("Select the location of the property", LOCATIONS)
    property_type = st.selectbox("Select the property type", PROPERTY_TYPES)
    beds = st.number_input("Enter the number of bedrooms in the property", value=0, step=1)
    baths = st.number_input("Enter the number of bathrooms in the property", value=0, step=1)
    size_sqft = st.number_input("Enter the square footage of the property", value=0, step=1)
    pool = st.checkbox("Does the property have a pool?")
    balcony = st.checkbox("Does the property have a balcony?")
    maid = st.checkbox("Does the property have a maid's room?")
    gym = st.checkbox("Does the property have a gym?")
    brand_new = st.checkbox("Is the property brand new?")
    burj_view = st.checkbox("Does the property have a view of the Burj Khalifa?")
    furnished = st.checkbox("Is the property furnished?")
    sea_view = st.checkbox("Does the property have a sea view?")
    beach_access = st.checkbox("Is the property beach accessible?")
    submit = st.button("Submit")

    response_dict = {
    "location": location,
    "property_type": property_type,
    "beds": beds,
    "baths": baths,
    "size_sqft": size_sqft,
    "pool": pool,
    "balcony": balcony,
    "maid": maid,
    "gym": gym,
    "brand_new": brand_new,
    "burj_view": burj_view,
    "furnished": furnished,
    "sea_view": sea_view,
    "beach": beach_access
}

    if submit:
        response_dict = {
        "location": location,
        "property_type": property_type,
        "beds": beds,
        "baths": baths,
        "size_sqft": size_sqft,
        "pool": pool,
        "balcony": balcony,
        "maid": maid,
        "gym": gym,
        "brand_new": brand_new,
        "burj_view": burj_view,
        "furnished": furnished,
        "sea_view": sea_view,
        "beach": beach_access
    }
    price = predict(response_dict)
    st.success(f"The predicted price of the property is AED {price:,.2f}")

if __name__ == "__main__":
    main()