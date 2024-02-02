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
    global model
    
    model = pickle.load(open('default_propensity_model.pkl', 'rb'))
    logging.info("Init complete")

@app.route("/predict", methods=['POST'])
def call_predict(request = request):
    data = pd.DataFrame(request.json, index=[0])
    prediction = model.predict(data)

    ret = json.dumps({'prediction': prediction[0]}, cls=NpEncoder)

    return app.response_class(response=ret, mimetype='application/json')

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER IS RUNNING!"

if __name__ == '__main__':
    init()
    app.run(port=8080, host = '0.0.0.0')