import time
import requests
import csv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

ua = UserAgent().random



with open("aa .txt","r") as f:
    links = f.read().splitlines()



for x in range(28, len(links)):
    url = links[x]
    s=str(x+1)
    t=str(x)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
               }

    requests.session().cookies.clear()
    response = requests.get(url,headers = headers)
    a = random.randint(1, 3)
    time.sleep(a)
    soup = BeautifulSoup(response.content, 'lxml')
    name = soup.find("h1").text
    types = soup.find_all('span', class_= "align-middle")[1].text
    part_link = soup.find_all("span",class_ = "text-muted small")[2].nextSibling["href"]
    link = "https://www.wine-searcher.com"+part_link
    with open('wine_data.csv', 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, types, link])
    print(name,types,link)
    print("Finished at " + t )
    print("Start a " + s)


