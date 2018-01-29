from selenium import webdriver
#from bs4 import BeautifulSoup

class HtmlDownloader(object):
    
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    
#    url -- url to be downloaded
    def download(self, url):
        if url is None:
            return None
        
        driver = webdriver.Chrome(executable_path='C:\\~ANU\\edx_Crawler\\Edx_Crawler_V0\\edXCrawler\\phantomjs-2.1.1-windows\\bin\\chromedriver')
        driver.get(url)
        html = driver.page_source
        return html
        
        