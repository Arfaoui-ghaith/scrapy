from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError,ConnectionError
import pandas as pd
import numpy as np

#url="https://www.skinstore.com/skin-care/see-all-skin-care.list?pageNumber="
url = "https://www.skinstore.com/hair-care/see-all-hair-care.list?pageNumber="
p=1
base=[]
index=0
while (p<21):
    try:
        page = requests.get(url+str(p))
        if(page.status_code == 200):
            soup = BeautifulSoup(page.text, 'html.parser')
            
            items = set([ elem['href'] for elem in soup.find_all('a', { 'class': 'productBlock_link' }) ])
            
            for item in items:
                index=index+1
                content=[]
                if(page.status_code == 200):
                    
                    itemPage = requests.get("https://www.skinstore.com"+item)
                    soupItem = BeautifulSoup(itemPage.text, 'html.parser')

                    try: content.append(str(soupItem.find('h1', { 'class': 'productName_title' }).text.strip())) 
                    except : content.append("None")
                    
                    try: content.append(str(soupItem.find('p', { 'class': 'productPrice_price' }).text.strip()))
                    except : content.append("None")
                    
                    try: content.append(str(soupItem.find('span', { 'class': 'productReviews_aggregateRatingValue' }).text.strip()))
                    except : content.append("None")
                    
                    try: content.append(str(soupItem.find('p', { 'class': 'productReviews_reviewCount' }).text.split(' ')[0]))
                    except : content.append("None")

                    try: content.append(str(soupItem.find('div', { 'data-information-component': 'ingredients' }).div.p.text.split(',')))
                    except: content.append("None")

                    try: content.append(str(soupItem.find('div', { 'data-information-component': 'brand' }).div.text.strip()))
                    except: content.append("None")

                    try: content.append(str(soupItem.find('div', { 'data-information-component': 'volume' }).div.text.strip()))
                    except: content.append("None")
                    
                    
                    base.append(content)

                    print('Item '+str(index)+' elements scraped !')
                
        print('Move to Page '+str(p)+' ------------------------ all elements scraped !')
        p=p+1
    except (HTTPError,ConnectionError):
        print("something went wrong !")

print(len(base))
items = np.asarray(base)
pd.DataFrame(items).to_csv('items2.csv')


