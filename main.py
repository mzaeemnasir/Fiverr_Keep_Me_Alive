import pyautogui
import subprocess
import time
import random
# display the current mouse position
print("Current mouse position: " + str(pyautogui.position()))   
# Click at the specified x and y coordinates
# minimize the current window
print("Minimizing the current window")
pyautogui.keyDown('winleft')
pyautogui.press('down')
pyautogui.keyUp('winleft')

while True:
    # randomize the interval between each click to make it look more human between 60 and 3000 seconds
    choice = random.choice([True, False])
    if choice:
        interval = random.randint(60, 3000)
        print("Waiting for " + str(interval) + " seconds or " + str(interval/60) + " minutes")
        time.sleep(interval)
        # focus on the current window
        pyautogui.click(x=315, y=102)
    choice = random.choice([True, False])
    if choice:
        interval = random.randint(60, 3000)
        print("Waiting for " + str(interval) + " seconds or " + str(interval/60) + " minutes")
        time.sleep(interval)
        pyautogui.click(x=560, y=617)
        
    choice = random.choice([True, False])
    if choice:
        interval = random.randint(60, 3000)
        print("Waiting for " + str(interval) + " seconds or " + str(interval/60) + " minutes")
        time.sleep(interval)
        pyautogui.click(x=376, y=290)


# Check your  Click Positions
# import pyautogui as py #Import pyautogui
# import time #Import Time

# while True: #Start loop
#     print (py.position())
#     time.sleep(1)