#!/usr/bin/python
# coding: UTF-8

from google import search
from BeautifulSoup import BeautifulSoup
import urllib
import webbrowser
import sys
from jinja2 import Environment, FileSystemLoader
import shutil
    
DEBUG = True

shop_list=[
#'shopname':u'mp3va', 		'shopurl':u'http://www.mp3va.com/',
#'shopname':u'Beatport', 	'shopurl':u'https://www.beatport.com/',
#'shopname':u'Wasabeat',	'shopurl':u'https://www.wasabeat.jp/',
#'shopname':u'Amazon',		'shopurl':u'http://www.amazon.co.jp/MP3-%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-%E9%9F%B3%E6%A5%BD%E9%85%8D%E4%BF%A1-DRM%E3%83%95%E3%83%AA%E3%83%BC/b/ref=sd_allcat_mp3_str?ie=UTF8&node=2128134051',
#'shopname':u'Juno',		'shopurl':u'http://www.junodownload.com/',
{'shopname':u'Hardwax','shopurl':u'https://hardwax.com/'},
#'shopname':u'JetSet',		'shopurl':u'http://www.jetsetrecords.net/',
{'shopname':u'ユニオン','shopurl':u'http://diskunion.net/'}
]


urls=[]
titles=[]


class Shop:
	def __init__(self, name, url):
		self.name=name
		self.url=url
		self.disk=[]
		#self.createDiskList()
		self.createDiskList4Test()

	def getShopName(self):
		return self.name

	def getShopUrl(self):
		return self.url

	def getShopDiskList(self):
		return self.disk

	def createDiskList(self):
		for url in search(input_line1 + ' site:' + self.url, stop=5):
			soup = BeautifulSoup(urllib.urlopen(url))
			title = soup.find('title').text
			self.disk.append(Disk(title,url))

	def createDiskList4Test(self):
		if self.url=="https://hardwax.com/":
			self.disk.append(Disk(u"Kassem Mosse: Workshop 12 - Hard Wax","https://hardwax.com/62572/kassem-mosse/workshop-12/"))
			self.disk.append(Disk(u"Kassem Mosse: Workshop 08 - Hard Wax","https://hardwax.com/58639/kassem-mosse/workshop-08"))
		elif self.url=="http://diskunion.net/":
			self.disk.append(Disk(u"KASSEM MOSSE / Workshop 12 | diskunion.net PROGRESSIVE ROCK ONLINE SHOP","http://diskunion.net/progre/ct/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"))
			self.disk.append(Disk(u"Workshop 12 - KASSEM MOSSE - 12&quot;(レコード) | CLUB/DANCE | ディスクユニオン･オンラインショップ","http://diskunion.net/sp/punk/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"))
			
class Disk:
	def __init__(self,name,url):
		self.name=name
		self.url=url

	def getDiskTitle(self):
		return self.name

	def getDiskUrl(self):
		return self.url


def create_html():
	env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
	tmpl = env.get_template('jinja.tmpl')
	title = u"sd.py result"

	sample_list = []
	sample_list.append({'shopname':u"Hard Wax", 'shopurl':u"https://hardwax.com/"})
	sample_list.append({'name':u"Kassem Mosse: Workshop 12 - Hard Wax", 'url':u"https://hardwax.com/62572/kassem-mosse/workshop-12/"})
	sample_list.append({'name':u"Kassem Mosse: Workshop 08 - Hard Wax", 'url':u"https://hardwax.com/58639/kassem-mosse/workshop-08"})
	sample_list.append({'name':u"Kassem Mosse: Workshop 03 - Hard Wax", 'url':u"https://hardwax.com/54697/kassem-mosse/workshop-03/"})
	sample_list.append({'shopname':u"disk union", 'shopurl':u"http://diskunion.net/"})
	sample_list.append({'name':u"KASSEM MOSSE / Workshop 12 | diskunion.net PROGRESSIVE ROCK ONLINE SHOP", 'url':u"http://diskunion.net/progre/ct/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"})
	sample_list.append({'name':u"Workshop 12 - KASSEM MOSSE - 12&quot;(レコード) | CLUB/DANCE | ディスクユニオン･オンラインショップ", 'url':u"http://diskunion.net/sp/punk/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"})
	html = tmpl.render({'title':title, 'disk_list':sample_list})
	f = open('jinja.html', 'w')
	f.write(html.encode('utf-8'))
	f.close()

def connect_jinja(c):
	# env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
	# tmpl = env.get_template('jinja.tmpl')
	# title = u"sd.py result"

	for shop_class in c:
		print shop_class.getShopName()
		print shop_class.getShopUrl()
		disk_class_list = shop_class.getShopDiskList()
		for disk_class in disk_class_list:
			print disk_class.getDiskTitle()
			print disk_class.getDiskUrl()
	
	# sample_list = []
	# sample_list.append({'shopname':u"Hard Wax", 'shopurl':u"https://hardwax.com/"})
	# sample_list.append({'name':u"Kassem Mosse: Workshop 12 - Hard Wax", 'url':u"https://hardwax.com/62572/kassem-mosse/workshop-12/"})
	# sample_list.append({'name':u"Kassem Mosse: Workshop 08 - Hard Wax", 'url':u"https://hardwax.com/58639/kassem-mosse/workshop-08"})
	# sample_list.append({'name':u"Kassem Mosse: Workshop 03 - Hard Wax", 'url':u"https://hardwax.com/54697/kassem-mosse/workshop-03/"})
	# sample_list.append({'shopname':u"disk union", 'shopurl':u"http://diskunion.net/"})
	# sample_list.append({'name':u"KASSEM MOSSE / Workshop 12 | diskunion.net PROGRESSIVE ROCK ONLINE SHOP", 'url':u"http://diskunion.net/progre/ct/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"})
	# sample_list.append({'name':u"Workshop 12 - KASSEM MOSSE - 12&quot;(レコード) | CLUB/DANCE | ディスクユニオン･オンラインショップ", 'url':u"http://diskunion.net/sp/punk/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"})
	# html = tmpl.render({'title':title, 'disk_list':sample_list})
	# f = open('jinja.html', 'w')
	# f.write(html.encode('utf-8'))
	# f.close()


if __name__ == "__main__":

	shop_class_list=[]
		
	if DEBUG:
		print 'DEBUG==true'
		HardWax = Shop("HardWax", "https://hardwax.com/")
		DiskUnion = Shop("DiskUnion", "http://diskunion.net/")
		shop_class_list.append(HardWax)
		shop_class_list.append(DiskUnion)
	else:
		input_line1 = raw_input()
		print 'DEBUG==false'
		
	#connect_jinja(shop_class_list)


	for a in shop_list:
		print a['shopname'], a['shopurl']
	
	
	#create_html()

	# for shop_url in shop_list:
		# shop_class_list.append(Shop(shop_url))

	# f = open('test.html', 'w')
	# f.write("<html>")
	# f.write("<body>")

	# for shop_class in shop_class_list:
		# html = u"<p><A Href="+shop_class.getShopUrl()+">"+shop_class.getShopName()+"</A></p>"
		# f.write(html)
		# for disk in shop_class.getShopDiskList():
			# html = u"<p><A Href="+disk.getDiskUrl()+">"+disk.getDiskTitle()+"</A></p>"
			# f.write(html.encode('utf-8'))

	# f.write("</body>")
	# f.write("</html>")
	# f.close()
	
	# create_html()

	#shutil.copy('./test.html', '/Library/WebServer/Documents/sd.html')
	#webbrowser.open('http://localhost/sd.html')

