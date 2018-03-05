# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:56:52 2018

@author: u5755653
"""
import pandas as pd

class excel_reader(object):
    def read(file_location):
        df = pd.read_excel(file_location,sheet_name='Sheet2')
        return df
    
#excel_reader.read('C:\\~ANU\\edx_Crawler\\Edx_Crawler_V0\\edXCrawler\\Data_analysis\\Data.xlsx')