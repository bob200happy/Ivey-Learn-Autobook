from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter import *
import pyautogui

class IveyLearnBot(object): 
    
    def LearnLogIn(self):

        email = driver.find_element(By.ID, 'userNameInput')
        email.send_keys('EMAIL')

        password = driver.find_element(By.ID, 'passwordInput')
        password.send_keys('PASSWORD')

        signIn = driver.find_element(By.ID, 'submitButton')
        signIn.click()

        time.sleep(2)

        duoButton = driver.find_element(By.ID, 'passcode')
        duoButton.click()

        duoCodeEntry = driver.find_element(By.NAME, 'passcode')

        duoCodeEntry.send_keys('2FACODE')
        duoButton.click()

        roomBooking = driver.find_element(By.ID, 'context_external_tool_532_menu_item')
        roomBooking.click()

        time.sleep(2)

        for x in range(7):
            driver.switch_to.default_content()
            frame = driver.find_element(By.NAME, 'tool_content')
            driver.switch_to.frame(frame)
            nextDay = driver.find_element(By.CLASS_NAME, 'icon-arrow-right')
            nextDay.click()
            time.sleep(2)
    
    def selectRooms(self):
        time.sleep(5)
        pyautogui.click(1157, 718)
        time.sleep(5)
        pyautogui.click(1119, 780)
        time.sleep(5)
        pyautogui.click(1081, 780)
        time.sleep(5)
        pyautogui.click(1043, 780)

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('https://learn.ivey.ca')
    driver.implicitly_wait(5)

    bot = IveyLearnBot()
    bot.LearnLogIn()
    bot.selectRooms()

'''
driver.switch_to.default_content()
frame = driver.find_element(By.NAME, 'tool_content')
driver.switch_to.frame(frame)

a3104 = driver.find_element(By.XPATH, "//td[@title='Room 3104 @ 6pm'][@class='selectRoomCell bookableRoom']")
a3104.click()
'''
