'''from imessage_reader import fetch_data

fd = fetch_data.FetchData("/Users/michaelgao/Desktop/chat_copy.db")
message = fd.get_messages()

for i in range(100):      
    print(message[i])
'''

import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.moveTo(1146, 747)
pyautogui.click()