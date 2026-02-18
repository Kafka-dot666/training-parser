
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
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

data_list = []
data_list1 = []

#из класса "select-wrap" нужно вытащить все "options" с "value"(данными)
for result in results:
    options = result.find_all('option')  
    for option in options:
        value = option.get('value')  
        text = option.get_text(strip=True)  
        data_list.append({'value': value, 'text': text})
        print(f'Value: {value}, Text: {text}')
        
try:
    element = WebDriverWait(driver,10 ).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ' .sub-menu > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)')))
    element.click()
except Exception as e:
    print (f"ошибка: {e}")
finally:
    pass
for result in results:
    options = result.find_all('option')  
    for option in options:
        value = option.get('value')  
        text = option.get_text(strip=True)
        data_list1.append({'value': value, 'text': text})  
        
print("Собранные данные:")
for item in data_list1:
    print(item)
    
time.sleep(10)
driver.quit()



