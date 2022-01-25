from random import randint
from multiprocessing import Pool
import sys
import os
from twilio.rest import Client
import time


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


WELCOME = ('Welcome To DSURF-ISP Networking Services')
canadian_phone = ('+12262704800')
kod=(str(random_with_N_digits(6)))

print(WELCOME)

time.sleep(3)

name = input('Enter Your User-Name: ')
to_phone = input('Enter your phone number: ')

time.sleep(1)

print ('\n' 'Hello ' + name + '!!!')

time.sleep(1)

print ('\n' 'your phone number is: ' + to_phone )

time.sleep(3)

print('\n' 'A code will be sent to you right away!!!')


#AC0c8a52d1aef8a52a60d63e93ce677e5b
#3716f3b82169b30697767d5299614494

account_sid=os.environ['TWILIO_ACCOUNT_SID']='AC0c8a52d1aef8a52a60d63e93ce677e5b'
auth_token=os.environ['TWILIO_AUTH_TOKEN']='3716f3b82169b30697767d5299614494'
client = Client(account_sid, auth_token)

from_whatsapp_number= canadian_phone
to_whatsapp_number= to_phone

client.messages.create(body='Hej på dig! ,' + name + '\n' 'Ditt kod är ' + kod + '\n' 'Mvh' '\n' 'DSURF-ISP',
		       from_=from_whatsapp_number,
		       to=to_whatsapp_number)
print('Code Sent, Check your inbox')
time.sleep(3)

code = input('Type in your code: ')

while True:
    if code == kod:
        print('Welcome ' + name)
        break
    else:
        print('Code Error, Please Try Again !!')
        code = input('Type in your code: ')
        
   
time.sleep(3)
    
    
print("DSURF-ISP \n SEE YOU NEXT TIME "+name+'.')

time.sleep(6)
