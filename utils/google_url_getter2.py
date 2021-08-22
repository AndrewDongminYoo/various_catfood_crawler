from selenium import webdriver
import csv
from urllib import parse
import time

driver = webdriver.Chrome()
driver.set_window_size(width=1600, height=900)
driver.implicitly_wait(5)

with open("./data/0004.csv", mode="r", encoding="ansi", newline="",) as input_file:
    with open("./data/0005.csv", mode="w", encoding="ansi", newline="") as output_file:
        reader = csv.reader(input_file, dialect="excel")
        writer = csv.writer(output_file, dialect="excel")
        new_url = ""
        for lines in reader:
            [brand, url] = lines
            if url == "url" or brand == "" or "http" in url:
                brand = brand
                new_url = url
            elif url == "":
                driver.get("https://www.google.com/search?q=" + brand.replace(" ", "+") + "+cat+food")
                is_ok = input(f'{brand} "url?" ')
                new_url = driver.current_url
            else:
                driver.get("https://" + url)
                is_ok = input(f'{brand} "url?" ')
                new_url = driver.current_url
            print(new_url)
            row = [brand, new_url]
            writer.writerow(row)
