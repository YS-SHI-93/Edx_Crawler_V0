from selenium import webdriver
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class HtmlDownloader(object):
    
#    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#       'Accept-Encoding': 'none',
#       'Accept-Language': 'en-US,en;q=0.8',
#       'Connection': 'keep-alive'}
#    
#    url -- url to be downloaded
    
    

    def download(self, url):
        
        SCROLL_PAUSE_TIME = 1.5
        
        if url is None:
            return None
        
        driver = webdriver.Chrome(executable_path='C:\\~ANU\\edx_Crawler\\Edx_Crawler_V0\\edXCrawler\\phantomjs-2.1.1-windows\\bin\\chromedriver')
        driver.get(url)
        
        print(' ')
        print('we are downloading: '+str(url))
        print(' ')
        
        
        try:
            if url == 'https://www.edx.org/course?course=all':
                # Get scroll height
                last_height = driver.execute_script("return document.body.scrollHeight")
                
                while True:
                    # Scroll down to bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)
                
                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
            
            html = driver.page_source
        
        
#        soup = BeautifulSoup(
#        html,
#        'html.parser',
#        from_encoding='uft-8'
#        )
#        
#        print (soup.prettify())
           
#            element = WebDriverWait(driver, 10).until(
#                    EC.presence_of_element_located((By.ID, "footer-edx-v3"))
#                    )

            driver.close()
            
        finally:
            driver.quit()
            
        return html
        
        