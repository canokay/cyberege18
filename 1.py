"""
Project: portTaraması
Pyton Version: Python 2.7.14
Author: canokay
"""

import socket
soket= socket.socket()
host="192.168.43.161"
linuxNetwork=["22"]
windows=["135","136","137","138","139"]
dosya=open("IPler.txt","r")
IPler=dosya.read()
dosya.close()
for IP in IPler.split("\n"):
    for i in range(1,82,1):
        try:
            soket.connect((IP,i))
            banner=soket.recv(1024)
            print "[+]Port acik:",str(i),":",banner
            soket.close()
            if str(i) in linuxNetwork:
                print "[+]Linux veya network cihazi olabilir"
                dosya=open("linux.txt","a")

                IP=str(host)+"\n"
                dosya.write(IP)
                dosya.close()
            elif str(i) in windows:
                print "[+]Windows cihaz olabilir"
            if "OpenSSH" in banner:
                dosya=open("openssh.txt","a")
                IP=str(host)+"\n"
                dosya.write(IP)
                dosya.close()
            #yeni  IP bulma
            dosya=open("yeni.txt","r")
            icerik=dosya.read()
            dosya.close()
            if not str(host) in icerik:
                print "Yeni IP bulundu."
                IP = str(host) + "\n"
                dosya=open("yeni.txt","a")
                dosya.write(IP)
                dosya.close()
                payload = {"api_key": "#apikey", "api_secret": "#apisecretkey", "to": "tokey",
                           "from": "ABY Bilgi Islem", "text": "yeni IP bulundu"}
                url = "https://rest.nexmo.com/sms/json"
                requests.post(url=url, data=payload, verify=False)
        except:
            pass
