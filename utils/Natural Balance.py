from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Natural_Balance_url_list = result['Natural Balance']
driver = webdriver.Chrome()
driver.implicitly_wait(10)
NBalance = []


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
    driver.get(formula['url'])
    time.sleep(2)
    if not formula['descriptions']:
        formula['descriptions'] = get_text_by_css('#content > div.module.product-detail-header > div > div.meta.animated.fadeInUp.in-view > div.product-description > div > div > div > p')
    driver.execute_script("window.scrollBy(0, 900);")
    if not formula['key_benefits']:
        formula['key_benefits'] = get_text_by_css('p.Description__consist-text')
    driver.execute_script("window.scrollBy(0, 600);")
    if not formula['analysis']:
        formula['analysis'] = get_text_by_css('#tab-nutrition > div > div.left > div > div > table > tbody > tr')
    if not formula['ingredients']:
        formula['ingredients'] = get_text_by_css('#tab-nutrition > div > div.right > div > div:nth-child(1) > div > div > div > div')
    formula['calorie'] = get_text_by_css('#tab-nutrition > div > div.right > div > div:nth-child(2) > div > p')
    print(formula)
output_file = open("./data/Natural_Balance_.json", mode="w", encoding="utf-8")
json.dump(NBalance, output_file, indent=3, ensure_ascii=False)
input_file.close()
output_file.close()
