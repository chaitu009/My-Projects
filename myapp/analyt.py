
from pandas.io.json import json_normalize
import pandas as pd
import requests
import json

def getdata(url):
     r = requests.get(url)
     data = json.loads(r.text)["data"]["history"]
     return data

def getdf(data):
     df_main =pd.DataFrame(columns = ["state","confirmed", "recovered","deaths", "active","day"])
     for i in data:
         df = json_normalize(i["statewise"])
         df['day'] = i['day']
         df_main = df_main.append(df)
         return df_main
