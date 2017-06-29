#coding:utf-8
count=2
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)
    
    def output_html(self,page_url,url_cont):
        filename=count+'.html'
        print filename
        fout=open(filename,'w')
        fout.write(url_cont)
        fout.close()
        
        count=count+1
        '''
        fout.write("<html>")
        fout.write("<body>")
        
        for data in self.datas:
            fout.write(data['url'])
            fout.write("-%s--" % data['title'].encode('utf-8'))
            fout.write("-%s<br>" % data['summary'].encode('utf-8'))
        fout.write("</body>")
        fout.write("</html>")
        '''