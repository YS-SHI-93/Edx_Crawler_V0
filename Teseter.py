# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:56:35 2018

@author: u5755653
"""
import pandas as pd
import re
import numpy as ny
from scipy import stats
import pandas.plotting as plotting
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

from statsmodels.sandbox.regression.predstd import wls_prediction_std


file_location = 'C:\\~ANU\\edx_Crawler\\Edx_Crawler_V0\\edXCrawler\\Data_analysis\\Data.xlsx'
    
def parse_week(week):

        
    if week is None or week =='' or week == 'na':
        return None
    
#       irregularities found
    if "hours" in week or \
    "horas" in week or \
    "days" in week or \
    "Days" in week or \
    "module" in week or \
    "modules" in week or \
    "Module" in week or \
    "Modules" in week or \
    "semanas" in week or \
    "Semanas" in week or \
    "Semanas" in week or \
    "sections" in week or \
    "Sections" in week:
        return None
    
    #    effort_regular = "3-5weeks"
    
    match = re.search(r'\d+-\d+', week)
        
        
    if match:
        match = match.group()
        match = re.findall(r'(\d+)',match)
        return match
    else:
        return [int(s) for s in week.split() if s.isdigit()]

def read(file_location):
    df = pd.read_excel(file_location, 'Sheet1')
    return df

def parse_length(df):
    length=df['Length']
    l=[]
    for item in length:
#        print(item)
        if type(item) is not str:
            item = str(item)
        item=parse_week(item)
        l.append(item)
#        print(len(l))
    return l


def parse_efforts(df):
    
    DEFAULT_WEEK = 1
    l=[]
    
    efforts=df['Recommended_Max_Effort']
    
    for i, effort in enumerate(efforts):
        if not ny.isnan(df['length_parsed_average'][i]):
            DEFAULT_WEEK = df['length_parsed_average'][i]
        
            
#        print(item)
        if type(effort) is not str:
            effort = str(effort)
            
        if effort == "":
            l.append(ny.nan)
        if effort is None:
            l.append(ny.nan)
            
        #       regular    
        match = re.search(r'\d+ to \d+', effort)
        if match:
            match = match.group()
            match = re.findall(r'(\d+)',match)
#           effort_ir8 = "Most users will find that thoroughly covering the material will take anywhere from 40 to 60 hours"
        
            if int(match[0]) >20 or int(match[1])>20:
                for index, value in enumerate(match):
                    value = int(value) / DEFAULT_WEEK
                    match[index] = value
            l.append(list(map(int,match)))
        else:
        
    #    effort_ir7 = "每周 3-5 小时"
            match = re.search(r'\d+-\d+', effort)
            
            #    effort_ir9 = "每周 30-50 小时"
            if match:
                match = match.group()
    #                print("#########")
    #                print(match)
                match = re.findall(r'(\d+)',match)
                
                if int(match[0]) > 20 or int(match[1]) > 20:
                    for index, value in enumerate(match):
                        value = int(value) / DEFAULT_WEEK
                        match[index] = value
                l.append(list(map(int,match)))
                
                
            else:
            #    effort_ir1 = "18 hours per week"
            #    effort_ir2 = "8 hours/week"
            #    effort_ir4 = "12+ hours per week"
                match = re.search(r'(\d+)', effort)

                #    effort_ir3 = "30 heures au total"
                #    effort_ir6 = "84 hours self-paced"
                
                if match:
                    match = match[1]

                    if int(match)>20:
                        match=int(match)/DEFAULT_WEEK
                    
                    l.append([int(match)])
                else:
                    #    effort_ir5 = "na"
                    l.append(ny.nan)
            
    return l
    #        print(len(l))    
    
    

    


    
    
    

df=read(file_location)
df.insert(loc=0,column='length_parsed',value=parse_length(df))

#print(df['length_parsed'])

source_col = df['length_parsed']
length_min = []
length_max = []

for x in source_col:
    try:
        if len(x)==0:
            length_min.append(ny.nan)
            length_max.append(ny.nan)
        elif len(x)==1:
            length_min.append(x[0])
            length_max.append(x[0])
        elif len(x)==2:
            length_min.append(x[0])
            length_max.append(x[1])
        else:
            length_min.append(ny.nan)
            length_max.append(ny.nan)
    except TypeError:
        length_min.append(ny.nan)
        length_max.append(ny.nan)
        

    
df['length_parsed_min'] = length_min
df['length_parsed_max'] = length_max
df['length_parsed_min'].convert_objects(convert_numeric=True)
df['length_parsed_max'].convert_objects(convert_numeric=True)
#print(df[['length_parsed_min','length_parsed_max']] )
df['length_parsed_average'] = df[['length_parsed_min', 'length_parsed_max']].apply(ny.mean, axis=1)

df.insert(loc=0,column='effort_parsed',value=parse_efforts(df))
print(df['effort_parsed'])

source_col = df['effort_parsed']
effort_min = []
effort_max = []

for x in source_col:
    try:
        if len(x)==0:
            effort_min.append(ny.nan)
            effort_max.append(ny.nan)
        elif len(x)==1:
            effort_min.append(x[0])
            effort_max.append(x[0])
        elif len(x)==2:
            effort_min.append(x[0])
            effort_max.append(x[1])
        else:
            effort_min.append(ny.nan)
            effort_max.append(ny.nan)
    except TypeError:
        effort_min.append(ny.nan)
        effort_max.append(ny.nan)
        
        
        
        

df['effort_parsed_min'] = effort_min
df['effort_parsed_max'] = effort_max
df['effort_parsed_min'].convert_objects(convert_numeric=True)
df['effort_parsed_max'].convert_objects(convert_numeric=True)
df['effort_parsed_average'] = df[['effort_parsed_min', 'effort_parsed_max']].apply(ny.mean, axis=1)

df['Price_Number'].convert_objects(convert_numeric=True)

#pandas.factorize

df['Institution_factorised']= pd.factorize(df['Institution'], na_sentinel=ny.nan)
#df.boxplot(column='Price_Number', by =['Level'],showmeans=True,,return_type='dict')



'''
df.to_excel('test_output_data.xlsx', sheet_name='Sheet1')


#price stat
df['Price_Number'].describe(percentiles=[.05, .25, .75, .95])

plotting.scatter_matrix(df[['Price_Number', 'length_parsed_average']], alpha=0.2, figsize=(6, 6))
plotting.scatter_matrix(df[['Price_Number', 'effort_parsed_average']], alpha=0.2, figsize=(6, 6))

df['effort_parsed_average'].mean()
df['effort_parsed_average'].std()
S=pd.Series(df['effort_parsed_average'])
S[~((S-S.mean()).abs()>3*S.std())].mean()

S=pd.Series(df['Price_Number'])
df['Price_Number_drop_outliers']=S[~((S-S.mean()).abs()>3*S.std())]



df['length_parsed_average'].mean()
df['length_parsed_average'].std()
S2=pd.Series(df['length_parsed_average'])
S2[~((S2-S2.mean()).abs()>3*S2.std())].mean()

S2=pd.Series(df['length_parsed_average'])
df['length_drop_outliers']=S2[~((S2-S2.mean()).abs()>3*S2.std())]
'''
formula='Price_Number ~ Institution+Level+Subject+Languages'



#print(df.head())
#
Introductory_price = df[df['Level'] == 'Introductory']['Price_Number']
Intermediate_price = df[df['Level'] == 'Intermediate']['Price_Number']
Advanced_price = df[df['Level'] == 'Advanced']['Price_Number']

stats.ttest_ind(Introductory_price, Intermediate_price, nan_policy ='omit')
stats.ttest_ind(Introductory_price, Advanced_price, nan_policy ='omit')
stats.ttest_ind(Intermediate_price, Advanced_price, nan_policy ='omit')


stats.ttest_ind(Intermediate_price,Introductory_price , nan_policy ='omit')
df['Languages'].replace('English, English','English',inplace=True)

df['Languages'].replace('Simplified Chinese, 中文','中文',inplace=True)
df['Languages'].replace('Simplified Chinese','中文',inplace=True)
df['Languages'].replace('中文, Simplified Chinese','中文',inplace=True)
