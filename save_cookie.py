import pickle
from selenium import webdriver


#browser = webdriver.Chrome("chromedriver.exe")

browser = webdriver.Firefox(executable_path='D:\\aliexpress\\geckodriver.exe')
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--test-type')
#driver = webdriver.Chrome('chromedriver.exe')
def get_cookies():
    browser.get("https://login.aliexpress.com/buyer.htm?return=https%3A%2Fwww.aliexpress.com%2F&random=CEA73DF4D81D4775227F78080B9B6126")
    
    #browser.get("https://app.alishark.com/login")
    print('input your username and password in chrome and hit submit then come here')
    input('hit enter here if you have submited the form: <enter>')
    cookies = browser.get_cookies()
    pickle.dump(cookies,open("cookies.pickle",'wb'))

def set_cookies():
    browser.get("https://aliexpress.com")
    cookies = pickle.load(open("cookies.pickle","rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    print(cookies)
    browser.get("https://bestselling.aliexpress.com/en")

if __name__=='__main__':
    get_cookies()
