# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:20:24 2018

@author: u5755653
"""
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader  = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):
        count = 1  # 记录成功条数

        self.urls.add_new_url(root_url)  # 添加url到url管理器
        
        
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print (count, new_url))
                html_cont = self.downloader.download(new_url) # 根据url下载网页
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 50:
                    break
                
                count = count+1
                
                
            except:
                print ("Couldn't crawl further")
                
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://www.edx.org/course/?course=all&availability=current&language=English"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
    