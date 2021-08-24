from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Hills_url_list = result["Hill's Science Diet"]
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=7)
Hills = []
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


for url in Hills_url_list:
    driver.get(url)
    time.sleep(5)
    driver.execute_script("""
            let lis = document.querySelectorAll("#content > div > div > div > div > div.accordion.component.section.accordion-product-detail.odd.col-xs-12.initialized > div > ul > li.accordion-slide > header > h3");
            for (i=0;i<lis.length;i++) {
                lis[i].click();
            };
            """)
    title = driver.title
    time.sleep(5)
    key_benefits = get_text_by_xpath('//*[@id="406762222"]/div/div[6]/div/div/p[2]')
    driver.execute_script("window.scrollTo(0, 750);")
    descriptions = get_text_by_xpath('//*[@id="0561100104"]/div/div[2]/div/div/p')
    driver.execute_script("window.scrollTo(0, 1400);")
    ingredients = get_text_by_xpath('//*[@id="2073436235"]/div/div[1]/div/div/p')
    driver.execute_script("window.scrollTo(0, 1900);")
    calorie = get_text_by_xpath('//*[@id="2084752362"]/div/div[1]/div/div/h6')
    driver.execute_script("window.scrollTo(0, 2400);")
    analysis = get_text_by_xpath('//*[@id="2084752362"]/div/div[2]/div/div/div/table/tbody/tr')
    product = {
        "url": url,
        "title": title,
        "key_benefits": key_benefits,
        "descriptions": descriptions,
        "ingredients": ingredients,
        "analysis": analysis
    }
    print(product)
    Hills.append(product)
driver.quit()
output_file = open("./data/Hills.json", mode="w", newline="", encoding="utf-8")
json.dump(obj=Hills, fp=output_file, indent=3, ensure_ascii=False)
output_file.close()