import pandas as pd
import time
import requests
import bs4 

session = requests.session()
agent = {'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html'}


reader = pd.read_csv('link.csv')
link = []
count = []

for _ in reader['Links']:
    link.append(_)
c = 0 
for _ in link:
    if c == 3:
        break
    print(_)
    data = requests.get(_,headers=agent)
    print(data)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    print(soup)
    for div in soup.find_all('div',{'class':'search-result'}):
        count.append(div.find('strong',{'class':'search-count'}).text)
    c+=1  

print(count)
print(len(count))

           



