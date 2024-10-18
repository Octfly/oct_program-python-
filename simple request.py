import requests
from bs4 import BeautifulSoup as bs
cishu = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}

while True:
    response = requests.get("网页",headers=headers)
    ct = response.text
    print(response)
    if response.status_code == 200:
        cishu += 1
        print (cishu)
    else:
        break
    #soup = bs(ct,"html.parser")
    #print(soup)
