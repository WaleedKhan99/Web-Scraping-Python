import requests

def fetchAndSaveTofile(url, path):
    r = requests.get(url)
    with open (path, "w") as f:
        f.write(r.text)

url = "https://www.codewithharry.com/"

fetchAndSaveTofile(url, "data/file.html")

