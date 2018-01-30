# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:26:59 2018

@author: u5755653
"""

import io
with io.open("output.html", "w", encoding="utf-8") as f:

    datas = list()
    
    res_data = {}
    
    res_data['kte'] = '你是煞笔么'
    res_data['sw2'] = '真日了狗了'
    res_data['xstt'] = '我了个去'
    
    datas.append(res_data)
    
    count=0
    
    f.write('<html>')
    f.write('<body>')
    f.write('<p style="width:100%">')
    
    for data in datas:
        count=count+1
        f.write(data['kte'])
    #    fout.write(data['sw2'])
    #    fout.write(data['xstt'])
    
    f.write('</p>')
    f.write('</body>')
    f.write('</html>')
    
    f.close()

    
        