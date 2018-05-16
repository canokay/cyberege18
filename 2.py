"""
Project: Bitcoin SMS
Pyton Version: Python 2.7.14
Author: canokay
"""

import  requests
url ="https://www.bitcturk.com/api/ticker"
print requests.get(url,verify=False).json()[0]['last']
cikti=  requests.get(url,verify=False).json()[0]['last']
if int(cikti)<40000:
    print "Fyat dustu"
    payload={"api_key":"4642e3","api_secret":"#apikey","to":"#tokey","from":"CO IT","text":"Bitcoin Fiyatlari dustu..."}
    url="https://rest.nexmo.com/sms/json"
    requests.post(url=url,data=payload,verify=False)
