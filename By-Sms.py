#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s
import colorama
from colorama import Fore, Back, Style

import os

os.system("apt-get install figlet")

os.system("clear")

banner = """       
_   ___       __   ____     __          
  / _ )__ __/ /  / / /____/ /_____ ____
 / _  / // / _ \/_  _/ __/  '_/ -_) __/
/____/\_, /_//_/ /_/ \__/_/\_\\__/_/
     /___/     
>>>>> Coder By H4cker <<<<<<

|> Instagram = byh4cker
|> YouTube = By H4cker
|> WebSite = https://www.byh4cker.com/
"""
print(Fore.GREEN)
print(banner)

sor = input("Telefon Numarası Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:100]

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
