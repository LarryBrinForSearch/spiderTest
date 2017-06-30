
#coding:utf-8
import url_manager,html_downloader,html_outputer,html_parser

from bs4 import BeautifulSoup
from test1.url_manager import UrlManager

class SpiderMain(object):
	def __init__(self):
		self.urls=url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser=html_parser.HtmlParser()
		self.outputer=html_outputer.HtmlOutputer();
	
	def craw(self,root_url):
		count=1
		#现将入口url添加进去
		self.urls.add_new_url(root_url)
		print 'aa'
		new_url=self.urls.get_new_url()
		
		while new_url is not None:
			try:
				print 'craw %d : %s'% (count,new_url)
				
				html_cont=self.downloader.download(new_url)
				
				#得到新的要爬取的URL
				new_urls,new_data=self.parser.parse(new_url, html_cont)
				
				self.urls.add_new_urls(new_urls)
				#self.outputer.collect_data(new_data)
				self.outputer.output_html(new_url, html_cont)
				print 'sss'
			
			except:
				print 'craw failed'	
			
			count=count+1
			if count==20:
				self.urls.close_db()
				break
			
			new_url=self.urls.get_new_url()	
		
if __name__=="__main__":
	root_url = "http://www.baidu.com"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
	