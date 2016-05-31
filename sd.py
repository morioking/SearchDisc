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
'http://www.mp3va.com/',
'https://www.beatport.com/',
'https://www.wasabeat.jp/',
'http://www.amazon.co.jp/MP3-%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-%E9%9F%B3%E6%A5%BD%E9%85%8D%E4%BF%A1-DRM%E3%83%95%E3%83%AA%E3%83%BC/b/ref=sd_allcat_mp3_str?ie=UTF8&node=2128134051',
'http://www.junodownload.com/',
'https://hardwax.com/',
'http://www.jetsetrecords.net/',
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


def create_html(obj):
	env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
	tmpl = env.get_template('test.tmpl')
	html = tmpl.render(shop=obj)
	f = open('test.html', 'w')
	f.write(html)
	f.close()
	shutil.copy('./test.html', '/Library/WebServer/Documents/sd.html')
	webbrowser.open('http://localhost/sd.html')


if __name__ == "__main__":
	print "input words..."
	input_line1 = raw_input()
	#input_line1 = 'kassem mosse workshop 12'

	pack=[]
	for shop_url in shop_list:
		pack.append(Shop(shop_url))

	f = open('test.html', 'w')
	f.write("<html>")
	f.write("<body>")

	for shop_class in pack:
		html = u"<p><A Href="+shop_class.getUrl()+">"+shop_class.getName()+"</A></p>"
		f.write(html)
		for disk in shop_class.getDisk():
			# print disk.getDiskUrl()
			# print disk.getDiskTitle()
			# pass
			html = u"<p><A Href="+disk.getDiskUrl()+">"+disk.getDiskTitle()+"</A></p>"
			f.write(html.encode('utf-8'))

	f.write("</body>")
	f.write("</html>")
	f.close()
	shutil.copy('./test.html', '/Library/WebServer/Documents/sd.html')
	webbrowser.open('http://localhost/sd.html')

	#create_html(a)

