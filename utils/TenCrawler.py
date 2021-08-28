from objective_scraper import WebScrapper
import json
from selenium import webdriver

# bwd_scrapper = WebScrapper("Blackwood Pet Food")
# print(bwd_scrapper.url_list[0])
# bwd_script = """
# document.querySelectorAll("#main > div.product-tabs > div > div.tabs > div.tab").forEach(e=>e.classList.add('active'));
# """
# bwd_scrapper.crawl(
#     DESC_PATH='//*[@id="main"]/div[2]/div[2]/div[3]/ul/li',
#     BENEFIT_PATH='//*[@id="main"]/div[2]/div[2]/div[4]/div',
#     INGREDIENTS='//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]/div',
#     ANALYSIS='//*[@id="main"]/div[3]/div/div[2]/div[2]/table/tbody/tr',
#     CALORIE_CONTENT='//*[@id="main"]/div[3]/div/div[2]/div[2]/table/tbody/tr[last()]',
#     JAVASCRIPT=bwd_script,
# )
# bwd_scrapper.save()
#
# k9_scrapper = WebScrapper("Feline Natural")
# print(k9_scrapper.url_list[0])
# k9_script = """
# document.querySelectorAll("div.accordion-content").forEach(e => e.classList.add('open-content'));
# document.querySelectorAll("div.accordion-content").forEach(e => e.setAttribute('style','display:block'));
# """
# k9_scrapper.crawl(
#     DESC_PATH='//*[@id="shopify-section-product-template"]/div/section[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/p[1]',
#     BENEFIT_PATH='//*[@id="accordion-container"]/div[2]/div/ul/li',
#     INGREDIENTS='//*[@id="accordion-container"]/div[4]/div/p',
#     ANALYSIS='//*[@id="accordion-container"]/div[6]/div/table/tbody/tr/td/p',
#     CALORIE_CONTENT='//*[@id="accordion-container"]/div[6]/div/table/tbody/tr/td[1]/p[last()]',
#     JAVASCRIPT=k9_script,
# )
# k9_scrapper.save()
#
# gos_scrapper = WebScrapper("Gosbi")
# print(gos_scrapper.url_list[0])
# gos_scrapper.crawl(
#     DESC_PATH='/html/body/main/article/div[2]/div[2]/div[2]/p'
# )
# gos_scrapper.save()
#
# leo_scrapper = WebScrapper("Leonardo Catfood")
# print(leo_scrapper.url_list[0])
# leo_script = """
# document.querySelectorAll(".tab-pane.fade").forEach(e=>{
#     e.classList.add('active');
#     e.classList.add('show');
# });
# """
# leo_scrapper.crawl(
#     DESC_PATH='/html/body/main/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/p[2]',
#     BENEFIT_PATH='/html/body/main/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/ul/li',
#     INGREDIENTS='//*[@id="analyse-tab-pane"]/div/div/div[2]/div/div[1]/p',
#     ANALYSIS='//*[@id="analyse-tab-pane"]/div/div/div[2]/div/div[2]/p',
#     ADDITIVES='//*[@id="analyse-tab-pane"]/div/div/div[2]/div/div[3]/p[contains(text(),"mg")]',
#     JAVASCRIPT=leo_script,
# )
# leo_scrapper.save()
#
# lot_scrapper = WebScrapper("Lotus")
# print(lot_scrapper.url_list[0])
# lot_script = """
# document.querySelectorAll("div.tab-pane").forEach(e=>e.classList.add('active'));
# """
# lot_scrapper.crawl(
#     DESC_PATH='//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[1]/div[4]/div/div/div/ul/li/p',
#     INGREDIENTS='//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[1]/p',
#     ANALYSIS='//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/div/div/div/div/div[1]/div/div[2]/div/ul/li',
#     CALORIE_CONTENT='//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/div/div/div/div/div[3]/div/div[2]/div/ul/li',
#     JAVASCRIPT=lot_script,
# )
# lot_scrapper.save()
#
# mar_scrapper = WebScrapper("Maria Pet Food")
# print(mar_scrapper.url_list[0])
# mar_scrapper.crawl(
#     DESC_PATH='/html/body/app-root/app-front/div/div/dynamic-components[2]/app-page-product-detail/div[1]/div/div/div[2]/div[3]/div/p[1]/span',
#     INGREDIENTS='/html/body/app-root/app-front/div/div/dynamic-components[2]/app-page-product-detail/div[1]/div/div/div[2]/div[3]/div/p[2]/span',
#     ANALYSIS='/html/body/app-root/app-front/div/div/dynamic-components[2]/app-page-product-detail/div[1]/div/div/div[2]/div[3]/div/ul/li/span'
# )
# mar_scrapper.save()

