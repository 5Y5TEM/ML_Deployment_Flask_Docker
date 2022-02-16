# Created by MeltemSubasioglu at 2/16/2022

import pickle
from flask import Flask, request
from flasgger import Swagger
import numpy as np
import pandas as pd
import os
dirname = os.path.dirname(__file__)

# Load model in read binary mode
with open(dirname+ r"/rf.pkl", 'rb') as model_file:
    model = pickle.load(model_file)



# Start the flask app
app = Flask(__name__)

# Flasgger library for Flask UI support via Swagger
# NOTE: Flasgger uses docstrings as specification, so make sure to use the exact format 
swagger = Swagger(app)


# GET Request with URI Params
@app.route("/predict")
def get_prediction():
    """
    Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    # Parse the features as list of lists
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))

    return str(prediction)


# POST Request with File Input
@app.route("/predict_file", methods=["POST"])
def get_prediction_file():
    """
    Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    # Reading filed in Flask with request.files
    input_data = pd.read_csv(request.files.get("input_file"), header=None)

    # Parse the features as list of lists
    prediction = model.predict(np.array(input_data))
    return str(list(prediction))



if __name__ == "__main__":
    app.run()