import pickle
import time 
from selenium import webdriver
import random
import bs4
import requests
import json

driver = webdriver.Firefox(executable_path='D:\\aliexpress\\geckodriver.exe')
categories = []
link = []
updatedlink = [] 
count = []
session = requests.session()
cat_p = {}

json_array = []

driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)


def extract_categories(cat_page_url):
    driver.get(cat_page_url)
    data = driver.page_source
    
    soup = bs4.BeautifulSoup(data, 'html.parser')
    for div in soup.find_all('div',{'class':'item util-clearfix'}):
        link.append(div.find('a').get('href'))
    
    for l in link:
        updatedlink.append("https:"+l)
    for _ in updatedlink:
           driver.get(_)
           time.sleep(5)
           data = driver.page_source
           soup = bs4.BeautifulSoup(data, 'html.parser')
           for div in soup.find_all('div',{'class':'ui-breadcrumb'}):
                #print(div)
                k = div.find('h1')
                while k:
                        categories.append(k.find('span').text)
                        break

                else :
                        pass
                    
           for div in soup.find_all('div',{'class':'search-result'}):
              count.append(div.find('strong',{'class':'search-count'}).text)
           time.sleep(random.choice([15,20,17]))
    
if __name__ == '__main__':
            extract_categories('https://www.aliexpress.com/all-wholesale-products.html?spm=2114.search0603.2.2.6d983d375OKIfy')
            for _ in categories:
                    cat_tp = {}
                    i = categories.index(_)
                    cat_tp['category'] = _
                    cat_tp['count'] = count[i]
                    json_array.append(cat_tp)
            print(json_array)
            data_json = json.dumps(json_array)
            requests.post('https://tech.hawkscode.in/alishark/app/CategoryData', data_json)
