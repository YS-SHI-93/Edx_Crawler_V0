# 数据输出器
class HtmlOutputer(object):

    def __init__(self):
        self.datas = list()

    # 添加数据到列表中
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出到html文件中
    def output_html(self):
        import io
        with io.open("output.html", "w", encoding="utf-8") as f:
            
#        f = open(r'output.html','w')

            f.write('<html>')
            f.write('<body>')
            f.write('<table style="width:100%">')
    
            f.write('<tr>')
            f.write('<th>')
            f.write('url')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Length')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Effort')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Price')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Institution')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Subject')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Level')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Languages')
            f.write('<\th>')
    
            f.write('<th>')
            f.write('Video Transcripts')
            f.write('<\th>')
            
            for data in self.datas:
                
                f.write('<tr>')
                f.write('<td>%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['Length'])
                f.write('<td>%s</td>' % data['Effort'])
                f.write('<td>%s</td>' % data['Price'])
                f.write('<td>%s</td>' % data['Institution'])
                f.write('<td>%s</td>' % data['Subject'])
                f.write('<td>%s</td>' % data['Level'])
                f.write('<td>%s</td>' % data['Languages'])
                f.write('<td>%s</td>' % data['Video Transcripts'])
                
                f.write('</tr>')
    
    
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
    
            f.close()