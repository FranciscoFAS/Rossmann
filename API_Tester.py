import json

import requests
from flask          import request
import pandas as pd

df10 = pd.read_csv( 'C:/Users/af_na/repos/ds_em_producao/data/test.csv' )

df_store_raw = pd.read_csv( 'C:/Users/af_na/repos/ds_em_producao/data/store.csv' )

df_test = pd.merge(df10, df_store_raw, how='left', on='Store')

df_test = df_test[df_test['Store'].isin( [20, 23, 22] )]

df_test = df_test[df_test['Open'] != 0]
df_test = df_test[~df_test['Open'].isnull()]
df_test = df_test.drop( 'Id', axis=1 )

data = json.dumps( df_test.to_dict( orient='records'))

url = 'https://rossmann-store-sales.onrender.com'
header = {'Content-type': 'application/json'}
data = data

r = requests.post(url, data=data, headers=header)
print('Status Code {}'.format(r.status_code))