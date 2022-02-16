# Created by MeltemSubasioglu at 2/16/2022

from flask import Flask, request

#initialize the flask app
app = Flask(__name__)

@app.get("/")
def home():
    """
    Set a function for GET request on landing page
    This function will simply paste the str in browser
    """
    return("Hello World")



@app.route("/predict", methods=['POST'])
# @app.post("/predict")
def add():
    """
    NOTE: web browsers always also access via "GET" request.
    When disabling GET, use Postmaster instead
    """
    ## user input as strings, parsed in URL
    #a = request.args.get("a")
    #b = request.args.get("b")

    a = request.form["a"]
    b = request.form["b"]

    # We can't return an int
    return str(int(a) + int(b))


if __name__=='__main__':
    """
    Once the server is running, switch to location 
    Parameters are handed by adding e.g. ?a=10&b=20
    --> 127.0.0.1:5000/?a=10&b=20
    """
    app.run(port=7000)


