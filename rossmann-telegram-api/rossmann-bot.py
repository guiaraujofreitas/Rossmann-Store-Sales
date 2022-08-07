#scrip to test
import json
import pandas as pd
import requests

def load_dataset(store_id):
    
    #loading the file of test
    df10 = pd.read_csv('/home/guilherme/Documentos/repos/datascienceemproducao/data/test.csv')
    df_store = pd.read_csv('/home/guilherme/Documentos/repos/datascienceemproducao/data/store.csv')

    #merge the dataset for to making predction 
    df_test = pd.merge(df10, df_store, how= 'left', on='Store')

    #choose the store for prediction to local test
    df_test = df_test.loc[df_test['Store']==22]

    #remove the rows and columns empty and filtering the stores that are opens
    df_test = df_test.loc[(~df_test['Open'].isnull()) & (df_test['Open']!=0)]

    #remove the colum id
    df_test = df_test.drop('Id', axis=1)

    #convent DataFrame to json
    data = json.dumps(df_test.to_dict(orient='records') )
    
    return data

def prediction(data):
    
    #API Call
    #address call
    url = 'https://rossmann-prediction-week-sales.herokuapp.com/rossmann/predict'

    #type of requisition
    header = {'Content-type':'application/json'}

    #data the to be collected
    data = data

    #send the datas
    r = requests.post(url, data=data, headers=header)

    print('Status code {}'.format(r.status_code) )

    d1 = pd.DataFrame( r.json(),columns = r.json()[0].keys() )
    
    return d1

#d2 = d1[['store','prediction']].groupby('store').sum().reset_index()

#for i in range( len(d2 ) ):
    #print('Store Number {} will sell R$ {:,.2f} in the next 6 weekend'.format(
        #d2.loc[i,'store'],
        #d2.loc[i,'prediction'] ) )