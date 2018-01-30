from bs4 import BeautifulSoup


class HtmlParser(object):
    
    # 获取其中的内容（关键词，简介）
    def __get_new_data(self,page_url,soup):
        res_data = {}

        res_data['url'] = page_url

        # 获取关键词
        cards = soup.find_all('span', class_='block-list__desc')
        res_data['Length'] = cards[0].get_text()
        res_data['Effort'] = cards[1].get_text()
        res_data['Price'] = cards[2].get_text().strip()
        res_data['Institution'] = cards[3].get_text().strip()
        res_data['Subject'] = cards[4].get_text().strip()
        res_data['Level'] = cards[5].get_text().strip()
        res_data['Languages'] = cards[6].get_text().strip()
        res_data['Video Transcripts'] = cards[7].get_text().strip()
#        for card in cards:
#            res_data['information'] = card.get_text()

#        # 获取简介
#        summary_node = soup.find('div', class_ = 'lemma-summary')
#        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析htnl字符串
    def parse(self,page_url,html_cont):
        if  html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
#        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        
        print(" ")
        
        print("our current new data is: " + str(new_data))

        
        return new_data