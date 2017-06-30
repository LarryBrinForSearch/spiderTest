#coding:utf-8
import bsddb
import os,sys,string
from bdb_test import bdb_solve
from test1 import bdb_test

class UrlManager(object):
	def __init__(self):
		self.bdb=bdb_test.bdb_solve()
		self.new_urls = self.bdb.createQueue()
		self.old_urls = self.bdb.createHash()
		
	def add_new_url(self,url):
		if url is None:
			return
		if not self.old_urls.has_key(url.encode('utf-8')):
			self.new_urls.append(url.encode('utf-8'))
	
	def add_new_urls(self,urls):
		if urls is None or len(urls)==0:
			return 
		for url in urls:
			self.add_new_url(url)
	
	#判断是否还有url未读
	def has_new_url(self):
		return len(self.new_urls)!=0

	def get_new_url(self):
		#先取出一个url
		tuples=self.new_urls.consume()	
		while tuples is not None:
			[id,new_url]=tuples
			#判断该URL是否被访问过
			if not self.old_urls.has_key(new_url.encode('utf-8')):
				#如果没被访问过，则将要访问
				self.old_urls.put(new_url.encode('utf-8').rstrip(),'0')
				return new_url
			tuples=self.new_urls.consume()		
		return None
	
	def close_db(self):
		self.bdb.close_db()
	'''
	def add_new_url(self,url):
		if url is None:
			return 
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)
	
	def add_new_urls(self,urls):
		if urls is None or len(urls)==0:
			return 
		for url in urls:
			self.add_new_url(url)
	
	#判断是否还有url未读
	def has_new_url(self):
		return len(self.new_urls) !=0

	def get_new_url(self):
		new_url =self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
	'''