class UrlManager(object):
    def __init__(self):
    #       set 1 to crawl
    #       set 2 already crawled
        self.new_urls = set()
        self.old_urls = set()
        
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            # totally new url -- to crawl 
            self.new_urls.add(url)
            
        

        
    def add_new_urls(self, urls):
        
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)
            
            
    def has_new_url(self):
        return len(self.new_urls)!=0 
#    not zero --> we have url to crawl 
                
#          get a new url from the list
    def get_new_url(self):
        new_url=self.new_urls.pop()
#        pop() == get and remove 
        self.old_urls.add(new_url)
        return new_url