log_scrapper = WebScrapper("Nature's Logic")
print(log_scrapper.url_list[0])
log_scrapper.crawl(
    DESC_PATH='//*[@id="after_submenu"]/div/div/div/div/div[2]/section/div/p[1]',
    BENEFIT_PATH='//*[@id="av-layout-grid-2"]/div/div/div[6]/section/div/h4',
    INGREDIENTS='/html/body/div[2]/div/div[6]/div/div/div/section/div/h4',
    ANALYSIS='/html/body/div[2]/div/div[9]/div/div[3]/div[2]/div/div/section/div/table/tbody/tr',
    ADDITIVES='//div[@id="av-tab-section-1-3" or @id="av-tab-section-1-4"]/div/div/section/div/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="av_section_2"]/div/div/div/div/div[6]/div'
)
log_scrapper.save()

nut_scrapper = WebScrapper("Nutro")
print(nut_scrapper.url_list[0])
nut_scrapper.crawl(
    DESC_PATH='/html/body/main/section[1]/div/div[2]/div/div[2]/p[1]',
    BENEFIT_PATH='/html/body/main/section[2]/div/div/div[1]/div',
    INGREDIENTS='/html/body/main/section[3]/div/div/div[1]/div/p',
    ANALYSIS='/html/body/main/section[3]/div/div/div[2]/div/table/tbody/tr',
    CALORIE_CONTENT='/html/body/main/section[5]/div/div/div[2]/div/p[10]'
)
nut_scrapper.save()

fel_scrapper = WebScrapper("Terra Fellis")
print(fel_scrapper.url_list[0])
fel_script = """
document.querySelectorAll(".tab-pane").forEach(e=>{
    e.classList.add('active');
    e.classList.add('show');
})
"""
fel_scrapper.crawl(
    DESC_PATH='/html/body/main/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/ul/li',
    BENEFIT_PATH='/html/body/main/div[2]/div/div/div/div/div[2]/div/div/div/p',
    INGREDIENTS='//*[@id="description-tab-pane"]/div/div[1]/div/div/div/div[2]/p[1]',
    ANALYSIS='//*[@id="analytical-components-tab-pane"]/div/div/div/div/p',
    ADDITIVES='//*[@id="analytical-components-tab-pane"]/div/div/div/div/div',
    JAVASCRIPT=fel_script
)
fel_scrapper.save()

brand_list = ["Blackwood Pet Food", "Feline Natural", "Gosbi", "Leonardo Catfood",
              "Lotus", "Maria Pet Food", "Nature's Logic", "Nutro", "Terra Fellis"]
# driver = webdriver.Chrome()
# for brand in brand_list:
#     with open(file=f"./data/{brand}.json", mode="r", encoding="UTF-8", newline="") as input_file:
#         formulas = json.load(input_file)
#         for formula in formulas:
#             for key, value in formula.items():
#                 if not value:
#                     driver.get(formula['url'])
#                     formula[key] = input(f'"{key}" => // ')
#     with open(file=f"./data/{brand}_.json", mode="w", encoding="UTF-8", newline="") as output_file:
#         json.dump(formulas, output_file, indent=4, ensure_ascii=False, allow_nan=True)
