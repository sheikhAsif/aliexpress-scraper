import pickle
import time 
from selenium import webdriver
import random
import pandas as pd
import bs4
import requests
import json

driver = webdriver.Firefox(executable_path='D:\\aliexpress\\geckodriver.exe')
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--test-type')
#driver = webdriver.Chrome('chromedriver.exe')
categories = []
link = []
updatedlink = [] 
count = []
session = requests.session()
cat_p = {}

driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)


def extract_categories(cat_page_url):
    driver.get(cat_page_url)
    time.sleep(5)
    data = driver.page_source
    
    soup = bs4.BeautifulSoup(data, 'html.parser')
    for div in soup.find_all('div',{'class':'item util-clearfix'}):
        #categories.append(div.find('a').text)
        link.append(div.find('a').get('href'))
    
    for l in link:
        updatedlink.append("https:"+l)
    
    for _ in updatedlink:
           #data = requests.get(_,headers=agent)
           driver.get(_)
           data = driver.page_source
           soup = bs4.BeautifulSoup(data, 'html.parser')
           for div in soup.find_all('div',{'class':'ui-breadcrumb'}):
               for h1 in soup.find_all('h1'):
                   
                    print(h1.find('span'))
                    categories.append(h1.find('span').text)
                    #print(h1.find('span',{'data-spm-anchor-id':'2114.search0103.0.i3.11801a5e4N57o6'}).text)
           for div in soup.find_all('div',{'class':'search-result'}):
              count.append(div.find('strong',{'class':'search-count'}).text)
           time.sleep(random.choice([15,20,17]))
           #time.sleep(1)     
    
if __name__ == '__main__':
            extract_categories('https://www.aliexpress.com/all-wholesale-products.html?spm=2114.search0603.2.2.6d983d375OKIfy')
            #print(categories)
            #print(updatedlink)
            #print(count)
            #print(len(count))
            #print(len(categories))
            #print(len(updatedlink))
            for _ in categories:
                    i = categories.index(str(_))
                    cat_p[_] = count[i]
            #print(cat_p)
            head = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            data_json = json.dumps(cat_p)
            print(data_json)
            requests.post('https://tech.hawkscode.in/alishark/app/Categorydata', data_json, headers=head)
            #requests.post('https://tech.hawkscode.in/acc/check.php', data_json, headers=head)
