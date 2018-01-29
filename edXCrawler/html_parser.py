from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    

    # 获取其中的url
    def __get_new_urls(self,page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/course/[a-zA-Z0-9%]+')) # 匹配url，可能会发生变化
        for link in links:
            new_url = link['href'].encode('utf-8') # 获取url
            new_full_url = 'https://www.edx.org'+new_url # 拼接url
            new_urls.add(new_full_url)
        return new_urls

    # 获取其中的内容（关键词，简介）
    def __get_new_data(self,page_url,soup):
        res_data = {}

        res_data['url'] = page_url

        # 获取关键词
        cards = soup.find_all('span', class_='block-list__desc')
        for card in cards:
            res_data['information'] = card.get_text()

#        # 获取简介
#        summary_node = soup.find('div', class_ = 'lemma-summary')
#        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析htnl字符串
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        return new_urls, new_data