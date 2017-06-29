import urlparse
from bs4 import BeautifulSoup
import re
from setuptools.package_index import HREF

class HtmlParser(object):
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return 
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		
		new_urls=self._get_new_urls(page_url, soup)
		#new_data=self._get_new_data(page_url, soup)
		new_data=0
		return new_urls,new_data

	def _get_new_urls(self,page_url,soup):
		new_urls=set()
		links = soup.find_all('a',href=re.compile(''))
		
		for link in links:
			new_url =link['href']
			if new_url.startswith('http'):
			#new_full_url =urlparse.urljoin(page_url,new_url)
			#new_urls.add(new_full_url)
				new_urls.add(new_url)
		return new_urls
		
	def _get_new_data(self,page_url,soup):
		res_data ={}
		res_data['url']=page_url
		
		title_node=soup.find('dd',class_="lemmanWgt-lemmaTitle-title").find("h1")
		print 3
		res_data['title'] = title_node.get_text();
		print 4
		summary_node=soup.find('div',class_="lemma-summary")
		res_data['summary'] = summary_node.get_text();
		
		return res_data