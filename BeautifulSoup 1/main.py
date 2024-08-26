# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements 
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal
title = soup.title
# print(title)

# Commonly used types of objects: 
# 1. Tag ---- Print(type(title))
# 2. NavigableString ---- Print(type(title.string))
# 3. BeautifulSoup ---- Print(type(soup))
# 4. Comment 
markup = "<p><!-- This is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
# exit()


# # Get all the paragraph from the page
# paras = soup.find_all('p')
# # print(paras)

# # get first element in the HTML Page
# print(soup.find('p'))

# # To find a first paragraph or classes in the HTML Page
# print(soup.find('p')['class'])

# # Find all the elements of specific class
# print(soup.find_all("p", class_="lead")) 

# # Get the text from tags/soup
# print(soup.find("p").get_text())
# print(soup.get_text())

# # Get all the anchor tags from the page
# anchors = soup.find_all('a')
# print(anchors)

# # Get all the links on the page:
# anchors = soup.find_all('a')
# all_links = set()

# for link in anchors:
#     if (link.get('href') != ('#')):
#         linkText = "https://codewithharry.com" +link.get('href') 
#         all_links.add(link)
#         print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

for item in navbarSupportedContent.strings:
    print(item)

        
    

