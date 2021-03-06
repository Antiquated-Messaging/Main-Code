from cipher.py import cipher
from saver.py import saver
from translate.py import Numcode
from morse.py import morse

print('What type of message would you like to send?')
print('Morse Code')
print('Cipher')
print('Numeric')
print('')
messageType=input().lower()
while messageType!='cipher' and messageType!='morse code' and messageType!='numeric':
    print('Sorry, I didn\'t get that, try again?')
    messageType=input().lower()
print('Please type your message here:')
message=input()
print('For whom is this message?')
location=input()
print('And finally, what\'s your name?')
sender=input()
if messageType=='cipher':
          export=cipher(message)
if messageType=='numeric':
          export=Numcode(message, location)
if messageType=='morse code':
          export=morse(message)
finish=saver(export.translation, sender, location)