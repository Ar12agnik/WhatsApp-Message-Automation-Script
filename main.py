import pywhatkit as kit
import time
import pyautogui as pg

# List of WhatsApp numbers

numbers = []
with open("WhattsappNumbers.txt", "r") as fp:
    for line in fp:
        numbers.append(line.strip())  
        print(f"{line.strip()} added")



    


# Message to send
message = input("enter a message: ")
input("press enter to start")
a=len(numbers)
# Sending the message to each number
for number in numbers:
    kit.sendwhatmsg_instantly(f"+91{number}", message, 10)
    pg.press("enter")
    a=a-1
    print(a,"left ")
    time.sleep(20)  # Add delay to avoid spamming and to comply with WhatsApp's rate limits
    pg.hotkey('ctrl','w')