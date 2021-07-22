# translator
One shot English to Multi-lang brute-force translator using Google Translate.  
Crawls through specified 'English' website, extracts texts inside **out/English.txt**, opens chrome, navigates to https://translate.google.com, uploads **out/English.txt** and brute forces translation into all available languages.
# Definition of Brute force according to author w.r.t. this tool
Google restricts requests after some time, giving **4XX** error.  The tool closes Chrome, changes TOR circuit, and retries the translation process from where it had left off.
# Requirements
WHONIX, Python 3, Chrome, Selenium
# What's included
translator.py, chromedriver for selenium
# Usage
Install urllib, bs4, selenium  
Run following command
```python
python3 yacTranslator.py https://[your website]
```
You can focus on a specific are of the web page that needs translation by changing the DOM selectors inside the tool @ Line number 48.
