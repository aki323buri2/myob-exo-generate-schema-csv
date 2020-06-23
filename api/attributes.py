from utils import fullpath 
import pandas as pd 
import os 

# database = 'crm'
# camel = 'CRM'

root_dir = fullpath('../myobexo')
entl_url = lambda camel: 'http://help.myob.com.au/exo/schemas/exo87/{}/entl.html'.format(camel)
entd_url = lambda camel: 'http://help.myob.com.au/exo/schemas/exo87/{}/entd.html'.format(camel)


def attributes_csv(database, name):
  return root_dir / database / 'attributes' / '{}.csv'.format(name)  

def firstRowIsColumn(df):
  df.columns = df.iloc[0]
  return df.reindex(df.index.drop(0))

def generateCsv(df, filename):
  os.makedirs(filename.parent, exist_ok=True)
  df.to_csv(filename)

def createEntryList(database, camel):

  df = pd.read_html(entl_url(camel))[1]
  df = firstRowIsColumn(df)
  entl = df

  filename = fullpath(root_dir, database, 'entl.csv')
  os.makedirs(filename.parent, exist_ok=True)
  entl.to_csv(filename)

  return entl

def createAttributes(database, camel):

  entl = createEntryList(database, camel)

  tables = pd.read_html(entd_url(camel))

  tables = [
    firstRowIsColumn(df) for df in tables 
  ]

  tables = [
    df for df in tables if 'Column name' in df.columns
  ]

  for i, name in enumerate(entl.Name):
    df = tables[i]
    filename = fullpath(attributes_csv(database, name))
    generateCsv(df, filename)