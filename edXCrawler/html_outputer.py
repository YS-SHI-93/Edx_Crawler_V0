# Outputer
class HtmlOutputer(object):

    def __init__(self):
        self.datas = list()

    # collect data from the crawled data variable
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # write into output.html
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
            
            f.write('<th>')
            f.write('Type')
            f.write('<\th>')
            
            f.write('<th>')
            f.write('Flags')
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
                f.write('<td>%s</td>' % data['Type'])
                f.write('<td>%s</td>' % data['Flag'])
                f.write('</tr>')
    
    
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
    
            f.close()