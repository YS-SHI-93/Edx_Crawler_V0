# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:20:24 2018

@author: u5755653
"""
import url_manager
import html_downloader
import html_parser
import html_outputer
import course_recorder

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader  = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.recorder = course_recorder.CourseRecorder()
        
    def craw(self, root_url):
        

#        self.urls.add_new_url(root_url)  # 添加url到url管理器
        
        
        ''' 
        添加root url到url管理器,并爬取该页面上所有的course hyperlink
        '''
        count = 1  # 记录成功条数
        
        html_cont = self.downloader.download(root_url) # 根据url下载网页
        course_urls = self.recorder.get_root_urls(html_cont)
        
        
        for course_url in course_urls:
            self.urls.add_new_url(course_url)
        
        print (' ')
        print ('loaded')
        
        '''
        依次打开urls
        '''
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print (count, new_url)
                print ('######################################')
    
                html_cont = self.downloader.download(new_url) # 根据url下载网页
#                course_urls = self.recorder.get_root_urls(html_cont)
                
                new_data = self.parser.parse(new_url, html_cont)
                
#               self.urls.add_new_urls(new_urls)
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
    