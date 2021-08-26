import json

from objective_scraper import WebScrapper

script = """
document.querySelectorAll(
"body > div.main-container > div.container.product-info-ctn > div:nth-child(3) > div.col-md-7.offset-lg-1 > div.features-details-ctn > div.product-details-ctn > div > div")
.forEach(e => e.setAttribute('style','height: 900px;'));
"""
scrapper = WebScrapper("Nutrience")
# scrapper.index_number = 3
# scrapper.crawl(
#     DESC_PATH='/html/body/div[5]/div[2]/div[3]/div[2]/div[3]/p[1]',
#     BENEFIT_PATH='/html/body/div[5]/div[2]/div[3]/div[2]/div[4]/div[@class="product-icons-section__content"]',
#     INGREDIENTS='/html/body/div[5]/div[2]/div[3]/div[2]/div[6]/div[2]/div[1]/div[@class="inner"]',
#     ANALYSIS='//*[@id="analysis-table"]/tbody/tr',
#     CALORIE_CONTENT='/html/body/div[5]/div[2]/div[3]/div[2]/div[6]/div[2]/div[2]/div/div/p[3]',
#     JAVASCRIPT=script
# )
# scrapper.save()

driver = scrapper.driver

with open("data/Nutrience.json", mode="r", encoding="utf8", newline="") as input_file:
    Nutrience = json.load(input_file)
for formula in Nutrience:
    for key, value in formula.items():
        if not value:
            driver.get(formula['url'])
            driver.execute_script(script)
            formula[key] = input(f'"{key}" =>')
with open("./data/Nutrience.json", mode="w", newline="", encoding="utf-8") as output_file:
    json.dump(obj=Nutrience, fp=output_file, indent=4, ensure_ascii=False)
    driver.quit()
