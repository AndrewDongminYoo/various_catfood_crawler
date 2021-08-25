from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Greatness_url_list = result["Natural Greatness"]
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=7)
# Greatness = []
scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
scroll_300px = "window.scrollBy(0, 300);"
get_window_height = "return document.body.scrollHeight"
last_height = driver.execute_script(get_window_height)


def get_text_by_xpath(xpath):
    result_list = []
    targets = driver.find_elements(By.XPATH, xpath)
    if len(targets) == 0:
        return None
    if len(targets) == 1:
        return targets[0].text.replace("\n", " ")
    elif len(targets) > 1:
        for t in targets:
            if t.text:
                result_list.append(t.text.replace("\n", " "))
        if len(result_list) == 1:
            return result_list[0]
        return result_list


# for url in Greatness_url_list:
#     driver.get(url)
#     title = driver.title
#     driver.execute_script('window.scrollBy(0,200);')
#     descriptions = get_text_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/section[4]/div/div/div/div/div/div[1]/div/div/p')
#     driver.execute_script('window.scrollBy(0,200);')
#     key_benefits = get_text_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/section[4]/div/div/div/div/div/div[13]/div/div/p[3]')
#     driver.execute_script('window.scrollBy(0,200);')
#     ingredients = get_text_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/section[4]/div/div/div/div/div/div[9]/div/div/p')
#     driver.execute_script('window.scrollBy(0,200);')
#     analysis = get_text_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/section[4]/div/div/div/div/div/div[13]/div/div/p[1]')
#     driver.execute_script('window.scrollBy(0,200);')
#     calorie = get_text_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/section[4]/div/div/div/div/div/div[13]/div/div/p[2]')
#     product = {
#         "url": url,
#         "title": title,
#         "descriptions": descriptions,
#         "key_benefits": key_benefits,
#         "ingredients": ingredients,
#         "analysis": analysis,
#         "calorie": calorie
#     }
#     print(product)
#     Greatness.append(product)
# driver.quit()
# output_file = open("./data/Natural Greatness.json", mode="w", newline="", encoding="utf-8")
# json.dump(obj=Greatness, fp=output_file, indent=3, ensure_ascii=False)
# output_file.close()

input_file = open("./data/Natural Greatness.json", mode="r", newline="", encoding="utf-8")
Greatness = json.load(input_file)
for formula in Greatness:
    for key, value in formula.items():
        if not value:
            driver.get(formula['url'])
            formula[key] = input(f'"{key}" => ')

output_file = open("./data/Natural Greatness_.json", mode="w", newline="", encoding="utf-8")
json.dump(obj=Greatness, fp=output_file, indent=3, ensure_ascii=False)
input_file.close()
output_file.close()
driver.quit()
