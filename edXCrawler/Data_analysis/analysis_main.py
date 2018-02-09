# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:41:08 2018

@author: u5755653
"""

import re
import excel_reader

class main():
    def __init__(self):
        global DEFAULT_WEEK
        DEFAULT_WEEK = 4
        global location
        LOCATION = 'Data.xlsx'
        self.data = excel_reader.excel_reader()
        
#    def do(self):
#        data_raw = self.data.read(LOCATION)
#        for thing in data['Length']:
            
        
    def parse_week(self, week):

        
        if week is None or week =='' or week == 'na':
            return None
        
#       irregularities found
        if "hours" in week or \
        "horas" in week or \
        "days" in week or \
        "Days" in week or \
        "module" in week or \
        "modules" in week or \
        "Module" in week or \
        "Modules" in week or \
        "semanas" in week or \
        "Semanas" in week or \
        "Semanas" in week or \
        "sections" in week or \
        "Sections" in week:
            return None
        
        #    effort_regular = "3-5weeks"
        
        match = re.search(r'\d+-\d+', week)
            
            
        if match:
            match = match.group()
            match = re.findall(r'(\d+)',match)
            return match
        else:
            return [int(s) for s in week.split() if s.isdigit()]
        
    def parse_efforts(self, effort):
        if effort =="":
            return 
        if effort is None:
            return
        
#       regular
        match = re.search(r'\d+ to \d+', effort)
        
        if match:
            match = match.group()
            match = re.findall(r'(\d+)',match)
#           effort_ir8 = "Most users will find that thoroughly covering the material will take anywhere from 40 to 60 hours"
            if int(match[0]) >20 or int(match[1])>20:
                for index, value in enumerate(match):
                    value = int(value) / DEFAULT_WEEK
                    match[index] = value
            return list(map(int,match))
        else:
            
        #    effort_ir7 = "每周 3-5 小时"
            match = re.search(r'\d+-\d+', effort)
            
            #    effort_ir9 = "每周 30-50 小时"
            if match:
                match = match.group()
#                print("#########")
#                print(match)
                match = re.findall(r'(\d+)',match)
                
                if int(match[0]) > 20 or int(match[1]) > 20:
                    for index, value in enumerate(match):
                        value = int(value) / DEFAULT_WEEK
                        match[index] = value
                return list(map(int,match))
                
                
            else:
            #    effort_ir1 = "18 hours per week"
            #    effort_ir2 = "8 hours/week"
            #    effort_ir4 = "12+ hours per week"
                match = re.search(r'(\d+)', effort)
#                print ('*****')
#                print (match)
                #    effort_ir3 = "30 heures au total"
                #    effort_ir6 = "84 hours self-paced"
                
                if match:
                    match = match[1]
#                    print("~~~~~~")
#                    print(match)
                    if int(match)>20:
                        return [int(match)/DEFAULT_WEEK]
                    
                    return [match]
                else:
                    #    effort_ir5 = "na"
                    return None
        
        
        
if __name__ == "__main__":
    
    main = main()
    
    print("week :")
    res=main.parse_week("100 days")
    print()
    print(res)
    
    '''
    List of all the irregularities identified
    '''  
    
'''
    effort = "12 to 14 hours per week"
    effort_regular2 = "2 to 4 hours per week"

    effort_ir1 = "to 18 hours per week"
    effort_ir2 = "8 hours/week"
    effort_ir3 = "30 heures au total"
    effort_ir4 = "12+ hours per week"
    effort_ir5 = "na"
    effort_ir6 = "84 hours self-paced"
    effort_ir7 = "每周 3-5 小时"
    effort_ir8 = "Most users will find that thoroughly covering the material will take anywhere from 40 to 60 hours"
    
    res=main.parse_efforts(effort)
    print(effort_ir1+":")
    res=main.parse_efforts(effort_ir1)
    print()
    print(res)
    
    print(effort_ir2+":")
    res=main.parse_efforts(effort_ir2)
    print()
    print(res)
    
    print(effort_ir3+":")
    res=main.parse_efforts(effort_ir3)
    print()
    print(res)
    
    print(effort_ir4+":")
    res=main.parse_efforts(effort_ir4)
    print()
    print(res)
    
    print(effort_ir5+":")
    res=main.parse_efforts(effort_ir5)
    print()
    print(res)
    
    print(effort_ir6+":")
    res=main.parse_efforts(effort_ir6)
    print()
    print(res)
    
    print(effort_ir7+":")
    res=main.parse_efforts(effort_ir7)
    print()
    print(res)
    
    print(effort_ir8+":")
    res=main.parse_efforts(effort_ir8)
    print()
    print(res)

    print("week :")
    res=main.parse_week("5 weeks")
    print()
    print(res)
'''