from selenium import webdriver
from selenium.common.exceptions import JavascriptException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time

Nutro_url_list = result["Nutro Natural Choice"]
driver = webdriver.Chrome()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, timeout=7)
Nutro = []
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


for url in Nutro_url_list:
    driver.get(url)
    time.sleep(3)
    driver.execute_script("""
            document.querySelector("#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(1) > div > div > dl:nth-child(2) > dt").className = "active";
            let ingr = document.querySelectorAll("#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(2) > div > ul > li")
            for (let i=0; i<ingr.length;i++) {
                ingr[i].className = "";
            }
            """)
    driver.execute_script("window.scrollTo(0, 200);")
    title = get_text_by_xpath('//*[@id="product"]/section[1]/div/div/div/ol/li[4]/span')
    descriptions = get_text_by_xpath('//*[@id="product"]/section[3]/div/div/div[1]/section[1]/div/div[1]/div/div/dl[1]/dd/span/p[1]')
    driver.execute_script("window.scrollTo(0, 800);")
    ingredients = get_text_by_xpath('//*[@id="product"]/section[3]/div/div/div[1]/section[1]/div/div[2]/div/ul/li')
    driver.execute_script("window.scrollTo(0, 1300);")
    analysis = get_text_by_xpath('//*[@id="product"]/section[3]/div/div/div[1]/section[1]/div/div[1]/div/div/dl[2]/dd/div/table/tbody/tr')
    driver.execute_script("window.scrollTo(0, 3400);")
    calorie = get_text_by_xpath('//*[@id="product"]/section[3]/div/div/div[1]/section[2]/div/div[2]/div[3]/div/p[4]')
    product = {
        "url": url,
        "title": title,
        "descriptions": descriptions,
        "ingredients": ingredients,
        "analysis": analysis
    }
    print(product)
    Nutro.append(product)
    # except NoSuchElementException:
    #     driver.quit()
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(5)
driver.quit()
output_file = open("./data/Nutro.json", mode="w", newline="", encoding="utf-8")
json.dump(obj=Nutro, fp=output_file, indent=3, ensure_ascii=False)
output_file.close()