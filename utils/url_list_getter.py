from objective_scraper import WebScrapper
import csv

scraper = WebScrapper()
driver = scraper.driver

input_file = open("./data/0005.csv", mode="r", encoding="ansi", newline="")
output_file = open("./data/0006.csv", mode="a", encoding="ansi", newline="")
reader = csv.reader(input_file, dialect="excel")
writer = csv.writer(output_file, dialect="excel")
new_url = ""
for line in reader:
    [brand, url] = line
    url_list = []
    driver.get(url)
    while True:
        new_url = input(f'"{brand}" =>\n')
        if new_url == ".":
            break
        elif new_url == "exit":
            driver.quit()
            input_file.close()
            output_file.close()
            brand = ""
            break
        else:
            url_list.append(new_url.strip())
    if brand == "":
        break
    row = [brand, ""]
    row.extend(url_list)
    writer.writerow(row)
driver.quit()
input_file.close()
output_file.close()
