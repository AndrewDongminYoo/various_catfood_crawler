from openpyxl import Workbook
from selenium import webdriver
import csv


class ExcelMaker:
    def __init__(self, name, mainpage):
        self._name = name
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(12)
        self.driver.get(mainpage)
        self.csv_file = open(
            f'./output/{self._name}_scrap.csv', 'w', newline="")
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(
            ['name', 'one_price', 'box_price', 'box_count', 'type', 'img_src'])

    def mall_scraper(self,
                     product_name_tag,
                     price_of_one_tag,
                     price_of_box_tag,
                     box_bundle_count,
                     wet_or_dry_foods,
                     image_source_src,
                     next_page_loader):
        pass
