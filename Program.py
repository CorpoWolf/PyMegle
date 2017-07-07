'''
View the coding live on Twitch @ https://www.twitch.tv/gmangavin and look at the github @ https://github.com/gmangavin/PyWeb
The 3rd written version on "PyMegle".
'''

import selenium.webdriver #Main module.
import threading #Allows for multi-tasking.
import os #Allows for deletion on cmd text.
import time #Allows for pauses.

while True:
    DriverChoice = input("1) ProjectJS (Invisable) \n2) Chrome \n3) Firefox \n Which webdriver would you like to use?: ")
    if DriverChoice == ("1"):
        try:
            WebVar = selenium.webdriver.PhantomJS()
            break
        except selenium.common.exceptions.WebDriverException:
                    print("You don't seem to have the PhantomJS webdriver installed. You can get it here http://phantomjs.org/")
    elif DriverChoice == ("2"):
        try:
            WebVar = selenium.webdriver.Chrome()
            break
        except selenium.common.exceptions.WebDriverException:
                    print("You don't seem to have the chrome webdriver installed. You can get it here https://sites.google.com/a/chromium.org/chromedriver/downloads")
    elif DriverChoice == ("3"):
        try:
            WebVar = selenium.webdriver.Firefox()
            break
        except selenium.common.exceptions.WebDriverException:
                    print("You don't seem to have the firefox webdriver installed. You can get it here https://github.com/mozilla/geckodriver/releases")
    else:
        print("You need to input a number 1, 2, or 3")
        time.sleep(3)
        os.system('cls')

os.system('cls')
print("loading...")

WebVar.get('https://www.omegle.com')
os.system('cls')
print(WebVar.title)

def Interests():
    Interest = input("What is a common interest you're looking for?: ")
    WebVar.find_element_by_xpath('//*[@id="topicsettingscontainer"]/div/div[1]/span[2]').click()
    Send = WebVar.find_element_by_class_name('newtopicinput')
    Send.send_keys(Interest + ',')
    WebVar.find_element_by_xpath('//*[@id="textbtn"]').click()

def SendMode():
    while True:

        Sending = WebVar.find_element_by_class_name('chatmsg') #Takes the class used for user input.
        Sending.send_keys(UserM)
        WebVar.find_element_by_class_name('sendbtn').click()

def StatusMode():
    threading.Thread(target=SendMode).start()
    StatusNew = None #Create a variable with no value.
    while True:
        Status = WebVar.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div[1]/div').text #Takes the text info from xpath
        if StatusNew == (Status):
            continue
        else:
            StatusNew = Status
            os.system('cls') #Refreshes chat.
            print(StatusNew)
            print('')


Interests()
threading.Thread(target=StatusMode).start()