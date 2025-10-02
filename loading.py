from bs4 import BeautifulSoup
import requests
import os

diseases = ["cholera", "malaria", "cancer", "coronavirus-disease-(covid-19)", "rabies"]

for disease in diseases:
    with open(f"disease/{disease}.html", "w", encoding="utf-8") as f:
        a = requests.get(f"https://www.who.int/news-room/fact-sheets/detail/{disease}")
        f.write(a.text)
        print(f"{disease}.html")