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
        fout.write('<table>')



        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['information'].encode('utf-8'))
            fout.write('</tr>')


        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()