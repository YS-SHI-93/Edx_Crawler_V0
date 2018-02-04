from bs4 import BeautifulSoup


class HtmlParser(object):
    
    # 获取其中的内容（关键词，简介）
    def __get_new_data(self,page_url,soup):
        res_data = {}

        res_data['url'] = page_url

        # Obtain the information wanted
        course_meta = soup.find('ul', class_='clear-list block-list content-block')
        cards = course_meta.find_all('li')
        print("the length of cards is ")
        cards_len = len(cards)
        print(cards_len)
        print(" ")
        
        course_length1 = course_meta.find(attrs={"data-field": "length"})
        course_effort = course_meta.find(attrs={"data-field": "effort"})
        course_type = course_meta.find(attrs={"data-field": "type"})
        course_price = course_meta.find(attrs={"data-field": "price"})
        course_school = course_meta.find(attrs={"data-field": "school"})
        course_subject = course_meta.find(attrs={"data-field": "subject"})
        course_level = course_meta.find(attrs={"data-field": "level"})
        course_language = course_meta.find(attrs={"data-field": "language"})
        course_video_transcript = course_meta.find(attrs={"data-field": "video-transcript"})
        
#       meta-data to be obtained 
        '''
        Meta1
        '''
        if course_length1 is not None:
            res_data['Length'] = course_length1.find('span', class_='block-list__desc').get_text().strip()
        else:
            res_data['Length'] = 'na'
        '''
        Meta2
        '''
        if course_effort is not None:
            res_data['Effort'] = course_effort.find('span', class_='block-list__desc').get_text().strip()
        else:
            res_data['Effort'] = 'na'
        '''
        Meta3
        '''
        if course_type is not None:
            res_data['Type'] = course_type.find('span', class_='block-list__desc').get_text().strip()
        
        else:
            res_data['Type'] = 'na'
        '''
        Meta4
        '''
        if course_school is not None:
            res_data['Institution'] = course_school.find('span', class_='block-list__desc').get_text().strip()
        
        else:
            res_data['Institution'] = 'na'
        '''
        Meta5
        '''
        if course_subject is not None:
            res_data['Subject'] = course_subject.find('span', class_='block-list__desc').get_text().strip()
        
        else:
            res_data['Subject'] = 'na'
        '''
        Meta6
        '''
        if course_level is not None:
            res_data['Level'] = course_level.find('span', class_='block-list__desc').get_text().strip()
        
        else:
            res_data['Level'] = 'na'
        '''
        Meta7
        '''
        if course_language is not None:
            res_data['Languages'] = course_video_transcript.find('span', class_='block-list__desc').get_text().strip()
         
        else:
            res_data['Languages'] = 'na'
        '''
        Meta8
        '''
        if course_video_transcript is not None:
            res_data['Video Transcripts'] = course_video_transcript.find('span', class_='block-list__desc').get_text().strip()
         
        else:
            res_data['Video Transcripts'] = 'na'
        '''
        Meta9
        '''
        if course_price is not None:
            res_data['Price'] = course_price.find('span', class_='block-list__desc').get_text().strip().replace(u'\xa0', u' ')
        
        else:
            res_data['Price'] = 'na'
        
        #Checking if numbers are matched
        effective_count = 0
        for item in res_data.values():
#            print('item: '+ str(type(item)))
            
            if item != 'na' and item != '' and item is not None:
                effective_count=effective_count+1
                print(effective_count)
            print("==")
            print(item)
            print("==")

            
            
        if cards_len!=(effective_count-1):
            print(effective_count)
            res_data['Flag'] = 'Y: List has at least 1 Missing Label(s)'
            
        #    maybe there will be other cases 
        #elif:
        #    pass
        
        else:
            res_data['Flag'] = 'N'
        effective_count = 0
            
        return res_data

    # Parse the HTML tags
    def parse(self,page_url,html_cont):
        if  html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
#        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)
        
        print(" ")
        
        print("our current new data is: " + str(new_data))

        
        return new_data