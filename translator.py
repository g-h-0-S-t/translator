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
# Pass URL, extract blog, translate
############################################################################################################################

URL = str(sys.argv[1])

print('\nExtracting Blog...')
req = Request(URL)
html = BeautifulSoup(urllib.request.urlopen(req).read(), 'html.parser')
blog = html.find('div', {'id': 'bodyContent'}).get_text()
print('\nExtracted...')

print('\nTranslating Blog...')
with open('out/English.txt', "w", encoding="utf-8") as f:
	f.write(blog)

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='driver/chromedriver', options=options)
driver.get('https://translate.google.com/')
time.sleep(1)
try:
	driver.find_elements_by_xpath ('//span[contains(text(), "I agree")]')[0].click()
except:
	pass
time.sleep(2)
driver.find_element_by_xpath('//*[@aria-label="Document translation"]').click()
driver.find_element_by_name('file').send_keys(os.path.abspath('out/English.txt'))
langEle = driver.find_elements_by_xpath('//*[@class="Llmcnf"]')

i = 1

def init(driver):
	try:
		langEle = driver.find_elements_by_xpath('//*[@class="Llmcnf"]') # elements are stale, need to refresh the list
		lang = langEle[i]
		langTxt = lang.get_attribute('innerHTML')
		if langTxt != 'English':
			driver.find_elements_by_xpath('//button[@aria-label="More target languages"]')[1].click()
			time.sleep(2)
			driver.find_elements_by_xpath('//div[@data-language-code="' + lang.find_element_by_xpath('..').get_attribute('data-language-code') + '"]')[3].click()
			driver.find_elements_by_xpath ('//span[contains(text(), "Translate")]')[3].click()
			time.sleep(1)
			translatedBlog = driver.find_element_by_xpath('//pre').text
			with open('out/' + langTxt + '.txt', "w", encoding="utf-8") as f:
				f.write(translatedBlog)
			print('\n' + langTxt + ' -> Done' + '...')
			driver.back()
	except:
		driver.quit()

		with Controller.from_port(port = 9051) as controller:
			controller.authenticate()
			controller.signal(Signal.NEWNYM)


		options = webdriver.ChromeOptions()
		options.add_argument('--incognito')
		driver = webdriver.Chrome(executable_path='driver/chromedriver', options=options)
		driver.get('https://translate.google.com/')
		time.sleep(1)
		try:
			driver.find_elements_by_xpath ('//span[contains(text(), "I agree")]')[0].click()
		except:
			pass
		time.sleep(2)
		driver.find_element_by_xpath('//*[@aria-label="Document translation"]').click()
		driver.find_element_by_name('file').send_keys(os.path.abspath('out/English.txt'))

		init(driver)

while i < len(langEle):
	init(driver)
	i += 1

print('\nTranslations completed...')

driver.quit()
