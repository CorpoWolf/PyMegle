'''
View the coding live on Twitch @ https://www.twitch.tv/gmangavin and look at the github @ https://github.com/gmangavin/PyWeb
chromedriver for gui view, phantomjs for ghost view.
'''

import selenium.webdriver #Imports module
import time #Imports time
import threading #Imports threading, used to have multiple things happen at the same time.
import os #Imports OS

N = False #Used for the bool loop.
while N == False:
    EngineChoice = input('Would you like a visual of the bot? (Y/N): ') #Part one for the web driver choice
    YN = (EngineChoice.lower()) #Prevents capatalization error.
    if YN == ('y'):
        while N == False:
            VarChoice = input('Would you like Firefox or Chrome? (F/C): ') #Part two for the web driver choice
            FC = (VarChoice.lower()) #Prevents capatalization error.
            if FC == ('f'):
                try:
                    WebVar = selenium.webdriver.Firefox()
                    N = True
                except selenium.common.exceptions.WebDriverException:
                    print("You don't seem to have this webdriver installed.")
            elif FC == ('c'):
                try:
                    WebVar = selenium.webdriver.Chrome()
                    N = True
                except:
                    print("You don't seem to have this webdriver installed.")
            else:
                print('Try again')
    elif YN == ('n'):
        try:
            WebVar = selenium.webdriver.PhantomJS()
            N = True
        except selenium.common.exceptions.WebDriverException:
                    print("You don't seem to have this webdriver installed.")
    else:
        print('Try again')
#A while loop to make sure the user enters in a correct character.
#Allows the user to choose which web driver they want to use.

Interest = input("What is a common interest you're looking for?: ")
WebVar.get('https://www.omegle.com')
print(WebVar.title)

WebVar.find_element_by_xpath('//*[@id="topicsettingscontainer"]/div/div[1]/span[2]').click() #Clicks the area for typing
Send = WebVar.find_element_by_class_name('newtopicinput') #Creates an input variable for text area.
Send.send_keys(Interest + ',') #Sends input to text area.

WebVar.find_element_by_xpath('//*[@id="textbtn"]').click() #Clicks the 'text' button

def UserMode(*args):
    while True:
        UserM = input('') #Has the user type an interest.
        Sending = WebVar.find_element_by_class_name('chatmsg') #Takes the class used for user input.
        Sending.send_keys(UserM)
        WebVar.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/table/tbody/tr/td[3]/div/button').click()

def StatusMode(*args):
    threading.Thread(target=UserMode).start()
    StatusNew = None
    while True:
        Status = WebVar.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div[1]/div').text #Takes the text info from xpath
        if StatusNew == (Status):
            continue
        else:
            StatusNew = Status
            os.system('cls')#Refreshes chat.
            print(StatusNew)
            print('')

threading.Thread(target=StatusMode).start()