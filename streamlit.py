import streamlit as st
from static.property_types import PROPERTY_TYPES
from static.locations import LOCATIONS
from static.df_cols import DF_COLS
import pandas as pd
import pickle

# currency conversion
aed_to_usd = 1 / 3.67 # exchange rate
aed_to_eur = 1 / 4.45
aed_to_rub = 1 / 0.058
aed_to_gbp = 1 / 5.1
aed_to_sek = 1 / 0.39

def load_model():
    return pickle.load(open('final_model.p', 'rb'))

def predict(response_dict):
    # initialize all columns with 0
    d = {k:[0] for k in DF_COLS}

    # update corresponding columns using submitted form values
    d[f'location_{response_dict["location"]}'] = [1]
    d[f'property_type_{response_dict["property_type"]}'] = [1]
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
    st.title("Dubai Real Estate Price Predictor")

    location = st.selectbox("Select the location of the property", sorted(LOCATIONS))
    property_type = st.selectbox("Property type", PROPERTY_TYPES)
    beds = st.slider("Number of Bedrooms (0 is a Studio)", 0,6,2)
    baths = st.slider("Number of Bathrooms", 1,7,3)
    size_sqft = st.slider("Area, sqft", 250,5000,1000)
    pool = st.checkbox("Pool")
    balcony = st.checkbox("Balcony")
    maid = st.checkbox("Maid's room")
    gym = st.checkbox("Gym")
    brand_new = st.checkbox("Brand new property")
    burj_view = st.checkbox("Burj Khalifa view")
    furnished = st.checkbox("Furnished property")
    sea_view = st.checkbox("Sea view")
    beach_access = st.checkbox("Beach nearby")
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
    price = int(round(price, -3)) # rounding up to 1,000 AED
    st.success(f"The predicted price of the property is {price} AED")
    st.info(f"Currency Conversion:")
    st.info(f"USD: {price * aed_to_usd}")
    st.info(f"EUR: {price * aed_to_eur}")
    st.info(f"RUB: {price * aed_to_rub}")
    st.info(f"GBP: {price * aed_to_gbp}")
    st.info(f"SEK: {price * aed_to_sek}")

    #st.success(f"The predicted price of the property is {price:,.2f} AED.")
    #st.success(f"The predicted price of the property is {price:,} AED.")

if __name__ == "__main__":
    main()