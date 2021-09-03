from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.set_window_size(width=1600, height=900)
driver.minimize_window()
driver.implicitly_wait(15)

with open('json/MAMACATURL.txt', 'r', encoding='utf8', newline="") as input:
    formulas_list = []
    for idx, line in enumerate(input.readlines()):
        driver.get(line)
        diction = {}
        title = driver.find_element(
            By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[2]/div[1]/h2').text
        image = driver.find_element(
            By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[1]/div[1]/div/a/img').get_attribute('src')
        diction['id'] = idx
        diction['name'] = title
        diction['image'] = image
        table = driver.find_element(
            By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[2]/div[2]/table/tbody')
        head = table.find_elements(By.TAG_NAME, 'th')
        data = table.find_elements(By.TAG_NAME, 'td')
        for one, two in zip(head, data):
            diction[one.text] = two.text
            print(two.text)
        formulas_list.append(diction)
with open('./mamacat.json', 'w', encoding='utf8', newline="") as output:
    json.dump(formulas_list, output, ensure_ascii=False, indent=4)
