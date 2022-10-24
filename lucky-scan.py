import asyncio
from re import A, X
from urllib.error import URLError
import requests
import threading
from colorama import Fore, Back, Style
import sys
from time import sleep
from threading import Timer
import time

print(
        Fore.RED +
         """


          \\\|///     
        \\  - -  //   
         (  \033[42m@\033[49m \033[42m@\033[49m  )    
  -----oOOo-(_)-oOOo-------------
 |                               |
 |   \033[1mWe are ANONYMOUS\033[0m            |
 |   \033[42mlu3ky13-SCANNER\033[0m             |
 |   \033[43mCodded by trhacknon\033[0m         |
 |                               |
  -------------------------------




 [\033[44m\033[34mhttps://github.com/trhacknon/lu3ky13-SCANNER\033[0m ]

        """ + Fore.RESET)
time.sleep(0.5)
print()
print()


x=input(Fore.GREEN +'Enter your url:-')
r = requests.get('http://web.archive.org/cdx/search/cdx?url=*.{}&output=text&fl=original&collapse=urlkey'.format(x))
with open('url.txt', 'a') as f:
    f.write('\n')
    f.writelines(str(r.text))
    f.write('\n')

file = open('url.txt','r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'-- XSS Found   -->','   ' , f"{url}" + Fore.RESET)
           with open('Output.txt', 'a') as f:
            f.write('\n')
            f.writelines(url)
            f.write('\n')
        else :
            print(Fore.RED+'XSS NOT Found: '+url)
        
    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
