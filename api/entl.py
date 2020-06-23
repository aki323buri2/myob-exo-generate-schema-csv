from utils import fullpath 
import pandas as pd 
import os 

database = 'debtors'
camel = 'Debtors'

def createEntryList(database, camel):
  url = 'http://help.myob.com.au/exo/schemas/exo87/{}/entl.html'.format(camel)

  df = pd.read_html(url)[1]
  df.columns = df.iloc[0]
  df = df.reindex(df.index.drop(0))
  entl = df

  filename = fullpath('myobexo/{}/entl.csv'.format(database))
  os.makedirs(filename.parent, exist_ok=True)
  entl.to_csv(filename)

  return entl