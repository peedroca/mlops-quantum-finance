import os
import logging
import string
import json
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = NpEncoder

def init():
    global loan_purpose_encoder
    global Security_Type_encoder
    global age_encoder
    global Region_encoder
    global scaler
    global model
    global stats_label
    
    loan_purpose_encoder = pickle.load(open('loan_purpose_encoder.pkl', 'rb'))
    Security_Type_encoder = pickle.load(open('Security_Type_encoder.pkl', 'rb'))
    age_encoder = pickle.load(open('age_encoder.pkl', 'rb'))
    Region_encoder = pickle.load(open('Region_encoder.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))

    stats_label = pd.read_csv('stats_label.csv')

    logging.info("Init complete")

def get_score_description(score):
    if score < 600:
        return "low score"
    elif score < 700:
        return "medium score"
    elif score >= 700:
        return "high score"

def get_persona(row):
    return f"A person with a {get_score_description(row['Credit_Score'])}, living in the {row['Region']}, is around {row['age']} years old."

@app.route("/predict", methods=['POST'])
def call_predict(request = request):
    data = pd.DataFrame(request.json, index=[0])

    data['loan_purpose_encoded'] = loan_purpose_encoder.transform(data['loan_purpose'])
    data['Security_Type_encoded'] = Security_Type_encoder.transform(data['Security_Type'])
    data['age_encoded'] = age_encoder.transform(data['age'])
    data['Region_encoded'] = Region_encoder.transform(data['Region'])
    
    data_scaled = scaler.transform(data[['loan_purpose_encoded',
        'Security_Type_encoded',
        'age_encoded',
        'Region_encoded',
        'year',
        'loan_amount',
        'term',
        'property_value',
        'income',
        'Credit_Score',
        'LTV',
        'dtir1']])

    prediction = model.predict(data_scaled)[0]
    stats_label_selected = stats_label.query("label == @prediction")

    persona = get_persona(data.iloc[0])

    ret = json.dumps({
        'prediction_label': prediction,  
        'defaulted_ratio': stats_label_selected.iloc[0]['defaulted_ratio'],  
        'mean_credit_score_defaulted': stats_label_selected.iloc[0]['mean_credit_score_defaulted'],
        'persona': persona
    }, cls=NpEncoder)

    return app.response_class(response=ret, mimetype='application/json')

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER IS RUNNING!"

if __name__ == '__main__':
    init()
    app.run(port=8080, host = '0.0.0.0')