from utils import fullpath 
import pandas as pd 
import os 
from entl import createEntryList

database = 'crm'
camel = 'CRM'

def createAttributes(database, camel):
  entd_url = 'http://help.myob.com.au/exo/schemas/exo87/{}/entd.html'.format(camel)

  root_dir = fullpath('myobexo', database)
  
  entl = createEntryList(database, camel)

  def attributes_csv(name):
    return root_dir / 'attributes' / '{}.csv'.format(name)  

  tables = pd.read_html(entd_url)

  def firstRowIsColumn(df):
    df.columns = df.iloc[0]
    return df.reindex(df.index.drop(0))

  tables = [
    firstRowIsColumn(df) for df in tables 
  ]

  tables = [
    df for df in tables if 'Column name' in df.columns
  ]

  def genCsv(df, filenmae):
    os.makedirs(filename.parent, exist_ok=True)
    df.to_csv(filename)

  for i, name in enumerate(entl.Name):
    df = tables[i]
    filename = fullpath(attributes_csv(name))
    genCsv(df, filename)