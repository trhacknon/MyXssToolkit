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


<h1> <g-emoji class="g-emoji" alias="card_file_box" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f5c3.png">🗃️</g-emoji> <a href="https://youtu.be/" rel="nofollow"><img src="" alt="YouTube" data-canonical-src="https://youtu.be/FgkwKou9QqE" style="max-width: 100%;"></a> <g-emoji class="g-emoji" alias="card_file_box" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f5c3.png">🗃️</g-emoji> </h1>

###### 
![1](https://github.com/trhacknon/lucky-scan/raw/main/Screenshot_2022-10-24-04-33-34-627_com.termux.jpg)  ![3](https://github.com/trhacknon/lucky-scan/raw/main/Screenshot_2022-10-24-04-52-07-579_com.termux.jpg) ![2](https://github.com/trhacknon/lucky-scan/raw/main/Screenshot_2022-10-24-04-42-55-122_com.darknethaxor.hackbar.jpg) 

# XSSearch
##### _A Comprehensive Reflected XSS Scanner_
<p align="center">
  <img  width="350" src="Images/Banner.PNG" />
</p>

<p align="center">
<img src=https://img.shields.io/badge/Made%20with-Python-blue>
<img src=https://img.shields.io/badge/Python-3.7-green>
<img src=https://img.shields.io/badge/Version-1.0-yellowgreen>
<img src=https://img.shields.io/badge/OS-Linux-yellow> <br>
<img src=https://img.shields.io/badge/Framework-Selenium-brightgreen>
<img src=https://img.shields.io/badge/WebDriver-ChromeDriver-blue>
</p>
<p align="center">
    <h3 align="center"> XSSearch is a comprehensive reflected XSS tool with 3000+ Payloads for automating XSS attacks and validating XSS endpoints.  </h3>
</p>

***
>#### DISCLAIMER :

The XSSearch developer will not be held liable if the tool is used with harmful or criminal intent. Please use at your own risk. :)

**** 
>#### USES :
- XSSearch can be used to discover reflected Cross Site Scripting (XSS) vulnerabilities 
- XSSearch is capable of validating XSS payloads.
- XSSearch will facilitate in the automation of brute - force attack for the verification of reflected XSS.
- Works on all Linux environment
- This can also be used in penetration testing to evaluate sanitization strength.
***
>#### FEATURES :
- Contains more than 3000 payloads for XSS validation
- Works on selenium framework & ChromeDriver
- It is faster than other XSS tools since the code is very light and rapid.
- The code and payloads can be modified according to the situation. 
***
>#### SETUP & INSTALLATION
XSSearch requires Selenium, ChromeDriver and Python to work smoothly on your system.

**Installing Selenium**
```
$ sudo apt update
$ pip3 install selenium
```
**Installing Chrome Browser for Linux (Skip this if you already have Chrome browser on your Linux)**
````
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo apt install ./google-chrome-stable_current_amd64.deb
````
**You may use the command to start Chrome from your terminal.**
```
$ google-chrome --no-sandbox
```
**Downloading ChromeDriver**

Go to https://chromedriver.chromium.org/downloads and get the linux 64 zipped version of ChromeDriver 80.0.3987.106.

Unzip the zip file. There will be a file for ChromeDriver. Open terminal on the same location and use the following command.
````
$ sudo chmod +x chromedriver
$ sudo mv -f chromedriver /usr/bin/chromedriver
````
***
>#### USAGE
XSSearch is a command line tool that uses a single command line instruction for simple and speedy execution.<br/>
**Note** : This tool will only work on url which has a input paramter in the url. Example : www[.]target[.]com/?xyz=
```
$ python3 xssearch.py -u url.com/?s={xss} -p payloads.txt
```
**Arguments :**<br/>
**-u** : It is required for URL input<br/>
**-p** : It is required for Payload file input<br/>
**{xss}** : It is a placeholder that the user should append after an equal to sign (=) in the url argument.

**Live Usage**
````
$ python3 xssearch.py -u https://ac121f0e1eb31ae5c0c9473f00f400f7.web-security-academy.net/?search={xss} -p payloads.txt
````
<p align="center">
<img src=https://github.com/trhacknon/MyXssToolkit/raw/master/IMG_20221024_100750.jpg>
</p>

Above is the screenshot of the tool with live example.<br/>
_Valid XSS exploits are marked with red alerts.<br/>
Invalid XSS exploits are marked with blue alerts._

**Errors & Warnings**<br/>
The following are some errors that might arise as a result of an incomplete command, not specifying arguments or not specifying placeholders.<br/>

Use the below command to get help
````
$ python3 xssearch.py -h
````
<h2><strong>you can use this other tool for xss https://github.com/trhacknon/PwnXSS
