#!/usr/bin/python3

# MIT License
# 
# Copyright (c) 2021 gh0$t
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

############################################################################################################################
# imports
############################################################################################################################

import sys
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request
from selenium import webdriver
import os
import time
from stem import Signal
from stem.control import Controller

############################################################################################################################
# Pass URL, extract text, translate
############################################################################################################################

URL = str(sys.argv[1])

GTURL = 'https://translate.google.com/'

# this is important, drives the whole translation process.
# if google updates the translate.google.com page selectors, this HORRIBLE selector needs to be updated
GTXpathSel = '//*[@id="yDmH0d"]/c-wiz/div/div[@class="WFnNle"]/c-wiz/div[@class="OlSOob"]/c-wiz/div[@class="hRFt4b"]/c-wiz/div[@class="ykTHSe"]/div/div[@class="dykxn MeCBDd j33Gae"]/div/div[2]/div/div[@class="Llmcnf"]'

print('\nConnecting to ' + URL + ' ...' + '\nExtracting text...')
req = Request(URL)
html = BeautifulSoup(urllib.request.urlopen(req).read(), 'html.parser')
text = html.find('div', {'id': 'bodyContent'}).get_text()

with open('out/English.txt', 'w', encoding='utf-8') as f:
	f.write(text)
	print('\nExtracted -> out/English.txt')

print('\nStarting translation job...')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='driver/chromedriver', options=options)

print('\nConnecting to ' + GTURL + ' ...')

driver.get(GTURL)
time.sleep(1)

try:

	# accept Google's cookies
	driver.find_elements_by_xpath ('//span[contains(text(), "I agree")]')[0].click()

except:

	pass

time.sleep(2)
driver.find_element_by_xpath('//*[@aria-label="Document translation"]').click()
driver.find_element_by_name('file').send_keys(os.path.abspath('out/English.txt'))

langEle = driver.find_elements_by_xpath(GTXpathSel)

i = 0

def init(driver):

	try:

		# elements are stale, need to refresh the list
		langEle = driver.find_elements_by_xpath(GTXpathSel)

		lang = langEle[i]
		langTxt = lang.get_attribute('innerHTML')
		
		if langTxt != 'English':
			
			# printing this to make you feel less giddy if you end up staring at your terminal at a stretch
			print('\nTrying English to ' + langTxt + '...')

			driver.find_elements_by_xpath('//button[@aria-label="More target languages"]')[1].click()
			time.sleep(2)

			# translate.google.com DOM structure SUCKS.
			# sorry Google, but that's the truth.
			# #$!@ -> i am swearing, that's Google's representation of their 'swearing emote'
			try:

				driver.find_elements_by_xpath('//div[@data-language-code="' + lang.find_element_by_xpath('..').get_attribute('data-language-code') + '"]')[3].click()

			except:

				driver.find_elements_by_xpath('//div[@data-language-code="' + lang.find_element_by_xpath('..').get_attribute('data-language-code') + '"]')[1].click()

			driver.find_elements_by_xpath ('//span[contains(text(), "Translate")]')[3].click()
			time.sleep(1)
			translatedBlog = driver.find_element_by_xpath('//pre').text
			with open('out/' + langTxt + '.txt', 'w', encoding='utf-8') as f:
				f.write(translatedBlog)
			print('\n' + str(i + 1) + '/' + str(totLang) + ' -> ' + langTxt + ' -> Done -> out/' + langTxt + '.txt')

			driver.back()

		else:

			print('\nSkipping ' + str(i + 1) + '/' + str(totLang) + ' -> ' + langTxt + '...')

	except Exception as e:

		# for debugging. use it @ your own risk. i am tired of the terminal screaming @ my face.
		# print('\n---------->', e)

		# Strategy to bypass Google's spam filter: quit chrome, switch TOR ID, re-try translation job
		driver.quit()

		with Controller.from_port(port = 9051) as controller:

			controller.authenticate()
			controller.signal(Signal.NEWNYM)

		# it's an overkill to print this. just let it do it's job silently.
		# print('\n----------> Switching TOR ID & re-trying ' + str(i + 1) + '/' + str(totLang) + '...')

		options = webdriver.ChromeOptions()
		options.add_argument('--incognito')
		options.add_argument('--headless')
		driver = webdriver.Chrome(executable_path='driver/chromedriver', options=options)
		driver.get(GTURL)
		time.sleep(1)

		try:

			# accept Google's cookies
			driver.find_elements_by_xpath ('//span[contains(text(), "I agree")]')[0].click()

		except:

				pass

		time.sleep(2)
		driver.find_element_by_xpath('//*[@aria-label="Document translation"]').click()
		driver.find_element_by_name('file').send_keys(os.path.abspath('out/English.txt'))

		init(driver)

totLang = len(langEle)
print('\nTotal languages = ' + str(totLang) + ' [press CTRL + C once or twice or thrice or any number of times you like to press to quit anytime]')
print('\nTranslating text...')

while i < totLang:

	init(driver)

	i += 1

print('\nTranslations completed. Check "/out" for the files.')

driver.quit()
exit()
