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
        

#        self.urls.add_new_url(root_url)  # add a url to url manager
        
        count = 1  # How many urls has been written into the output.html file
        ''' 
        To find all the course hyperlinks
        '''

        '''
        html_cont = self.downloader.download(root_url) 
        course_urls = self.recorder.get_root_urls(html_cont)
        
        print (' ')
        print ('Now we have this number of URLs')
        print (len(course_urls))
        for course_url in course_urls:
            self.urls.add_new_url(course_url)
        
        '''
        
        '''
        依次打开urls
        '''
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                
                print (count, new_url)
                print ('######################################')
    
                course_html_cont = self.downloader.download(new_url) #download a page in that specific web-page
                
                print (" ---!--- ")
                
                print (str(new_url)+": this one has been downloaded")
                
                new_data = self.parser.parse(new_url, course_html_cont)
                
                self.outputer.collect_data(new_data)
                
                if count == 2018:
                    break
                
                count = count+1
                
                
            except:
                print ("Couldn't crawl further")
                
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://www.edx.org/course/?course=all&subject=Architecture"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
    