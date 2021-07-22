# translator
A one shot English to Multi-Lang bulk Python 3 web crawler-translator powered by Google Translate for WHONIX.  
It bypasses Google's anti spam filter through switching TOR circuits.  

Crawls through specified 'English' website provided as an URL input parameter from console/terminal  
-> extracts texts inside **out/English.txt**  
-> opens Chrome  
-> navigates to https://translate.google.com  
-> uploads **out/English.txt**, and  
-> brute forces translation into all available languages  
-> saving those translated texts into respective **.txt** files inside **out**.
# Definition of 'Brute force' according to the author w.r.t. this tool
Google restricts requests after sometime, giving **4XX** error.  
The tool  
-> closes Chrome  
-> changes TOR circuit  
-> reopens Chrome  
-> navigates to https://translate.google.com, and  
-> retries the translation process from where it had left off.
# Requirements
(1) WHONIX Operating System (modify the code at your will to support other Operating Systems)  
(2) Python 3  
(3) Chrome  
(4) Selenium
# What's included
(1) translator.py  
(2) chromedriver for selenium (you can replace this with your own version)
# Usage
(1) Install urllib, bs4, selenium.  
(2) Change the DOM selectors inside the tool @ Line number 48, based on your need.  
These selectors represents the element inside the Website from where the text is to be extracted.  
Syntax examples: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
```python
blog = html.find('div', {'id': 'bodyContent'}).get_text()
```
(3) Run the following command.
```python
python3 translator.py https://en.wikipedia.org/wiki/Google_Translate
```
Replace the above Website URL with yours from where you want to extract the text.
# Note
Please raise PRs for improving this tool.
