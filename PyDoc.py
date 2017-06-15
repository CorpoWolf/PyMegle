'''
    Reason to use Selenium of the build in webscrape module "urllib.request" is Selenium uses web engine which can render JavaScript webpages.
'''
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