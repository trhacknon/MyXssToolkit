# FindXSS

###Compatibility:

Windows , Linux or any device running python 2.7
###Requirements:

Python 2.7

Wordlist included(wordlist.txt)

Modules required: Colorama, Mechanize

###Modules Required:

Colorama: https://pypi.python.org/pypi/colorama/

Mechanize: https://pypi.python.org/pypi/mechanize/

###Description: BruteXSS is a very powerful and fast Cross-Site Scripting Brutforcer which is used for bruteforcing a parameters. The BruteXSS injects multiple payloads loaded from a specified wordlist and fires them at the specified parameters and scans if any of the parameter is vulnerable to XSS vulnerability. BruteXSS is very accurate at doing its task and there is no chance of false positive as the scanning is much powerful. BruteXSS supports POST and GET requests which makes it compatible with the modern web applications.

###Features:

XSS Bruteforcing

XSS Scanning

Supports GET/POST requests

Custom wordlist can be included

User-friendly UI

###Usage(GET Method):

COMMAND:  python2 FindXSS.py
METHOD:   g
URL:      http://www.site.com/?parameter=value
WORDLIST: wordlist.txt
###Usage(POST method):

COMMAND:   python2 FindXSS.py
METHOD:    p
URL:       http://www.site.com/file.php
POST DATA: parameter=value&parameter1=value1
WORDLIST:  wordlist.txt


# lucky-scan      🐛 🐛 
   
######  <g-emoji class="g-emoji" alias="cd" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4bf.png">💿</g-emoji> I created this tool to find xss on a big website sometimes we use archive.org  to find links we see have thousand of links we use these tools to easily find xss the tools by sending a request to all links in archive.org and changing all parameters (=) to your payload  <g-emoji class="g-emoji" alias="cd" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4bf.png">💿</g-emoji>

<h1><g-emoji class="g-emoji" alias="ledger" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d2.png">📒</g-emoji> How it work <g-emoji class="g-emoji" alias="ledger" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d2.png">📒</g-emoji> </h1>



- download file python (you need python3) ( python3 lucky-scan.py) <br>
- modify  txt files like (payloads.txt) add payload in a text <br>
- run tools  python3 lucky-scan.py <br>
