#!usr/bin/env python3
from selenium import webdriver

# launch url
url = 'http://chatbot.admiralbulldog.live/playsound'

# create a browser session with webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

