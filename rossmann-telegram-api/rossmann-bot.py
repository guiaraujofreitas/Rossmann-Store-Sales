#scrip to test
import json
import pandas as pd
import requests

from flask import Flask, request, Response

#constants

TOKEN = '5419949546:AAEjBl0T1EOLD69KMvMiu84SUsA_jharnGU'

#infomation about the BOT
#https://api.telegram.org/bot5419949546:AAEjBl0T1EOLD69KMvMiu84SUsA_jharnGU/getMe

# GET UPDATES ( To collect messagens )
#https://api.telegram.org/bot5419949546:AAEjBl0T1EOLD69KMvMiu84SUsA_jharnGU/getUpdates

#Webhook
#https://api.telegram.org/bot5419949546:AAEjBl0T1EOLD69KMvMiu84SUsA_jharnGU/setWebhook?url=https://a3aba08d90b4a8.lhrtunnel.link

#Webhook Heroku
#https://api.telegram.org/bot5419949546:AAEjBl0T1EOLD69KMvMiu84SUsA_jharnGU/setWebhook?url=https://rossmann-prediction-week-sales.herokuapp.com/rossmann/predict

# Send Messagens
#https://api.telegram.org/bot5419949546:AAEjBl0T1EOLD69KMvMiu84SUsA_jharnGU/sendMessage?chat_id=1299583213&text="Hi Gui, I'm fine. What abou you?"

def send_messagens(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id='.format(chat_id)
    
    #methdo send of data
    r = requests.post(url, json={'text': text} )
    print( 'Status code {}'.format( r.status_code ) )
    #print( 'Status Code {}'.format( r.status_code ) )
    return None
                  


def load_dataset(store_id):
    
    #loading the file of test
    df10 = pd.read_csv('/home/guilherme/Documentos/repos/datascienceemproducao/data/test.csv')
    df_store = pd.read_csv('/home/guilherme/Documentos/repos/datascienceemproducao/data/store.csv')

    #merge the dataset for to making predction 
    df_test = pd.merge(df10, df_store, how= 'left', on='Store')

    #choose the store for prediction to local test
    df_test = df_test.loc[df_test['Store']==22]
                      
    if not df_test.empty:
                      
        #remove the rows and columns empty and filtering the stores that are opens
        df_test = df_test.loc[(~df_test['Open'].isnull()) & (df_test['Open']!=0)]

        #remove the colum id
        df_test = df_test.drop('Id', axis=1)

        #convent DataFrame to json
        data = json.dumps(df_test.to_dict(orient='records') )
                      
    else: 
         data = 'error'
                      
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
  
def parse_message(message):
    #chat_id  = message['message']['chat']['id']
    chat_id  = message['message']['chat']['id']
    store_id = message['message']['text']
              
    store_id = store_id.replace('/', '')
                 
    try:
        store_id = int(store_id)

    except ValueError:
        send_message(chat_id,' Store ID is Wrong')
        store_id = 'error' 
    
    return chat_id, store_id
                      
#API Initialize
app = Flask( __name__ )
                      
@app.route('/', methods= ['GET','POST'] )
                      
def index():
    if request.method == 'POST': 
        message = request.get_json()
                      
        chat_id, store_id = parse_message( message )
        
        if store_id != 'error':
            #loading data
            data = load_dataset(store_id)
                      
            if data != 'error':
            
                #prediction
                d1 = predict(data)
                
                #calculation
                d2 = d1[['store','prediction']].groupby('store').sum().reset_index()
                msg = 'Store Number {} will sell R$ {:,.2f} in the next 6 weekend'.format(d2['store'].values[0],
                                                                                          d2['prediction'].values[0] )
                 
                send_message(chat_id, msg)
                return Response('ok', status=200)       
                    
                             
                                
            else:
                send_message(chat_id, 'Store Not Available')
                return Response ('Ok', status=200 )
        else:
            
            send_message(chat_id, 'Store ID is Wrong')
            return Response ('Ok', status=200 )
                      
    else:
        
        return '<h1> Rossmann Prediction Telegram Boot </h1>'
     
if __name__ == '__main__':
#if __name__ = '__main__':
    app.run(host = '0.0.0.0', port=5000)
                      
                      
                      
