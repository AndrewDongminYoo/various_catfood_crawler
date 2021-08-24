from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Royal_Canin_url_list = result['RoyalCanin']
driver = webdriver.Chrome()
driver.implicitly_wait(10)
royal = []


def set_attr(element_id: str, attr_to_on: str):
    driver.execute_script(f"document.getElementById('{element_id}').setAttribute('{attr_to_on}','true');")


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


def get_text_by_css(css):
    result_list = []
    targets = driver.find_elements(By.CSS_SELECTOR, css)
    if len(targets) == 0:
        return None
    elif len(targets) == 1:
        return targets[0].text.replace("\n", " ")
    elif len(targets) > 1:
        for t in targets:
            if t.text:
                result_list.append(t.text.replace("\n", " "))
        if len(result_list) == 1:
            return result_list[0]
        return result_list


# for url in Royal_Canin_url_list:
#     try:
#         driver.get(url)
#         title = driver.title
#         time.sleep(2)
#         driver.execute_script("window.scrollBy(0, 800);")
#         key_benefits = get_text_by_css('div.rc-padding-x--none--mobile > p.rc-margin-y--none')
#         try:
#             driver.execute_script('document.querySelector("#bd_section_productpage ul > li:nth-child(2) > button").click();')
#         except JavascriptException:
#             pass
#         descriptions = get_text_by_css('div > div.rc-margin-y--none--desktop')
#         driver.execute_script("window.scrollBy(0, 1400);")
#         nutrient = get_text_by_css('div.rc-padding-y--md.rc-max-width--md > div.rc-full-width ')
#         product = {
#             "url": url,
#             "title": title,
#             "key_benefits": key_benefits,
#             "descriptions": descriptions,
#             "nutrient": nutrient
#         }
#         print(product)
#         royal.append(product)
#     except NoSuchElementException:
#         driver.quit()
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(5)
# driver.quit()
# input_file = open("./data/Royal_Canin.json", mode="w", newline="", encoding="utf-8")
# json.dump(obj=royal, fp=input_file, indent=3, ensure_ascii=False)
# input_file.close()
input_file = open("./data/Royal_Canin.json", mode="r", encoding="utf-8")
royal = json.load(input_file)
for formula in royal:
    if not formula['descriptions']:
        driver.get(formula['url'])
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 1000);")
        formula['descriptions'] = get_text_by_xpath('//*[@id="product-description-carousel"]/div[1]/p')
    print(formula)
output_file = open("./data/Royal_Canin_.json", mode="w", encoding="utf-8")
json.dump(royal, output_file, indent=3, ensure_ascii=False)
input_file.close()
output_file.close()
