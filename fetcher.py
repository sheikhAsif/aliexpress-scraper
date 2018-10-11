import bs4
import time
from selenium import webdriver
import random
import pickle

driver = webdriver.Firefox(executable_path='D:\\Downloads\\geckodriver.exe')
category_name = {}
product_name = {}
product_price = {}
tot_number = {}
wish_list = {}
rating = {}
votes = {}
image = {}

driver.get('https://www.aliexpress.com/')
cookies = pickle.load(open("cookies.pickle","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)


def extract(cat_url):
    driver.get(cat_url)
    time.sleep(5)
    data = driver.page_source

    soup = bs4.BeautifulSoup(data,'html.parser')
    
    for div in soup.find_all('div',{'class':'ui-breadcrumb'}):
            #print(div)
            k = div.find('h1')
            if  k.select('a')[0].text is not None:
                category_name['main_category_name'] = k.select('a')[0].text

            try:
                if  k.select('a')[1].text is not None:
                    category_name['sub_category_name'] = k.select('a')[1].text
            except IndexError :
                category_name['sub_category_name'] = k.select('span')[1].text
                break

            try:
                if  k.select('a')[2].text is not None:
                    category_name['sub_sub_category_name'] = k.select('a')[2].text
            except IndexError:
                category_name['sub_sub_category_name'] = k.select('span')[2].text
                break

            try:
                if  k.select('span')[3].text is not None:
                    category_name['sub_sub_sub_category_name'] = k.select('span')[3].text
            except IndexError:
                category_name['sub_sub_sub_category_name'] = k.select('span')[3].text
                break
            
    print(category_name)    
    pl = []
    c = 1
    while c <= 100:
        driver.get('https://www.aliexpress.com/category/200003482/dresses/{0}.html?isrefine=y&site=glo&g=y&needQuery=n&tag='.format(c))
        time.sleep(10)
        data = driver.page_source
        soup = bs4.BeautifulSoup(data,'html.parser')
        for ul in soup.find_all('ul',{'class':'util-clearfix son-list'}):
            if ul.find('div',{'class':'info'}):
                div = ul.find('div',{'class':'info'})
                if div.find('h3') :
                    productlinks = ul.find_all('a',{'class':'product'})
                    
                    for _ in productlinks:
                        pl.append('http:{0}'.format(_.get('href')))
                    
                else:pass
            else:pass
        '''for _ in pl:
             print(_)
             print(len(pl))'''
        
    for link in pl:
        driver.get(link)
        time.sleep(20)
        data = driver.page_source
        soup = bs4.BeautifulSoup(data,'html.parser')
        l = div = soup.find('div',{'class':'store-detail-wrap'})
        print(l)
        if  l == None:
            div = soup.find('div',{'class':'detail-wrap'})
        else:
            div = soup.find('div',{'class':'store-detail-wrap'})

        product_name['product_name'] = div.find('h1',{'class':'product-name'}).text
        product_price['product_price'] = div.find('span',{'class':'p-symbol'}).text + div.find('span',{'class':'p-price'}).text
        tot_number['total number of order'] = div.find('span',{'class':'order-num'}).text
        try:
            rating['rating'] = div.find('span',{'class':'percent-num'}).text
        except Exception:
            rating['rating'] = '0'
        try:
            votes['product votes'] = div.find('span',{'class':'rantings-num'}).text[1:-1]
        except Exception:
            votes['product votes'] = '0'
        img = soup.find('div',{'class':'detail-gallery-main'})
        li = img.find('ul',{'class':'image-thumb-list'})

        link = li.find_all('img')
        b = 0
        global image
        for _ in link:
            image['image {0}'.format(b)] = _.get('src')
            b += 1

            
        wish = driver.execute_script("return document.documentElement.outerHTML")
        wish = bs4.BeautifulSoup(wish,'html.parser')
        wi = wish.find_all('div',{'class':'product-action-block'})
        #print(wi)
        wish_list['wish list'] = wish.find('span',{'class':'wishlist-num'}).text
        print(product_name)
        print(product_price)
        print(tot_number)
        print(wish_list)
        print(rating)
        print(votes)
        print(image)
                



if __name__ == '__main__':
    extract("https://www.aliexpress.com/category/200003482/dresses/1.html?isrefine=y&site=glo&g=y&needQuery=n&tag=")
    
