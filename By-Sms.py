#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s

import os

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet Byh4cker-Sms")

banner = """
         	          
___  _   _ _  _ ____ _  _ ____ ____ 
|__]  \_/  |__| |    |_/  |___ |__/ 
|__]   |   |  | |___ | \_ |___ |  \ 
                                    
          >>>>> Coder By H4cker <<<<<<

|> Instagram = byh4cker
|> YouTube = By H4cker
|> Telefon = +1 (819) 800-8547

"""

print(banner)

sor = input("Telefon Numarası Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın gönderilebilecek kısmı aşağıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız gönderilsin mi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptınız.")
