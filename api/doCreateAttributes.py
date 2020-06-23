from utils import fullpath 
import pandas as pd 

from attributes import createAttributes 

if __name__ == '__main__':

  databases = [
    ['creditors'  , 'Creditors'  ], 
    ['debtors'    , 'Debtors'    ], 
    ['stock'      , 'Stock'      ], 
    ['crm'        , 'CRM'        ], 
    ['jobCosting' , 'JobCosting' ], 
  ]

  for database, camel in databases:
    print('{} is in process...'.format(database))
    createAttributes(database, camel)
    print('{} is created!'.format(database))