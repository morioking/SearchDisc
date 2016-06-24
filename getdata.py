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
    

if __name__ == "__main__":

	f = open('Beatport_test.dat', 'r')
	data = f.read()
	f.close()
	soup = BeautifulSoup(data)
	title = soup.find('title').tex
	print title
	
	# for Beatport
	divSoap = soup.findAll("button")
	print divSoap[0].renderContents()
	# for div in divSoap:
		# #print div['class']
		# if div['class'] == "add-to-default":
			# print div.renderContents()
			# break
		