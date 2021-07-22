# translator
One shot English to Multi-lang brute-force translator using Google Translate.  
Crawls through specified 'English' website provided as an URL input parameter from console/terminal, extracts texts inside **out/English.txt**, opens Chrome, navigates to https://translate.google.com, uploads **out/English.txt** and brute forces translation into all available languages, saving those translated texts into respective **.txt** files inside **out**.
# Definition of Brute force according to author w.r.t. this tool
Google restricts requests after sometime, giving **4XX** error.  The tool closes Chrome, changes TOR circuit, reopens Chrome, navigates to https://translate.google.com, and retries the translation process from where it had left off.
# Requirements
WHONIX Operating System, Python 3, Chrome, Selenium
# What's included
translator.py, chromedriver for selenium
# Usage
Install urllib, bs4, selenium  
Run following command
```python
python3 translator.py https://[your website]
```
You can focus on a specific area of the web page that needs translation by changing the DOM selectors inside the tool @ Line number 48.
