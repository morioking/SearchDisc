#!/usr/bin/python
# coding: UTF-8

from google import search
from BeautifulSoup import BeautifulSoup
import urllib
import webbrowser
import sys
from jinja2 import Environment, FileSystemLoader
import shutil
from datetime import datetime as dt
    
DEBUG = False

shop_list=[
{'shopname':u'mp3va', 		'shopurl':u'http://www.mp3va.com/'},
{'shopname':u'Beatport', 	'shopurl':u'https://www.beatport.com/'},
{'shopname':u'Wasabeat',	'shopurl':u'https://www.wasabeat.jp/'},
{'shopname':u'Amazon',		'shopurl':u'http://www.amazon.co.jp/MP3-%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-%E9%9F%B3%E6%A5%BD%E9%85%8D%E4%BF%A1-DRM%E3%83%95%E3%83%AA%E3%83%BC/b/ref=sd_allcat_mp3_str?ie=UTF8&node=2128134051'},
{'shopname':u'Juno',		'shopurl':u'http://www.junodownload.com/'},
{'shopname':u'Hardwax','shopurl':u'https://hardwax.com/'},
{'shopname':u'JetSet',		'shopurl':u'http://www.jetsetrecords.net/'},
{'shopname':u'ユニオン','shopurl':u'http://diskunion.net/'}
]


class Shop:
	def __init__(self, name, url, keyword):
		self.name=name
		self.url=url
		self.disk=[]
		self.createDiskList()

	def getShopName(self):
		return self.name

	def getShopUrl(self):
		return self.url

	def getShopDiskList(self):
		return self.disk

	def createDiskList(self):
		# use below method to search with google
		# https://breakingcode.wordpress.com/2010/06/29/google-search-python/
		for url in search(keyword + ' site:' + self.url, stop=5):
			soup = BeautifulSoup(urllib.urlopen(url))
			#print soup.prettify()
			try:
				title = soup.find('title').text
			except AttributeError:
				print 'AttributeError:'
				#print 'AttributeError:'.format(e.errno, e.strerror)
				title = u'hogehoge'
			except:
				print 'Unexpected error', sys.exc_info()[0]
				title = u'hogehoge'
			else:
				self.disk.append(Disk(title,url))
				print title
			
class Disk:
	def __init__(self,name,url):
		self.name=name
		self.url=url

	def getDiskTitle(self):
		return self.name

	def getDiskUrl(self):
		return self.url


def connect_jinja(shop_class_list, keyword):
	env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
	tmpl = env.get_template('jinja.tmpl')
	title = u" Search result of " + keyword

	sample_list = []
	for shop_class in shop_class_list:
		sample_list.append({'shopname':shop_class.getShopName(), 'shopurl':shop_class.getShopUrl()})
		disk_class_list = shop_class.getShopDiskList()
		for disk_class in disk_class_list:
			sample_list.append({'name':disk_class.getDiskTitle(), 'url':disk_class.getDiskUrl()})

	tdatetime = dt.now()
	tstr = tdatetime.strftime('%Y%m%d%H%M')

	html = tmpl.render({'title':title, 'disk_list':sample_list})
	f = open(keyword+'_'+tstr+'.html', 'w')
	f.write(html.encode('utf-8'))
	f.close()


if __name__ == "__main__":

	if DEBUG:
		print 'DEBUG==true'
		keyword = "kassem mosse workshop 12"
	else:
		print "input keyword..."
		keyword = raw_input()

	shop_class_list=[]

	for a in shop_list:
		shop_class_list.append(Shop(a['shopname'], a['shopurl'],keyword))
	
	connect_jinja(shop_class_list, keyword)

	print "Finish!!"

	#shutil.copy('./test.html', '/Library/WebServer/Documents/sd.html')
	#webbrowser.open('http://localhost/sd.html')

