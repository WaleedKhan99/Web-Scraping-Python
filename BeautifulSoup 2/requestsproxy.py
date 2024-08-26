import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}
# write ip address api in google browser to get this linl
r=requests.get("https://api64.ipify.org?format=json")
print(r.json())