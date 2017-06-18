'''
View the coding live on Twitch @ https://www.twitch.tv/gmangavin and look at the github @ https://github.com/gmangavin/PyWeb
chromedriver for gui view, phantomjs for ghost view.
'''

import selenium.webdriver #Imports module
import time #Imports time

N = False #Used for the bool loop.
while N == False:
    EngineChoice = input('Would you like a visual of the bot? (Y/N): ') #Part one for the web driver choice
    YN = (EngineChoice.lower()) #Prevents capatalization error.
    if YN == ('y'):
        while N == False:
            VarChoice = input('Would you like Firefox or Chrome?: (F/C)') #Part two for the web driver choice
            FC = (VarChoice.lower()) #Prevents capatalization error.
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

WebVar.find_element_by_xpath('//*[@id="topicsettingscontainer"]/div/div[1]/span[2]').click() #Clicks the area for typing
Send = WebVar.find_element_by_class_name('newtopicinput') #Creates an input variable for text area.
Send.send_keys(Interest + ',') #Sends input to text area.

WebVar.find_element_by_xpath('//*[@id="textbtn"]').click() #Clicks the 'text' button

StatusNew = ''
Connected = False
while Connected == False:
    Status = WebVar.find_element_by_xpath('/html/body/div[7]/div/div/div[1]/div[1]/div').text #Takes the text info from xpath.
    if StatusNew == (Status):
        time.sleep(1)
    else:
        StatusNew = str(Status)
        print(StatusNew)
        time.sleep(1)