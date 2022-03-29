import time
import pandas as pd 
import numpy as np
# hedha selenuim eli bech nestaamlouh fi scraping ama zeda yesta3mlouh fil testing lil web applications just ma3louma bonus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
# hedha el webdriver eli howa bech yhel el site eli bech naamlo scraping fi ay navigateur t7eb ena hatit chrome 
from webdriver_manager.chrome import ChromeDriverManager
# bech matsirech machakel khater kol pc o kifeh masboub fih chrome driver wala lee 3malna el line hedha bech nsobo driver ken moch maojoud o ye5dem kol chey
browser = webdriver.Chrome(ChromeDriverManager().install())
# baaed masabina el driver o hatineh fil variable browser bech nestaamlouh bech n7elo el site 


url = "https://www.dermstore.com/skin-care.list?pageNumber="
p=1
base=[]
condition=True
while True:
    if(p == 86): break
    try:
        browser.get(url+str(p))
        elems = browser.find_elements_by_css_selector(".productBlock_link")
        time.sleep(2)
        base = base + [elem.get_attribute('href') for elem in elems]
        time.sleep(2)
        p=p+1
        print("Navigating to Next Page")
    except (TimeoutException, WebDriverException) as e:
            print(e)
            break

array = set(base)
stock=[]
for link in array:
    content=[]
    browser.get(link)
    time.sleep(2)
    try:
        title = browser.find_element_by_css_selector(".breadcrumbs_item-active").text
        content.append(title)
    except NoSuchElementException:
        content.append("None")
    time.sleep(2)
    try:
        price = browser.find_element_by_css_selector(".productPrice_price").text
        content.append(price)
    except NoSuchElementException:
        content.append("None")
    time.sleep(2)
    try:
        stars = browser.find_element_by_css_selector(".athenaProductReviews_aggregateRatingValue").text
        content.append(stars)
    except NoSuchElementException:
        content.append("None")
    time.sleep(2)
    try:
        reviews = browser.find_element_by_css_selector(".athenaProductReviews_reviewCount").get_attribute('data-total-reviews')
        content.append(reviews)
    except NoSuchElementException:
        content.append("None")
    time.sleep(2)
    #details1 =  browser.find_element_by_css_selector(".productDescription_contentPropertyListItem .productDescription_contentPropertyListItem_atAGlance")
    #print(details1.get_attribute('innerHTML'))
    
    #application_area = "None"
    #ideal_for_these_concerns = "None"
    #ingredient="None"
    #makeup="None"
    
    details2 = browser.find_elements_by_css_selector(".productDescription_contentPropertyValue")
    time.sleep(2)
    Range = "None"
    Volume = "None"
    Brand="None"
    i=0
    for d in details2:
        i=i+1
        #print(d.find_element_by_tag_name('div').get_attribute('innerHTML'))
        if(d.get_attribute('data-information-component') == "range"):
            Range=d.find_element_by_tag_name('div').get_attribute('innerHTML')
            
        if(d.get_attribute('data-information-component') == "volume"):
            Volume=d.find_element_by_tag_name('div').get_attribute('innerHTML')
        
        if(d.get_attribute('data-information-component') == "brand"):
            Brand=d.find_element_by_tag_name('div').get_attribute('innerHTML')
    
    content.append(Range)
    content.append(Volume)
    content.append(Brand)
   
    print("item",i)
    
    stock.append(content)
    if(i == 2):
        break

items = np.asarray(stock)
pd.DataFrame(items).to_csv('items.csv')