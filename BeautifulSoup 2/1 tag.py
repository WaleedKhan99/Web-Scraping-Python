import requests
from bs4 import BeautifulSoup

with open('sample.html','r')as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser') 
# print(soup.prettify) 
# # print(soup.title, type(soup.title))
# print(soup.div)
# print(type(soup.find_all('div')[0]))

# for link in soup.find_all('a'):
#     print(link.get('href'))


# cont = soup.find(class_="container")
# cont.name = "span"
# cont["class"] = "myclass class2"
# cont.string = "I am a string" 
# print(cont)


# ulTag = soup.new_tag('ul')

# liTag = soup.new_tag('li')
# liTag.string = 'home'
# ulTag.append(liTag)


# liTag = soup.new_tag('li')
# liTag.string = 'about'
# ulTag.append(liTag)

# soup.html.body.insert(0, ulTag)
# with open ("modify.html", "w") as f:
#     f.write(str(soup))


# It is use to check a specific attribute is present or not!
cont = soup.find(class_="container")
print(cont.has_attr("id"))

