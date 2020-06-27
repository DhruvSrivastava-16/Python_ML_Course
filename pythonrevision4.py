# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:05:35 2020

@author: DHRUV
"""


import pandas as pd
import numpy as np
pokemons={'power': np.random.randint(1,200,5),'height': np.random.randint(10,100,5),'weight': np.random.randint(15,75,5)} 
df=pd.DataFrame(pokemons)
print(df)
csv_data=df.to_csv('pokemons.csv',index=False)
