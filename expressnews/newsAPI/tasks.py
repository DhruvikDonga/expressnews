from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import numpy as np
import pickle
from .models import Newsapi
from .views import predict
@shared_task
# do some heavy stuff let scrap some newshit
def crawl_news():
    print('Crawling news and creating objects in database ..')
    page = requests.get('https://www.india.com/news/india/')
    bs = BeautifulSoup(page.text, "html.parser")
    #print(bs)
    # Find first 5 table rows
    articles = bs.find("ul",class_="catPgList")
    headlines = articles.find_all('li',class_="catPgListitem")[0:5]
    #print(headlines)
    
    for headline in headlines:
        
        box = headline.find('figcaption')
        #print(box)
        newstitle = box.find('h3').text
        url =box.find('a').attrs['href']

        partipage = requests.get(url)
        bs = BeautifulSoup(partipage.text, "html.parser")
        newpage = bs.find('article',class_="common-text")
        content = newpage.find('p').text.strip()
        
        scrapped_articles=newstitle+content
        labels = ['army', 'buisness', 'politics', 'tech','sport']
        category = labels[predict(scrapped_articles)]

        print(scrapped_articles)
        print(category)
        print("----------------------")
        print(" ".join(content.split()[0:80])+"...tap Learn More")
        Newsapi.objects.get_or_create(
            newstitle = str(newstitle),
            content = str(" ".join(content.split()[0:55])),
            source = "India news",
            category = category,
            url= url
        )
   
   


    sleep(3)

@shared_task
def your_story():
    pass

@shared_task
def crawl_news_techcrunch():
    print('Crawling data and creating objects in database ..')
    page = requests.get('https://www.cnbctv18.com/')
    
    bs = BeautifulSoup(page.text, "html.parser")
    #print(bs)
    # Find first 5 table rows
    articles = bs.find("div",class_="col3")
    
    headlines = articles.find_all('ul')[0:3]
    print(headlines)

    for headline in headlines:
        
        box = headline.find('header')        
        #print(box)
        box = headline.find("h2")
        newstitle = box.find('a').text
        url =box.find('a').attrs['href']
        url='https://techcrunch.com/'+url
        print(url)
        partipage = requests.get(url)
        bs = BeautifulSoup(partipage.text, "html.parser")
        newpage = bs.find('div',class_="pu1zi")
        print(newpage)
        content = newpage.find('p').text
        print(content)
        scrapped_articles=newstitle+content
        labels = ['army', 'buisness', 'politics', 'tech','sport']
        category = labels[predict(scrapped_articles)]

        print(scrapped_articles)
        print(category)
        print("----------------------")
        print(" ".join(content.split()[0:80])+"...tap Learn More")
  
    sleep(3)


while True:
    sleep(1)
    print("Techcrunch----news")
    #crawl_news_techcrunch()
    print("Indianews----news")
    crawl_news()
    print("Yourstory")
    #your_story()
    