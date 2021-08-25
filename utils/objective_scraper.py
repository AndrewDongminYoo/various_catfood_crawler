from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from import_csv import result
import json
import time


class WebScrapper:
    options = Options()
    options.add_argument("--window-size=1545,1047")
    options.add_argument("--window-position=0,0")
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    driver.implicitly_wait(10)
    driver.minimize_window()
    scroll_down = "window.scrollBy(0,2000);"
    index_number = 0

    def __init__(self, brand_name):
        """
        :param brand_name: BRAND_NAME_FOR_NAME_RESULT
        """
        self.brand_name = brand_name
        self.url_list = result[brand_name]
        self.type_of_selector = "XPATH"
        self.index_number += 1
        self.result_list = []

    def save(self):
        self.driver.quit()
        with open(f"./data/{str(self.index_number).zfill(4)}_{self.brand_name}.json",
                  mode="w", encoding="utf-8", newline="") as output_file:
            json.dump(obj=self.result_list, fp=output_file, indent=4, ensure_ascii=False)

    def execute(self, script: str, *args):
        return self.driver.execute_script(script=script, *args)

    def set_attr(self, element_id: str, attr_to_on: str):
        self.execute(f"document.getElementById('{element_id}').setAttribute('{attr_to_on}','true');")

    def scroll_infinite(self):
        scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
        get_window_height = "return document.body.scrollHeight"
        last_height = self.execute(get_window_height)
        while True:
            self.execute(scroll_to_bottom)
            time.sleep(3)
            new_height = self.execute(get_window_height)
            if new_height == last_height:
                break
            last_height = new_height

    def activate_class(self, element_id: str, show_class: str):
        return self.execute(f"document.getElementById('{element_id}').classList.add('{show_class}');")

    def activate_class_by_selector(self, selector: str, show_class: str):
        return self.execute(f"document.querySelector('{selector}').classList.add('{show_class}');")

    def scroll_to(self, element: WebElement):
        return self.execute("arguments[0].scrollIntoView();", element)

    def click_element(self, selector):
        return self.execute(f"document.querySelector('{selector}').click().scrollIntoViewIfNeeded();")

    def get_text_by_xpath(self, xpath):
        result_list = []
        targets = self.driver.find_elements(By.XPATH, xpath)
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

    def get_text_by_css(self, css):
        result_list = []
        targets = self.driver.find_elements(By.CSS_SELECTOR, css)
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

    def extract_text(self, SELECTOR):
        if self.type_of_selector == "XPATH":
            return self.get_text_by_xpath(SELECTOR)
        else:
            return self.get_text_by_css(SELECTOR)

    def crawl(self,
              TITLE_PATH='',
              DESC_PATH='',
              BENEFIT_PATH='',
              INGREDIENTS='',
              ANALYSIS='',
              ADDITIVES='',
              CALORIE_CONTENT='',
              hidden_elements='',
              deactivated_elem='',
              activate_class='',
              JAVASCRIPT=''
              ):
        for url in self.url_list:
            product = {'brand': self.brand_name}
            self.driver.get(url)
            time.sleep(2)
            # if hidden_elements:
            #     self.execute(f"document.querySelectorAll('{hidden_elements}').forEach(e => e.setAttribute('style',"
            #                  f"'display:block;'));")
            # if deactivated_elem:
            #     self.activate_class_by_selector(deactivated_elem, activate_class)
            if TITLE_PATH:
                product['title'] = self.extract_text(TITLE_PATH)
                self.execute('window.scrollBy(0,200);')
            else:
                product['title'] = self.driver.title
            self.execute(JAVASCRIPT)
            if DESC_PATH:
                product['descriptions'] = self.extract_text(DESC_PATH)
                self.execute('window.scrollBy(0,200);')
            if BENEFIT_PATH:
                product['key_benefits'] = self.extract_text(BENEFIT_PATH)
                self.execute('window.scrollBy(0,200);')
            if INGREDIENTS:
                product['ingredients'] = self.extract_text(INGREDIENTS)
                self.execute('window.scrollBy(0,200);')
            if ANALYSIS:
                product['analysis'] = self.extract_text(ANALYSIS)
                self.execute('window.scrollBy(0,200);')
            if ADDITIVES:
                product['additive'] = self.extract_text(ADDITIVES)
                self.execute('window.scrollBy(0,200);')
            if CALORIE_CONTENT:
                product['calorie'] = self.extract_text(CALORIE_CONTENT)
            print(product)
            self.result_list.append(product)
