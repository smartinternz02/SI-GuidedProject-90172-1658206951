from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
import os

model = pickle.load(open('flight.pkl', 'rb'))
app = Flask(_name_)  # initializing the app


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction, methods =["POST"]/')
def predict():
    name = request.form['name']
    month = request.form['month']
    dayofmonth = request.form['dayofmonth']
    dayofweek = request.form['dayofweek']
    origin = request.form['origin']
    if (origin == "msp"):
        origini, origin2, origin3, origin4, orgin5 = 0, 0, 0, 0, 1
    if (origin == "dtw"):
        origini, origin2, origin3, origin4, orgin5 = 1, 0, 0, 0, 0
    if (origin == "jfk"):
        originl, origin2, origin3, origin4, orgin5 = 0, 0, 1, 0, 0
    if (origin == "sea"):
        originl, origin2, origin3, origins, orgin5 = 0, 1, 0, 0, 0
    if (origin == "alt"):
        origini, origin2, origin3, origins, orgin5 = 0, 0, 0, 1, 0


destination = request.form['destination']
if (destination == "msp"):
    destinationl, destination2, destination, destination4, destination5 = 0, 0, 0, 0, 1
if (destination == "dev"):
    destinationl, destination2, destination3, destination4, destination5 = 1, 0, 0, 0, 0
if (destination == "3"):
    destinationl, destination2, destination3, destination4, destination5 = 0, 0, 1, 0, 0
if (destination == "pca"):
    destinationl, destination2, destination3, destination4, destination5 = 0, 1, 0, 0, 0
if (destination == "alt"):
    destinationl, destination2, destination3, destination4, destination5 = 0, 0, 0, 1, 0

dept = request.form['dept']

arrtine = request.form['arruime']
actdept = request.form['actdept']

dept15 = int(dept) - int(actdept)

total = [[name, month, dayofmonth, dayofweek, originl, origin2, origin3, origin4, orgin5, destinationl, destination2,
          destination3, destination4, destination5, i]]

y_pred = model.predict(total)

print(y_pred)

if (y_pred[0.]):
    ans = "The Flight will be on sime"
else:
    ans = "The Flight will be delayed"

return render_template("index.html",showcase=ans)

if __name__==__main__'':
    app.run(debug=False)