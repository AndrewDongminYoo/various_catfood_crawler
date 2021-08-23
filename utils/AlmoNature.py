from selenium import webdriver
from selenium.webdriver.common.by import By
from import_csv import result
import json

Amlonature_url_list = result['AlmoNature']
driver = webdriver.Chrome()
driver.implicitly_wait(10)
almo = []


def get_text_by_xpath(xpath):
    result_list = []
    targets = driver.find_elements(By.XPATH, xpath)
    if len(targets) == 0:
        return None
    if len(targets) == 1:
        return targets[0].text.replace("\n", " ")
    for t in targets:
        if t.text:
            result_list.append(t.text.replace("\n", " "))
    return result_list


def get_text_by_css(css):
    result_list = []
    targets = driver.find_elements(By.CSS_SELECTOR, css)
    if len(targets) == 0:
        return None
    elif len(targets) == 1:
        return targets[0].text.replace("\n", " ")
    for t in targets:
        if t.text:
            result_list.append(t.text.replace("\n", " "))
    return result_list


# for url in Amlonature_url_list:
#     driver.get(url)
#     title = driver.title[0:-19]
#     descriptions = get_text_by_xpath('//*[@id="product"]/div/section[1]/div[2]/p')
#     key_benefits = get_text_by_xpath('//*[@id="product"]/div/section[1]/ul/li[1]/div[2]')
#     analysis = get_text_by_xpath('//*[@id="product"]/div/section[2]/div/div[3]/ul/li')
#     ingredients = get_text_by_xpath('//*[@id="product"]/div/section[2]/div/div[4]/div/ul/li/p')
#     calorie = get_text_by_xpath('//*[@id="product"]/div/section[2]/div/div[3]/ul/li[6]/span[2]/b')
#     product = {
#         "url": url,
#         "title": title,
#         "key_benefits": key_benefits,
#         "descriptions": descriptions,
#         "ingredients": ingredients,
#         "analysis": analysis,
#         "calorie": calorie
#     }
#     print(product)
#     almo.append(product)
# driver.quit()
# input_file = open("./data/AlmoNature.json", mode="w", newline="", encoding="utf-8")
# json.dump(obj=almo, fp=input_file, indent=3, ensure_ascii=False)
# input_file.close()
input_file = open("./data/AlmoNature.json", mode="r", encoding="utf-8")
almo = json.load(input_file)
for formula in almo:
    driver.get(formula['url'])
    if not formula['descriptions']:
        formula['descriptions'] = get_text_by_css('p.Description__text')
    if not formula['key_benefits']:
        formula['key_benefits'] = get_text_by_css('p.Description__consist-text')
    if not formula['analysis']:
        formula['analysis'] = get_text_by_css('li.Ingredients__el')
    if not formula['ingredients']:
        formula['ingredients'] = get_text_by_css('div.Ingredients__text')
    print(formula)
input_file2 = open("./data/AlmoNature_.json", mode="w", encoding="utf-8")
json.dump(almo, input_file2, indent=3, ensure_ascii=False)
input_file2.close()
input_file.close()
