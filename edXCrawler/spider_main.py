# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:20:24 2018

@author: u5755653
"""

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader  = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
        def craw(self, root_url):
            self.urls.add_new_url(root_url)
            try:
                    
                while self.urls.has_new_url():
                    new_url = self.urls.get_new_url()
                    html_cont = self.downloader.download(new_url)
                    new_urls, new_data = self.parser.parse(new_url, html_cont)
                    
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)
                    
                    self.outputer.output_html()

if __name__ == "__main__":
    root_url = ""
    obj_spider=SpiderMain()
    obj_spider,.craw(root_url)
    