import pandas as pd
import os, sys
sys.path.append(os.getcwd())

#importar dataset 
data = pd.read_csv('data/creditcard_2023.csv')

#ver informacion del dataset
data.info()

#ver descripcion del df
data.describe()