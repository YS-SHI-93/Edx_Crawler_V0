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
        fout = open(r'output.html','w')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table style="width:100%">')

        fout.write('<tr>')
        fout.write('<th>')
        fout.write('url')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Length')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Effort')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Price')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Institution')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Subject')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Level')
        fout.write('<\th>')
        
        fout.write('<th>')
        fout.write('Languages')
        fout.write('<\th>')

        fout.write('<th>')
        fout.write('Video Transcripts')
        fout.write('<\th>')
        
        for data in self.datas:
            
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['Length'])
            fout.write('<td>%s</td>' % data['Effort'])
            fout.write('<td>%s</td>' % data['Price'])
            fout.write('<td>%s</td>' % data['Institution'])
            fout.write('<td>%s</td>' % data['Subject'])
            fout.write('<td>%s</td>' % data['Level'])
            fout.write('<td>%s</td>' % data['Languages'])
            fout.write('<td>%s</td>' % data['Video Transcripts'])
            
            fout.write('</tr>')


        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()