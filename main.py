#!usr/bin/env python3
from selenium import webdriver
import bs4
import os
import wget
# launch url
url = input("URL: >>>")
os.makedirs("soundboard", exist_ok=True)

# create a browser session with webdriver
driver = webdriver.Chrome()
driver.get(url)
# wait for all elements to load
driver.implicitly_wait(30)
# save the source
html_page = driver.page_source
# save the page source to file
with open("source.html", "w") as file:
    file.write(html_page)
# close the webdriver
driver.quit()

# load html as BS object
sounds = bs4.BeautifulSoup(html_page, "lxml")
# look for all audio tags in the html code and iterate over them
for link in sounds.find_all('audio'):
    print("downloading " + link['id'])
    # compose a pathname and filename made of html id tag for every file
    filename = 'soundboard/' + link['id'] + '.mp3'
    # skip over file if it already exists, else download
    if not os.path.isfile(filename):
        wget.download(link['src'], filename)
        # print(link)
        # print(filename)
    else:
        print(filename, " already exists")
