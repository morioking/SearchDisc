#!/usr/bin/python
# coding: UTF-8

from google import search
from BeautifulSoup import BeautifulSoup
import urllib
import webbrowser
import sys
from jinja2 import Environment, FileSystemLoader
import shutil
    


shop_list=[
#'http://www.mp3va.com/',
#'https://www.beatport.com/',
#'https://www.wasabeat.jp/',
#'http://www.amazon.co.jp/MP3-%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-%E9%9F%B3%E6%A5%BD%E9%85%8D%E4%BF%A1-DRM%E3%83%95%E3%83%AA%E3%83%BC/b/ref=sd_allcat_mp3_str?ie=UTF8&node=2128134051',
#'http://www.junodownload.com/',
'https://hardwax.com/',
#'http://www.jetsetrecords.net/',
'http://diskunion.net/'
]


urls=[]
titles=[]


class Shop:
	def __init__(self, url):
		self.name=url
		self.url=url
		self.disk=[]
		self.serchDisk()

	def getName(self):
		return self.name

	def getUrl(self):
		return self.url

	def getDisk(self):
		return self.disk

	def serchDisk(self):
		for url in search(input_line1 + ' site:' + self.url, stop=5):
			soup = BeautifulSoup(urllib.urlopen(url))
			title = soup.find('title').text
			self.disk.append(Disk(title,url))

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
	sample_list.append({'name':u"Kassem Mosse: Workshop 12 - Hard Wax", 'url':u"Href=https://hardwax.com/62572/kassem-mosse/workshop-12/"})
	sample_list.append({'name':u"Kassem Mosse: Workshop 08 - Hard Wax", 'url':u"https://hardwax.com/58639/kassem-mosse/workshop-08"})
	sample_list.append({'name':u"Kassem Mosse: Workshop 03 - Hard Wax", 'url':u"https://hardwax.com/54697/kassem-mosse/workshop-03/"})
	sample_list.append({'shopname':u"disk union", 'shopurl':u"http://diskunion.net/"})
	sample_list.append({'name':u"KASSEM MOSSE / Workshop 12 | diskunion.net PROGRESSIVE ROCK ONLINE SHOP", 'url':u"Href=http://diskunion.net/progre/ct/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"})
	sample_list.append({'name':u"Workshop 12 - KASSEM MOSSE - 12&quot;(レコード) | CLUB/DANCE | ディスクユニオン･オンラインショップ", 'url':u"http://diskunion.net/sp/punk/detail/CM-0036556?utm_source=rmd&utm_medium=ad&utm_campaign=rmd"})
	html = tmpl.render({'title':title, 'disk_list':sample_list})
	f = open('jinja.html', 'w')
	f.write(html.encode('utf-8'))
	f.close()

if __name__ == "__main__":
	create_html()

	print "input words..."
	#input_line1 = raw_input()
	#input_line1 = 'kassem mosse workshop 12'

	# pack=[]
	# for shop_url in shop_list:
		# pack.append(Shop(shop_url))

	# f = open('test.html', 'w')
	# f.write("<html>")
	# f.write("<body>")

	# for shop_class in pack:
		# html = u"<p><A Href="+shop_class.getUrl()+">"+shop_class.getName()+"</A></p>"
		# f.write(html)
		# for disk in shop_class.getDisk():
			# html = u"<p><A Href="+disk.getDiskUrl()+">"+disk.getDiskTitle()+"</A></p>"
			# f.write(html.encode('utf-8'))

	# f.write("</body>")
	# f.write("</html>")
	# f.close()
	
	# create_html()

	#shutil.copy('./test.html', '/Library/WebServer/Documents/sd.html')
	#webbrowser.open('http://localhost/sd.html')

