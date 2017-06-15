'''
    Reason to use Selenium over the webscrape module "urllib.request" is because Selenium uses web engine which can render JavaScript webpages.
    More notes on my publically viewable google doc, https://www.bit.ly/JeePython
'''
import time

def Delay():
    time.sleep(1)
#Sometimes you're going to need to let the JavaScript load, easily done by adding a second delay.

import selenium.webdriver
#Selenium is a 3rd party module installed through the command prompt by typing "pip install selenium"
#Selenium.webdriver is what I call a "sub-module" which is installed with selenium

WebVar = selenium.webdriver.Chrome()
#WebVar is the variable we assigned to selenium.webdrive.Chrome
#Chrome is the web engine being used and needs to be installed from https://sites.google.com/a/chromium.org/chromedriver/downloads

WebVar2 = selenium.webdriver.PhantomJS()
#Another example using a seperate web engine called PhatomJS which can be installed from http://phantomjs.org/
#PhantomJS unlike Chromedriver is a "HEADLESS" webbrowser meaning it will not display anything.
#Chrome is developing a headless webbrowser of their own now.

WebVar.get('https://website.com')
#This is function that can recieve information from a website.

print(WebVar.title)
#This will print the title header of a website that our variable has obtained.

WebVar.find_element_by_xpath('//*[@id="site-menu"]/li[2]/a').click()
WebVar.find_element_by_xpath('//*[@id="designSideBar"]/span').click()
#WebVar.find_element_by_xpath('//*[@id="searchTemplates"]').click()
#This allows you to have selenium automatically click something for you.
#Firstly, You need to get the xpath name, you obtain this through the inspection tool on your web browser.
#Right click the button > Click inspect > Right click highlighted element > Copy > Copy Xpath

Delay()
WebVar.find_element_by_xpath('//*[@id="searchTemplates"]/form/input[1]').click()
#Here we call a delay to prevent an error of Xpath not found.

Send = WebVar.find_element_by_xpath('//*[@id="searchTemplates"]/form/input[1]')
Send.send_keys('test')
#This allows us to put text input into fields that can take text such as a search bar.