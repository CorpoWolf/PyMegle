'''
View the coding live on Twitch @ https://www.twitch.tv/gmangavin and look at the github @ https://github.com/gmangavin/PyWeb
chromedriver for gui view, phantomjs for ghost view.
'''

import selenium.webdriver #Imports module
import time #Imports time

N = False
while N == False:
    EngineChoice = input('Would you like a visual of the bot? (Y/N): ')
    YN = (EngineChoice.lower())
    if YN == ('y'):
        while N == False:
            VarChoice = input('Would you like Firefox or Chrome?: (F/C)')
            FC = (VarChoice.lower())
            if FC == ('f'):
                WebVar = selenium.webdriver.Firefox()
                N = True
            elif FC == ('c'):
                WebVar = selenium.webdriver.Chrome()
                N = True
            else:
                print('Try again')
    elif YN == ('n'):
        WebVar = selenium.webdriver.PhantomJS()
        N = True
    else:
        print('Try again')
#A while loop to make sure the user enters in a correct character.
#Allows the user to choose which web driver they want to use.

Interest = input("What is a common interest you're looking for?: ")
WebVar.get('https://www.omegle.com')
print(WebVar.title)
WebVar.find_element_by_xpath('//*[@id="topicsettingscontainer"]/div/div[1]/span[2]').click()

Send = WebVar.find_element_by_xpath('//*[@id="topicsettingscontainer"]/div/div[1]/span[2]')
Send.send_keys(Interest + ',')

WebVar.find_element_by_xpath('//*[@id="textbtn"]').click()