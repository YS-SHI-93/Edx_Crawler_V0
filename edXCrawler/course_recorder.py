# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:36:28 2018

@author: u5755653
"""

from bs4 import BeautifulSoup


class CourseRecorder(object):
    
#    Todo: Obtain all the urls from the root
    
    def get_root_urls(self, soup):
        new_urls = set()
        
        soup = BeautifulSoup(soup, 'html.parser', from_encoding='utf-8')
        links = soup.find_all("a", class_="course-link")
        
        for link in links:
            print('We got: ' + str(link['href']))
            new_full_url = link['href'] # Get URL
#            new_full_url = 'https://www.edx.org'+new_url # CONCAT URLS
            new_urls.add(new_full_url)
        
        print ('our whole package is: '+ str(new_urls))
        print ('############ root done #################')
        return new_urls