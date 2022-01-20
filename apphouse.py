
from flask import Flask, render_template, request
import requests
import pickle
import os
import pandas as pd
import numpy as np
import sklearn


app = Flask(__name__)
model = pickle.load(open('olxprediction.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('house.html')

@app.route("/predict", methods=['POST'])
def predict():
    print('no')
        
    if request.method == 'POST':
       

        TYPE  = str(request.form['TYPE_'])
        print('gttt')
        BEDROOMS  = int(request.form['BEDROOMS'])
        print('hh')
        BATHROOMS  = int(request.form['BATHROOMS'])
        FURNISHING  = str(request.form['FURNISHING'])
        CONSTRUCTIONSTATUS  = str(request.form['CONSTRUCTION STATUS'])
        POSTEDBY  = str(request.form['LISTED BY'])
        print('w')
        TotalArea  = int(request.form['SUPER BUILTUP AREA (FT²)'])
        
        CARPETAREA = int(request.form['CARPET AREA (FT²)'])
        print('q')
        CARPARKING = int(request.form['CAR PARKING'])
        
        FACING= str(request.form['FACING'])
        FLOORNO = int(request.form['FLOOR NO'])
        LOCATLITY = str(request.form['LOCATLITY'])
        STATE = str(request.form['STATE'])
        
        print(TYPE, BEDROOMS, BATHROOMS, FURNISHING, CONSTRUCTIONSTATUS, POSTEDBY,
       TotalArea, CARPETAREA, CARPARKING, FACING, FLOORNO,
       LOCATLITY,STATE)
        print('s')
        prediction=model.predict(np.array([[TYPE, BEDROOMS, BATHROOMS, FURNISHING, CONSTRUCTIONSTATUS, POSTEDBY,
       TotalArea, CARPETAREA, CARPARKING, FACING, FLOORNO,
       LOCATLITY,STATE ]]))
        output=np.exp(prediction)
        output=round(output[0],1)
        if output<0:
            return render_template('house.html',prediction="Sorry you cannot sell this House")
        else:
            return render_template('house.html',prediction="You can sell the House at ₹ {} ".format(output))
    else:
        return render_template('house.html')

if __name__ == "__main__":
   port = int(os.environ.get('PORT' , 5000))
   app.run(host='0.0.0.0', port=port)

