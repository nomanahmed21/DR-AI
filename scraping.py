from bs4 import BeautifulSoup
import requests
import os
import json

diseases = ["cholera", "malaria", "cancer", "coronavirus-disease-(covid-19)", "rabies"]
# diseases = [ "cancer"]
all_chunks =[]
for disease in diseases:
    with open(f"disease/{disease}.html", "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.select('article.sf-detail-body-wrapper')

    for article in articles:
        all_heading = article.find_all('h2')
        for heading in all_heading:
            heading_text =heading.get_text(strip= True)
            if not heading_text:
                print('empty')
            text = ""
            for sibling in heading.find_next_siblings():
                if sibling.name in ["h2", "h3"]:
                    break
                if sibling.name in ['p']:
                    text+= sibling.get_text(" ", strip= True) + " "
                if sibling.name in ['ul']:
                    li_texts = [li.get_text(" ", strip=True) for li in sibling.find_all('li')]
                    text += " ".join(li_texts) + " "


            if text.strip():
                all_chunks.append({
                    "disease": disease,
                    "heading": heading_text,
                    "text": text.strip()
                })

with open("data.json", "w") as f:
    json.dump(all_chunks, f, indent=4, ensure_ascii=False)