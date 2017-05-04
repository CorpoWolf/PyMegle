'''
View the coding live on Twitch @ https://www.twitch.tv/gmangavin and look at the github @ https://github.com/gmangavin/PyScrape
'''
import selenium.webdriver #Imports module
 
driver = selenium.webdriver.Chrome() #Opens chromium browser
driver.get('https://www.omegle.com') #Goes to this site
driver.find_element_by_xpath("""//*[@id="textbtn"]""").click() #Click a button.
print(driver.title) #prints website title to console.