from selenium import webdriver
from selenium.webdriver.common.by import By
import json

evolve_url_list = [
    "https://evolvepetfood.com/dry-cat-food/evolve-classic-chicken-amp-brown-rice-recipe-xck8w",
    "https://evolvepetfood.com/dry-cat-food/evolve-classic-salmon-rice-amp-sweet-potato-recipe-hlmlh",
    "https://evolvepetfood.com/dry-cat-food/evolve-grain-free-chicken-amp-chickpea-recipe-p6jkx",
    "https://evolvepetfood.com/dry-cat-food/evolve-grain-free-ocean-whitefish-amp-egg-recipe-cat-food-deklj",
    "https://evolvepetfood.com/dry-cat-food/evolve-grain-free-kitten-food-7gfjn"]
driver = webdriver.Chrome()
driver.implicitly_wait(5)
evolve = []


def get_text_by_xpath(xpath):
    result_list = []
    targets = driver.find_elements(By.XPATH, xpath)
    if len(targets) == 1:
        return targets[0].text
    for t in targets:
        result_list.append(t.text)
    return result_list


for url in evolve_url_list:
    driver.get(url)
    title = get_text_by_xpath('//article/section[1]/section[2]/h1')
    descriptions = get_text_by_xpath('//article/section[1]/section[2]/div[2]/p[1]')
    ingredients = get_text_by_xpath('//article/section[1]/section[2]/div[2]/p[2]')
    analysis = get_text_by_xpath('//article/section[1]/section[2]/div[2]/p[3]')
    calorie = get_text_by_xpath('//article/section[1]/section[2]/div[2]/p[6]')
    product = {
        "title": title,
        "descriptions": descriptions,
        "ingredients": ingredients,
        "analysis": analysis,
        "calorie": calorie
    }
    evolve.append(product)
driver.quit()
input_file = open("./data/Evolve.json", mode="w", newline="", encoding="utf-8")
json.dump(obj=evolve, fp=input_file, indent=3, ensure_ascii=False)
input_file.close()