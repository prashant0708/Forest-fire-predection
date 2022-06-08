import pickle
from flask import Flask , request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import os 

app= Flask (__name__)
model=pickle.load(open('model1.pkl','rb'))

@app.route ('/')
def home():
    return render_template('home.html')

@app.route ('/predict_forest_fire',methods=['POST'])

def predict_api():
    """For postman testing this code is written  """ 
    try:
        data=request.json['data']
        print (data)
        new_data=[list(data.values())]
        output=model.predict(new_data)[0]
        return jsonify(output)
    except Exception as e:
        return str(e)
    
@app.route('/predict',methods=['POST'])
def predict():
    """For HTML   this code is written  """ 
    try:

          data=[float(x) for x in request.form.values()]
          final_features = [np.array(data)]
          print(data)
    
          output=model.predict(final_features)[0]
          print(output)
          #output = round(prediction[0], 2)
          return render_template('home.html', prediction_text="Predection Fire in  Bejaia Forest    {}".format(output))
    except Exception as e:
        return str(e)

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=os.environ['PORT'])
