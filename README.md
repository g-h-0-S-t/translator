# translator
A one shot English to Multi-Lang bulk Python 3 web crawler-translator powered by Google Translate for WHONIX.  
It bypasses Google's anti spam filter through switching TOR circuits.  

Crawls through specified 'English' website provided as an URL input parameter from console/terminal  
-> extracts texts inside **out/English.txt**  
-> opens Chrome (v1 -> normal, v2 -> headless)  
-> navigates to https://translate.google.com  
-> uploads **out/English.txt**, and  
-> brute forces translation into all available languages  
-> saving those translated texts into respective **.txt** files inside **out**.
# Definition of 'Brute force' according to the author w.r.t. this tool
Google restricts requests after sometime, giving **4XX** error.  

The tool  
-> closes Chrome (v1 -> normal, v2 -> headless)  
-> changes TOR circuit  
-> reopens Chrome (v1 -> normal, v2 -> headless)  
-> navigates to https://translate.google.com, and  
-> retries the translation process from where it had left off.
# Requirements
(1) WHONIX Operating System (modify the code at your will to support other Operating Systems)  
(2) Python 3  
(3) Chrome  
(4) Selenium
# What's included
(1) translator.py (Use this for simple Terminal output. The selectors are screwed up in this version which is fixed in v2. Feel free to modify this to suit your purpose. It's a toy / tool / means afterall, this and all other future versions.)
(2) translator-v2.py (Super detailed code and Terminal output.)
(2) chromedriver for selenium (you can replace this with your own version)
# Usage
(1) Install urllib, bs4, selenium.  
(2) Change the DOM selectors inside the tool @ Line number 48(v1)/54(v2), based on your need.  
These selectors represents the element inside the Website from where the text is to be extracted.  
Syntax examples: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
```python
blog = html.find('div', {'id': 'bodyContent'}).get_text()
```
(3) Run the following command for:  
**v1**
```python
python3 translator.py https://en.wikipedia.org/wiki/Nuclear_fission
```
**v2**
```python
python3 translator-v2.py https://en.wikipedia.org/wiki/Nuclear_fission
```
Replace the above Website URL with yours from where you want to extract the text.  
**Output of v2**
```python
Connecting to https://en.wikipedia.org/wiki/Nuclear_fission ...
Extracting text...

Extracted -> out/English.txt

Starting translation job...

Connecting to https://translate.google.com/ ...

Total languages = 109 [press CTRL + C once or twice or thrice or any number of times you like to press to quit anytime]

Translating text...

Trying English to Afrikaans...

Trying English to Afrikaans...

1/109 -> Afrikaans -> Done -> out/Afrikaans.txt

Trying English to Albanian...

Trying English to Albanian...

2/109 -> Albanian -> Done -> out/Albanian.txt

Trying English to Amharic...

3/109 -> Amharic -> Done -> out/Amharic.txt

Trying English to Arabic...

Trying English to Arabic...

4/109 -> Arabic -> Done -> out/Arabic.txt

Trying English to Armenian...

5/109 -> Armenian -> Done -> out/Armenian.txt

Trying English to Azerbaijani...

6/109 -> Azerbaijani -> Done -> out/Azerbaijani.txt

Trying English to Basque...

7/109 -> Basque -> Done -> out/Basque.txt

Trying English to Belarusian...

8/109 -> Belarusian -> Done -> out/Belarusian.txt

Trying English to Bengali...

9/109 -> Bengali -> Done -> out/Bengali.txt

Trying English to Bosnian...

10/109 -> Bosnian -> Done -> out/Bosnian.txt

Trying English to Bulgarian...

11/109 -> Bulgarian -> Done -> out/Bulgarian.txt

Trying English to Catalan...

Trying English to Catalan...

Trying English to Catalan...

12/109 -> Catalan -> Done -> out/Catalan.txt

Trying English to Cebuano...

13/109 -> Cebuano -> Done -> out/Cebuano.txt

Trying English to Chichewa...

14/109 -> Chichewa -> Done -> out/Chichewa.txt

Trying English to Chinese (Simplified)...

15/109 -> Chinese (Simplified) -> Done -> out/Chinese (Simplified).txt

Trying English to Chinese (Traditional)...

16/109 -> Chinese (Traditional) -> Done -> out/Chinese (Traditional).txt

.
.
.
.
.
.
.
.
.
.
.
.
```
# Note
Please raise PRs for improving this tool.
