#!/usr/bin/python
# -*- coding: utf-8 -*-

path = 'ikkiyomi.txt'
bango = 0
hantei = 0
tugip = 1

with open(path, mode = 'w') as f:
	f.write(' ')

import os
import requests
from bs4 import BeautifulSoup

print('企画URLを入力')

kikaku = input('>> ')

#きかくいちらん
r = requests.get(kikaku)

while hantei != tugip:
	
	soup = BeautifulSoup(r.text, 'html.parser')
	
	titles = soup.select('.widget-workCard-titleLabel') 
	
	kname = soup.select('#userEvent-title')
	
	print(kname[0].get_text())

	for title in titles:
			#さんかさくひん
			rr = requests.get('https://kakuyomu.jp'+title.get('href'))
		
			soupp = BeautifulSoup(rr.text, 'html.parser')
	
			titlesp = soupp.select('.widget-toc-episode a')
		
			bango = bango + 1
		
			print(bango)
		
			for titlep in titlesp:
				#おはなし
				rrr = requests.get('https://kakuyomu.jp'+titlep.get('href'))
				souppp = BeautifulSoup(rrr.text, 'html.parser')
				titlespp = souppp.select('#contentMain-inner') 

				for titlepp in titlespp:
	
						honbun = titlepp.get_text()

						with open(path, mode ='a') as f:
							f.write(honbun)
						
	else:
		hantei = tugip
	
		tugi = soup.select('.widget-pagerNext a')
	
		for tugip in tugi:
			
			r = requests.get('https://kakuyomu.jp'+tugip.get('href'))

path2 = kname[0].get_text() + '.txt'

os.rename(path, path2)

print('おしまい')
