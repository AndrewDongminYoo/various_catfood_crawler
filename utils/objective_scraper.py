from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class WebScrapper:
    options = Options()
    options.add_argument("--window-size=1545,1047")
    options.add_argument("--window-position=0,0")
    driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    scroll_down = "window.scrollBy(0,2000);"

    def js(self, script, *args):
        return self.driver.execute_script(script=script, *args)

    def set_attr(self, element_id, attr_to_on):
        self.js(f"document.getElementById('{element_id}').setAttribute('{attr_to_on}','true');")

    def scroll_infinite(self):
        scroll_to_bottom = "window.scrollTo(0, document.body.scrollHeight);"
        get_window_height = "return document.body.scrollHeight"
        last_height = self.js(self.get_window_height)
        while True:
            self.js(self.scroll_to_bottom)
            time.sleep(3)
            new_height = self.js(self.get_window_height)
            if new_height == last_height:
                break
            last_height = new_height

    def activate_class(self, element_id, show_class):
        return self.js(f"document.getElementById('{element_id}').classList.add('{show_class}');")

    def activate_class_by_selector(self, selector, show_class):
        return self.js(f"document.querySelector('{selector}').classList.add('{show_class}');")

    def scroll_to(self, element):
        return self.js("arguments[0].scrollIntoView();", element)

    def click_element(self, selector):
        return self.js(f"document.querySelector('{selector}').click().scrollIntoViewIfNeeded();")