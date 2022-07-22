import pickle
import pandas as pd
import requests
import json
from flask import Flask, request, Response

#loading the model
model = pickle.load(open ('/home/guilherme/Documentos/repos/datascienceemproducao/model/model_rossmann.pkl','rb') )

#collecting the past, archive and import Class
from rossmann.Rossmann import Rossmann

#start API
app = Flask( __name__ )

#creating url (endpoint) to send data
@app.route('/rossmann/predict', methods=['POST'] )
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: #there is data
        
        if isinstance( test_json, dict):#Unique example
            
            #In case there is data only raw
            test_raw = pd.DataFrame(test_json, index=[0])
            
        else:
            #collect all the json of all the raws
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys() ) #Multiple examples
        
        
        #Instance Rossmann Class (Making a copy)
        pipeline = Rossmann()
        
        #data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        #featuree engineering
        df2 = pepeline.feature_engineering(df1)
        
        #data preparation
        df3 = pipeline.data_preparation(df2)
        
        #predict                              #test
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
    
    else:
        return Response( '{}',status=200 , mimetype='application/json')

if __name__ == '__main__':
    print('chegou aqui')
    # o resto
#if  __name__ == '_main_':
    app.run(host='0.0.0.0')
    #app.run( '0.0.0.0' )
    

