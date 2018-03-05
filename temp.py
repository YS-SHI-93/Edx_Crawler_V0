import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import re

http = urllib3.PoolManager()


outputfile = open("index.csv", "a")


title_data = pd.read_excel('d.xlsx', sheetname=1)
url_data = pd.read_excel('data.xlsx', sheetname=1)
titles = title_data.ix[:, 3]
course_numbers = title_data.ix[:, 1]
urls = url_data.ix[:, 0]
prices = url_data.ix[:, 3]

price_digit = map(lambda a: re.sub("\D", "", a), prices)

for index in range(0, url_data.shape[0]):
    key = url_data.ix[index, 0]
    r = http.request('GET', key)
    data = r.data
    try:
        soup = BeautifulSoup(data, 'html.parser', from_encoding = 'utf-8')
        course_title = soup.find('title').get_text().split('|')[0].strip()
        outputfile.write(bytes(index) + ',' + key + ',' + course_title + '\n')
    except:
        print('Error!')
    else:
        print(bytes(index) + ',' + key + ',' + course_title)
    
outputfile.close()


