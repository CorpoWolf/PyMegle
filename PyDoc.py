import urllib.request #Imports module urllib.request.
import re #Imports module re.
 
html = urllib.request.urlopen("https://www.omegle.com") #Requests info from "website"
scan = str(html.read()) #Processes the information
Title = str(scan.split("<title>")[1]).split("</title>")[0] #Takes post"<title>" & pre"</title>"
Title2 = re.findall(r'<title>(.*?)</title>',str(scan)) #Looks for Everything in between <title> & </title>

print(Title) #Prints "Title"
print(Title2) #Prints "Title2"
 
if 'What do you wanna talk about?' in scan: #Checks for specific text
    print('yep') #Prints 'yep'