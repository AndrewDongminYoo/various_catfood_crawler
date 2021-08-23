from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time
import json


class WebScrapper:
    options = Options()
    options.add_argument("--window-size=1545,1047")
    options.add_argument("--window-position=0,0")
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    scroll_down = "window.scrollBy(0,2000);"
    index_number = 0

    def __init__(self,
                 brand_name: str,
                 url_list: list,
                 type_of_selector: str
                 ):
        """
        :param brand_name: BRAND_NAME_FOR_NAME_RESULT
        :param url_list: URL_LIST_FOR_ITERATE
        :param type_of_selector: XPATH or CSS_SELECTOR
        """
        self.brand_name = brand_name
        self.url_list = url_list
        self.type_of_selector = type_of_selector
        self.index_number += 1
        self.result_list = []

    def esc(self):
        output_file = open(f"./data/{str(self.index_number).zfill(4)}_{self.brand_name}.json",
                           mode="w", encoding="utf-8", newline="")
        json.dump(obj=self.result_list, fp=output_file, indent=3, ensure_ascii=False, allow_nan=False)

    def js(self, script: str, *args):
        return self.driver.execute_script(script=script, *args)

    def set_attr(self, element_id: str, attr_to_on: str):
        self.js(f"document.getElementById('{element_id}').setAttribute('{attr_to_on}','true');")

    def scroll_infinite(self):
        scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
        get_window_height = "return document.body.scrollHeight"
        last_height = self.js(get_window_height)
        while True:
            self.js(scroll_to_bottom)
            time.sleep(3)
            new_height = self.js(get_window_height)
            if new_height == last_height:
                break
            last_height = new_height

    def activate_class(self, element_id: str, show_class: str):
        return self.js(f"document.getElementById('{element_id}').classList.add('{show_class}');")

    def activate_class_by_selector(self, selector: str, show_class: str):
        return self.js(f"document.querySelector('{selector}').classList.add('{show_class}');")

    def scroll_to(self, element: WebElement):
        return self.js("arguments[0].scrollIntoView();", element)

    def click_element(self, selector):
        return self.js(f"document.querySelector('{selector}').click().scrollIntoViewIfNeeded();")

    def select(self, selector):
        target_list = []
        if self.type_of_selector == "XPATH":
            target_list = self.driver.find_elements(By.XPATH, selector)
        else:
            target_list = self.driver.find_elements(By.CSS_SELECTOR, selector)



    def crawl(self, title, desc, key_bene, ing, anal, add, cal):
        for url in self.url_list:
            self.driver.get(url)
            title = self.select_one(title).text
            key_benefit_list = []
            key_benefits = self.select(key_bene)
            for key in key_benefits:
                key_benefit_list.append(key.text)
            descriptions = self.select_one(desc).text
            ingredients = self.select_one(ing).text
            analysis_list = []
            analysis_tags = self.select(anal)
            for ana in analysis_tags:
                analysis_list.append(ana.text)
            additive = self.select_one(add).text
            calorie = self.select_one(cal).text
            dictionary = {
                "title": title,
                "key_benefits": key_benefit_list,
                "description": descriptions,
                "ingredients": ingredients,
                "analysis": analysis_list,
                "additive": additive,
                "calorie": calorie
            }
            self.result_list.append(dictionary)
        self.esc()
