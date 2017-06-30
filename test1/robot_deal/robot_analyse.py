#coding=utf-8
#任意给定一个url，返回其robots.txt
 

import robotparser
import urlparse

class robot_analyse(object):
	"""docstring for robot_analyse"""
	def __init__(self):
		super(robot_analyse, self).__init__()
		
	def get_robots(self,url):
	    #1.解析URL，抽取协议及域名部分
	    urltuple = urlparse.urlparse(url)
	    url = urltuple.scheme+'://'+urltuple.netloc
	    # print url

	    #2.读取robots协议
	    rp = robotparser.RobotFileParser()
	    #得到robots.txt
	    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
	    rp.read()
	    return rp
	    pass

	def judge(self,user_agent,url):
		rp = self.get_robots(url)
		return rp.can_fetch(user_agent, url)
		pass

#注：对于未添加过 robots.txt 文件的站点，can_fetch 方法默认返回 False。
