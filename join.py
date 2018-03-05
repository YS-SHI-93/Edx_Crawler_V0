# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:02:58 2018

@author: u5755653
"""

import pandas as pd
import re
import numpy as ny
from scipy import stats

df_data = pd.read_excel('data.xlsx', 'Sheet1')
df_title = pd.read_csv('index.csv','index', names = ["index", "url", "title"])

print (df_title.columns)
print (df_title)
result = pd.merge(df_data, df_title, how='inner', on=['url'])

print(result)
