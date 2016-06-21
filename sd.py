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
RESULTS = 3

shop_list=[
{'shopname':u'mp3va', 		'shopurl':u'http://www.mp3va.com/'},
{'shopname':u'Beatport', 	'shopurl':u'https://www.beatport.com/'},
{'shopname':u'Wasabeat',	'shopurl':u'https://www.wasabeat.jp/'},
{'shopname':u'Amazon',		'shopurl':u'https://www.amazon.co.jp/'},
{'shopname':u'Juno',		'shopurl':u'http://www.junodownload.com/'},
{'shopname':u'Hardwax',		'shopurl':u'https://hardwax.com/'},
{'shopname':u'Traxsource',	'shopurl':u'http://www.traxsource.com/'},
{'shopname':u'Bleep',		'shopurl':u'https://bleep.com/'},
{'shopname':u'trackitdown',		'shopurl':u'https://www.trackitdown.net/'},
{'shopname':u'whatpeopleplay',		'shopurl':u'https://www.whatpeopleplay.com/'}
# {'shopname':u'JetSet',		'shopurl':u'http://www.jetsetrecords.net/'},
# {'shopname':u'ユニオン','shopurl':u'http://diskunion.net/'},
# {'shopname':u'テクニーク','shopurl':u'http://www.technique.co.jp/'}
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
		print self.name
		# use below method to search with google
		# https://breakingcode.wordpress.com/2010/06/29/google-search-python/
		for url in search(keyword + ' site:' + self.url, num=RESULTS, start=0, stop=RESULTS):
			if url.find('.xml') == -1:
				print '  ',url
				soup = BeautifulSoup(urllib.urlopen(url))
				#print soup.prettify()
				try:
					title = soup.find('title').text
				except AttributeError:
					print 'AttributeError:'
				except:
					print 'Unexpected error', sys.exc_info()[0]
				else:
					self.disk.append(Disk(title,url))
					try:
						print '     > ',title
					except UnicodeEncodeError:
						print "UnicodeEncodeError", "TODO:need to replace illigal words to display terminal"
					else:
						pass
			else:
				pass

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
	f = open(tstr+'_'+keyword.replace('/', '')+'.html', 'w')
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


	tdatetime = dt.now()
	tstr = tdatetime.strftime('%Y/%m/%d-%H:%M')
	print tstr, 'start search...'
	
	for a in shop_list:
		shop_class_list.append(Shop(a['shopname'], a['shopurl'],keyword))
	
	connect_jinja(shop_class_list, keyword)

	tdatetime = dt.now()
	tstr = tdatetime.strftime('%Y/%m/%d-%H:%M')
	print tstr, "Finish!!"

	#shutil.copy('./test.html', '/Library/WebServer/Documents/sd.html')
	#webbrowser.open('http://localhost/sd.html')

