#python 3.7.1
print("BYH4CKER SMS GÖNDERME TOOL 2020 
INSTAGRAM = byh4cker") 
import requests

while True:
  number = input("Sms atacağınız kişinin numarasını bunla birlikte yazın '+':")
  message = input('Atacağınız mesajınız: ')

  print(f'Receiver : {number}\nYour Message: {message}')

  print("Devam etmek için (1)\n Fikrinizi Değiştirmek için (2)")
  edit=int(input())
  
  if edit==1:
    resp = requests.post('https://textbelt.com/text', {
    'phone': number,
    'message': message,
    'key': 'textbelt',
    })
    response = resp.json()
    if response['success'] == False:
       print('ERROR : ',response['error'])

    elif response['success'] == True:
       print('DONE! Your Message ID is:',response['textId'])
    break
  elif edit==2:
    continue
  else:
     print("Wrong Command!\nBe sure you to check the message info for security")
  continue
  
