#cleaning, transformation and enconding

import pickle
import inflection
import pandas as pd
import numpy as np
import datetime
from datetime import date
import math
from sklearn.preprocessing   import LabelEncoder

class Rossmann (object):
    def __init__( self ):
        self.home_path = '/home/guilherme/Documentos/repos/datascienceemproducao/'
        self.competition_distance_scaler  = pickle.load( open(self.home_path + 'parameter/competition_distance_scaler.pkl_scaler', 'rb') )
        self.compettion_time_month_scaler = pickle.load( open(self.home_path + 'parameter/compettion_time_month.pkl_scaler', 'rb') )
        self.promo_time_week_scaler       = pickle.load( open(self.home_path + 'parameter/promo_time_week.pkl_scaler', 'rb') )
        self.year_scaler                  = pickle.load( open(self.home_path + 'parameter/year.pkl_scaler', 'rb') )
        self.store_type_encoded_scaler    = pickle.load( open(self.home_path + 'parameter/store_type_encoded_scaler.pkl', 'rb' ) )
        
    def data_cleaning(self, df1):
        

        ## 1.1  Rename Columns and Remove the Feature Sales and Customers

        df1['Promo2SinceWeek']           = df1['Promo2SinceWeek'].fillna(0).astype(int)
        df1['Promo2SinceYear']           = df1['Promo2SinceYear'].fillna(0).astype(int)
        df1['CompetitionDistance']       = df1['CompetitionDistance'].fillna(0).astype(int)
        df1['CompetitionOpenSinceMonth'] = df1['CompetitionOpenSinceMonth'].fillna(0).astype(int)
        df1['CompetitionOpenSinceYear']  = df1['CompetitionOpenSinceYear'].fillna(0).astype(int)
        
        cols_old = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo',
                   'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment',
                   'CompetitionDistance', 'CompetitionOpenSinceMonth',
                   'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek',
                   'Promo2SinceYear', 'PromoInterval']

        #function to convent columns format snackcase
        snackcase= lambda x: inflection.underscore( x )


        cols_new= list( map( snackcase, cols_old ))

        #rename columns 

        df1.columns = cols_new


        ## 1.3 Data Types

        # convent the colum data to datetime64
        df1['date'] = df1['date'].astype('datetime64[ns]')

        ## 1.5 FillOut NA

        #competition_distance
        df1['competition_distance'] = df1['competition_distance'].apply(lambda x: 200000 if math.isnan(x) else x )



        df1['competition_open_since_month']= df1.apply(lambda x: x['date'].month if 
                                                       math.isnan(x['competition_open_since_month']) 
                                                       else x['competition_open_since_month'], axis=1)



        df1['competition_open_since_year']= df1.apply(lambda x: x['date'].year if
                                                      math.isnan(x['competition_open_since_year']) 
                                                      else x['competition_open_since_year'],axis=1)


        df1['promo2_since_week'] = df1.apply(lambda x: x['date'].week if math.isnan(x['promo2_since_week'])
                                             else x['promo2_since_week'],axis=1)

        df1['promo2_since_year']= df1.apply(lambda x: x['date'].year if math.isnan(x['promo2_since_year'])
                                             else x['promo2_since_year'],axis=1)

        #dict of year to month
        month_map = {1: 'Jan',2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
                     6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov' ,12: 'Dec' }


        #substituindo NA por 0
        df1['promo_interval'].fillna(0,inplace=True)

        #extract month data 
        df1['month_map'] = df1['date'].dt.month.map(month_map)

        df1['is_promo'] = df1[['promo_interval','month_map']].apply(lambda x:0 if x['promo_interval']==0 
                                                                    else 1 if x['month_map'] in x['promo_interval'].split( ',' ) 
                                                                    else 0,axis=1)

        ## 1.6 Change Types
        
        #promo2
        df1['promo2_since_week']  = df1['promo2_since_week'] .astype(int)

        df1['promo2_since_year']  = df1['promo2_since_year'] .astype(int)
        
        #competition
        df1['competition_open_since_month'] = df1['competition_open_since_month'].astype(int)

        df1['competition_open_since_year'] =  df1['competition_open_since_year'].astype(int)
        
        return df1
    def feature_engineering(self, df2):
        
        df2['year']= df2['date'].dt.year

        df2['month'] = df2['date'].dt.month

        df2['day'] = df2['date'].dt.day

        df2['week_of_year'] = df2['date'].dt.isocalendar().week

        df2['year_week'] = df2['date'].dt.strftime('%Y-%W')

        df2['competition_since'] = df2.apply(lambda x: datetime.datetime(year=x['competition_open_since_year'],
                                                                         month=x['competition_open_since_month'],
                                                                         day=1),axis=1 )
        #date.fromtimestamp
        

        df2['compettion_time_month'] = ( ( df2['date'] - df2['competition_since'] )/30 ).apply(lambda x: x.days).astype(int)

        #join the columns promo2
        df2['promo_since'] = df2['promo2_since_year'].astype(str) + '-' + df2['promo2_since_week'].astype(str)

        # convent promo time week to datetime
        df2['promo_since'] = df2['promo_since'].apply(lambda x: datetime.datetime.strptime( x + '-1','%Y-%W-%w') - datetime.timedelta(days=7) )


        #calcule between start promo and continuation 
        df2['promo_time_week'] = (( df2['date'] - df2['promo_since'] ) /7 ).apply(lambda x: x.days).astype(int)

        # renome names assortment 
        df2['assortment'] = df2['assortment'].apply(lambda x: 'basic' if x== 'a' else 'extra' if x =='b'else 'extended')

        #rename state holiday

        df2['state_holiday']= df2['state_holiday'].apply(lambda x: 'public_holiday' if x=='a' 
                                                         else 'easter_holiday' if x=='b' 
                                                         else 'christmas' if x=='c'
                                                         else 'regular_day')
        ## 3.1 Filtering the data

        #filtereing the rows open and sales of dataset

        df2= df2.loc[df2['open'] > 0] 

        ## 3.2 Select the columns

        cols_drop= ['open','promo_interval','month_map']

        df2 = df2.drop( cols_drop,axis=1 )
        
        return df2
    
    def data_preparation(self, df5):
        
        ## 5.2 Rescaling

        selection = df5.select_dtypes( include = ['int64', 'float64'] )

        #competition_distance
        df5['competition_distance'] = self.competition_distance_scaler.fit( df5[['competition_distance']].values )

        #competition_time_month
        df5['compettion_time_month'] = self.compettion_time_month_scaler.fit( df5[['compettion_time_month']].values )

        #promo_time_week
        df5['promo_time_week'] = self.promo_time_week_scaler.fit( df5[['promo_time_week']].values )

        #year
        df5['year'] = self.year_scaler.fit( df5[['year']].values )

        ## 5. 3 Transformation


        ## 5.3.2 Enconding

        # ======================================= state_holiday ====================================== #

        # One Hot Enconding

        df5 = pd.get_dummies( df5, prefix= ['st_holiday'], columns = ['state_holiday'] )


        # ====================================== store type ============================================ #

        # Label Enconding 

        df5['store_type_encoded'] = self.store_type_encoded_scaler.fit(df5.store_type)
        

        # ===================================== assortment ============================================== #

        # Ordinal Encoding

        #created dictionary referencial
        types_assortment = {'basic': 1,
                           'extended':2,
                           'extra': 3 } 

        df5['assortment_ordinal'] = df5.assortment.map(types_assortment)

        ## 5.3.3 Nature Transformation

        # ===================================== day ========================================== #

        df5['day_sin'] = df5['day'].apply(lambda x: np.sin( x * (2 * np.pi/ 7 ) ) ) 
        df5['day_cos'] = df5['day'].apply(lambda x: np.cos( x * (2 * np.pi/ 7 ) ) )


        # ==================================== day of week ========================================= #

        df5['day_of_week_sin'] = df5['day_of_week'].apply(lambda x: np.sin( x * (2 * np.pi/ 7 ) ) ) 
        df5['day_of_week_cos'] = df5['day_of_week'].apply(lambda x: np.cos( x * (2 * np.pi/ 7 ) ) )



        # ==================================== month =============================================== #

        df5['month_sin'] = df5['month'].apply(lambda x: np.sin( x * (2 * np.pi / 12 ) ) )
        df5['month_cos'] = df5['month'].apply(lambda x: np.cos( x * (2 * np.pi / 12 ) ) )

        # ==================================== week of year ========================================= #

        df5['week_of_year_sin'] = df5['week_of_year'].apply(lambda x: np.sin( x * (2 * np.pi/ 53 ) ) )
        df5['week_of_year_cos'] = df5['week_of_year'].apply(lambda x: np.cos( x * (2 * np.pi/ 53 ) ) )
        
        cols_select = ['store','promo', 'store_type_encoded','assortment_ordinal',
                                    'competition_distance', 'competition_open_since_month',
                                    'competition_open_since_year','promo2','promo2_since_week','promo2_since_year',
                                    'compettion_time_month', 'promo_time_week','day_of_week_sin','day_of_week_cos',
                                    'month_sin','month_cos','day_sin','day_cos','week_of_year_sin',
                                    'week_of_year_cos']

        
        return df5[cols_select]
    
    def get_prediction (self, model, original_data, test_data):
        #prediction
        pred = model.predict( test_data )
        
        #join predict with original data
        original_data['prediction'] = np.expm1(pred)
        
        return original_data.to_json( orient = 'records', date_format = 'iso')