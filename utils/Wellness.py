from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Wellness_url_list = result["Wellness"]
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=7)
Wellness = []
scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
scroll_300px = "window.scrollBy(0, 300);"
get_window_height = "return document.body.scrollHeight"
last_height = driver.execute_script(get_window_height)


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


for url in Wellness_url_list:
    driver.get(url)
    time.sleep(3)
    driver.execute_script("document.querySelectorAll('p').forEach(p => p.setAttribute('style','display:block;'));")
    title = driver.title
    driver.execute_script("window.scrollTo(0, 200);")
    descriptions = get_text_by_xpath('//*[@id="block-wellness-content"]/div/section[1]/div/div/div[4]/p[3]')
    driver.execute_script("window.scrollTo(0, 600);")
    key_benefits = driver.execute_script('''
    let benefits = document.querySelectorAll("#block-wellness-content > div > section.full-bleed.full-bleed--product-header > section > ul > li > div > img");
    let alts = [];
    for (let i=0;i<benefits.length;i++) {
        let alt = benefits[i].getAttribute('alt');
        alts.push(alt);
    };
    return alts''')
    driver.execute_script("window.scrollTo(0, 1600);")
    ingredients = get_text_by_xpath('//*[@id="block-wellness-content"]/div/section[3]/div/div[1]/p[1]')
    driver.execute_script("window.scrollTo(0, 2200);")
    driver.execute_script("document.querySelectorAll('table').forEach(t => t.setAttribute('style','display:block;'));")
    analysis = get_text_by_xpath('//*[@id="tableWrapperWrapper"]/div[1]/table/tbody/tr')
    driver.execute_script("window.scrollTo(0, 3400);")
    calorie = get_text_by_xpath('//*[@id="block-wellness-content"]/div/section[3]/div/div[3]/p[4]')
    product = {
        "url": url,
        "title": title,
        "descriptions": descriptions,
        "key_benefits": key_benefits,
        "ingredients": ingredients,
        "analysis": analysis,
        "calorie": calorie
    }
    print(product)
    Wellness.append(product)
driver.quit()
output_file = open("./data/Wellness.json", mode="w", newline="", encoding="utf-8")
json.dump(obj=Wellness, fp=output_file, indent=3, ensure_ascii=False)
output_file.close()


input_file = open('./data/Wellness.json', mode='r', newline='', encoding='utf-8')
Wellness = json.load(input_file)
for formula in Wellness:
    if not formula['calorie']:
        formula['calorie'] = formula['analysis'].pop()
    print(formula)
output_file = open("./data/Wellness_.json", mode="w", encoding="utf-8")
json.dump(Wellness, output_file, indent=4, ensure_ascii=False)
input_file.close()
output_file.close()
