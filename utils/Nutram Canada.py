import json

from objective_scraper import WebScrapper

scrapper = WebScrapper('Nutram Canada')
# scrapper.crawl(
#     INGREDIENTS='/html/body/div[3]/div/div[1]/p[13]',
#     ANALYSIS='/html/body/div[3]/div/div[1]/div[5]/div[2]/div',
#     BENEFIT_PATH='/html/body/div[3]/div/div[1]/ul',
#     DESC_PATH='/html/body/div[3]/div/div[1]/p[1]',
#     CALORIE_CONTENT='/html/body/div[3]/div/div[1]/div[4]/div[1]/p'
# )
# scrapper.save()

driver = scrapper.driver
with open("data/Nutram Canada.json", mode="r", encoding="utf8", newline="") as input_file:
    Nutram = json.load(input_file)
for formula in Nutram:
    if not formula['ingredients']:
        driver.get(formula['url'])
        scrapper.extract_text('/html/body/div[3]/div/div[1]/p[12]')
with open("./data/Nutram.json", mode="w", newline="", encoding="utf-8") as output_file:
    json.dump(obj=Nutram, fp=output_file, indent=4, ensure_ascii=False)
    driver.quit()
