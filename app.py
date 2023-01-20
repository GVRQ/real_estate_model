from flask import Flask, flash, jsonify, redirect, render_template, request, session,redirect, jsonify
from static.property_types import PROPERTY_TYPES
from static.locations import LOCATIONS
from static.df_cols import DF_COLS
import pandas as pd
import pickle

app = Flask(__name__)

def load_model():
    return pickle.load(open('finalized_model.p', 'rb'))


@app.route("/")
def index():
	return render_template("index.html",message="",locations=LOCATIONS,property_types=PROPERTY_TYPES)

@app.route("/predict", methods=["POST"])
def predict():
    response_dict = jsonify(request.form).json
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

    return render_template("index.html",
                            message=f"Predicted price is AED {y_pred:,.2f}",
                            locations=LOCATIONS,
                            property_types=PROPERTY_TYPES,
                            success=True
                            )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',error_code='404',message='Opps! Are you lost?',link_to_home=True)



if __name__ == '__main__':
	app.debug=True
	app.run(debug=True)