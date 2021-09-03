from selenium import webdriver
from selenium.webdriver.common.by import By
import json


start = 0
product_list = []

for i in range(1, 11):
    driver = webdriver.Chrome()
    driver.set_window_size(width=1600, height=900)
    driver.minimize_window()
    driver.implicitly_wait(15)
    link_address = f"https://www.coupang.com/np/campaigns/82/components/445759?listSize=120&page={i}"
    driver.get(link_address)
    h1 = driver.find_element(By.TAG_NAME, 'h1').text
    cards = driver.find_elements(By.CSS_SELECTOR, 'li.baby-product.renew-badge')
    for card in cards:
        diction = {}
        product_link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
        product_img = card.find_element(By.CSS_SELECTOR, 'a > dl > dt > img').get_attribute('src')
        description = card.find_element(By.CSS_SELECTOR, 'a > dl > dd > div.name').text
        price_value = card.find_element(By.CSS_SELECTOR, 'a > dl > dd > div.price-area').text
        diction['link'] = product_link
        diction['image'] = product_img
        diction['name'] = description
        diction['price'] = price_value
        diction['id'] = start
        product_list.append(diction)
        print(description)
        start += 1
    driver.quit()
with open('coupang_catfood.json', 'w', encoding='utf8', newline="") as outputfile:
    json.dump(product_list, outputfile, ensure_ascii=False, indent=2)
