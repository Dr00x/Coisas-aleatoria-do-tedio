from datetime import datetime
from os import system as st
from art import tprint
from time import sleep as sl

while True:
    now = datetime.now()
    st('cls')
    tprint(str(now.hour) +":"+  str(now.minute) +":"+ str(now.second))
    sl(0.1)

