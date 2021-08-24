from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Natural_Balance_url_list = result['Natural Balance']
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=7)
NBalance = []


def set_attr(element_id: str, attr_to_on: str):
    driver.execute_script(f"document.getElementById('{element_id}').setAttribute('{attr_to_on}','true');")

scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
scroll_300px = "window.scrollBy(0, 300);"
get_window_height = "return document.body.scrollHeight"
last_height = driver.execute_script(get_window_height)
# while True:
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     driver.execute_script(scroll_300px)
#     time.sleep(1)
#     new_height = driver.execute_script(get_window_height)
#     if new_height == last_height:
#         break
#     last_height = new_height

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


# for url in Natural_Balance_url_list:
#     try:
#         driver.get(url)
#         title = driver.title
#         time.sleep(2)
#         driver.execute_script("window.scrollBy(0, 300);")
#         descriptions = get_text_by_css('div > div > div > div > div > div > div > div > div.product-highlights-title')
#         key_benefits = get_text_by_css('div.slick-slide > div > div.item > h6.benefit')
#         driver.execute_script("window.scrollBy(0, 1400);")
#         analysis = get_text_by_css('div.mobile-drawer-content > table > tbody > tr')
#         ingredients = get_text_by_css('div.product-nutritional-wrapper:nth-child(2) div.product-nutritional-section > div.product-nutritional-title')
#         calorie = get_text_by_css('main.product-detail.theme.dark-blue:nth-child(5) div.module.product-detail-tabs.animated.fadeInUp.in-view:nth-child(3) div.tabs-content div.tab-content.active:nth-child(1) div.tb-wrap div.right div.h-set div.mobile-drawer.open:nth-child(2) div.mobile-drawer-content:nth-child(2) > p:nth-child(1)')
#         product = {
#             "url": url,
#             "title": title,
#             "key_benefits": key_benefits,
#             "descriptions": descriptions,
#             "ingredients": ingredients,
#             "analysis": analysis
#         }
#         print(product)
#         NBalance.append(product)
#     except NoSuchElementException:
#         driver.quit()
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(5)
# driver.quit()
# output_file = open("./data/Natural_Balance.json", mode="w", newline="", encoding="utf-8")
# json.dump(obj=NBalance, fp=output_file, indent=3, ensure_ascii=False)
# output_file.close()
input_file = open("./data/Natural_Balance.json", mode="r", encoding="utf-8")
NBalance = json.load(input_file)
for formula in NBalance:
#     driver.get(formula['url'])
#     formula['descriptions'] = get_text_by_xpath('//*[@id="content"]/div[1]/div/div[2]/div[1]/div/div/div')
#     driver.execute_script('window.scrollTo(0, 600);')
#     time.sleep(2)
#     formula['key_benefits'] = get_text_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/div/div/div/div/h6')
#     driver.execute_script('window.scrollTo(0, 1350);')
#     time.sleep(2)
#     formula['analysis'] = get_text_by_xpath('//*[@id="tab-nutrition"]/div/div[1]/div/div/table/tbody/tr')
#     driver.execute_script('window.scrollTo(0, 1350);')
#     time.sleep(2)
#     formula['ingredients'] = get_text_by_xpath('//*[@id="tab-nutrition"]/div/div[2]/div/div[1]/div/p[2]')
#     driver.execute_script('window.scrollTo(0, 1450);')
#     time.sleep(2)
#     formula['calorie'] = get_text_by_xpath('//*[@id="tab-nutrition"]/div/div[2]/div/div[2]/div/p')
    print(formula)
# output_file = open("./data/Natural_Balance_.json", mode="w", encoding="utf-8")
# json.dump(NBalance, output_file, indent=3, ensure_ascii=False)
# input_file.close()
# output_file.close()
