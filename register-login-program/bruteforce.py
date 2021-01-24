import string
import time
import random

import pyautogui
import subprocess
import sys

startTime = time.time()
letters_and_digits = string.ascii_letters + string.digits
attempts = 0

def check():
    x = pyautogui.locateOnScreen('success.png')
    if x != None:
        return(True)

def guess():
    guess = ''.join(random.choice(letters_and_digits) for i in range(3)) #change range(#) to length of password
    return(guess)

# subprocess.call([cC6sys.executable, 'login2.py', 'htmlfilename.htm'])
time.sleep(3)
startTime = time.time()


entry2 = pyautogui.locateOnScreen('entry2.png')
entry3 = pyautogui.locateOnScreen('entry3.png')
loginButton = pyautogui.locateOnScreen('loginButton.png')

pyautogui.click(entry2, pause = 0.01)
pyautogui.write(guess(), pause = 0.01)
pyautogui.click(loginButton)

while check() != True:
    pyautogui.press('enter', pause = 0.01)

    pyautogui.click(entry3, pause = 0.01)
    pyautogui.write(guess(), pause = 0.01)
    pyautogui.click(loginButton, pause = 0.01)
    attempts += 1
    if attempts % 100 == 0:
        executionTime = (time.time() - startTime)
        print("Time taken for 100 attempts: ",executionTime)

    executionTime = (time.time() - startTime)

print(executionTime,' seconds.', attempts, 'attempts.')

