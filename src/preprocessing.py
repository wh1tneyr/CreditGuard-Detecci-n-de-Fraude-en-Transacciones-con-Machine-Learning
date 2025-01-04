import pandas as pd
import os, sys
sys.path.append(os.getcwd())

# Leer dataset 
data = pd.read_csv('data/creditcard_2023.csv')

# Informacion del df
data.info()

# Descripcion del df
data.describe()

# Ver datos duplicados
data.duplicated().sum()

# -- No hay datos duplicados -- 

# Ver datos ausentes 
data.isna().sum()

# -- No hay datos ausentes -- 
