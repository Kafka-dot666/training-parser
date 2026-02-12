from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from bs4 import BeautifulSoup
import time
import random

#агенты
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
   
]

#профиль + опции(работают или нет я не знаю XD)
profile = FirefoxProfile()
random_user_agent = random.choice(user_agents)
profile.set_preference("general.useragent.override", random_user_agent)
firefox_options = Options()
firefox_options.profile = profile
driver = webdriver.Firefox(options=firefox_options)

#переходы по ссылкам
driver.get("https://ya.ru/")
time.sleep(4)
driver.get("https://rasp.rsreu.ru/schedule-frame/group")

#парсер
html = driver.page_source  #берет HTML с конкретной страницы
soup = BeautifulSoup(html, 'html.parser')
results = soup.find_all(class_='select-wrap') #выбрать класс "select-wrap"

#из класса "select-wrap" нужно вытащить все "options" с "value"(данными)
for result in results:
    options = result.find_all('option')  
    for option in options:
        value = option.get('value')  
        text = option.get_text(strip=True)  
        print(f'Value: {value}, Text: {text}')

time.sleep(10)
driver.quit()



