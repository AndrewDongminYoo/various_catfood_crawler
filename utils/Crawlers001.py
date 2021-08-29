import json

from selenium import webdriver

from utils.objective_scraper import WebScrapper

# atg_scrapper = WebScrapper("Against The Grain")
# atg_scrapper.crawl(
#     DESC_PATH='//*[@id="post-989"]/div/ul[1]',
#     BENEFIT_PATH='//*[@id="post-989"]/div/ul[2]/li',
#     INGREDIENTS='//*[@id="post-989"]/div/p[5]',
#     ANALYSIS='//*[@id="wp-table-reloaded-id-19-no-1"]/tbody/tr',
#     CALORIE_CONTENT='//*[@id="wp-table-reloaded-id-19-no-1"]/tbody/tr[11]',
# )
# atg_scrapper.save()

# fus_scrapper = WebScrapper("Cardinal Fussie Cat")
# fus_scrapper.crawl(
#     DESC_PATH='/html/body/div[2]/div/div/section[1]/div/div/div[1]/div/div/div[2]/div/div/p',
#     BENEFIT_PATH='/html/body/div[2]/div/div/section[2]/div/div/div/div/div/div[2]/div/div',
#     INGREDIENTS='/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[2]/div/div',
#     ANALYSIS='/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[5]/div/div',
#     CALORIE_CONTENT='/html/body/div[2]/div/div/section[4]/div/div/div[2]/div/div/div[5]/div/div',
# )
# fus_scrapper.save()

# for_scrapper = WebScrapper("Forza10 USA")
# for_script = """
# document.querySelectorAll('.tabcontent').forEach(e=>e.classList.add('opened'));"""
# for_scrapper.crawl(
#     DESC_PATH='//*[@id="ProductSection-product-template"]/div/div[3]/div/div[3]/div',
#     BENEFIT_PATH='//*[@id="tab__Scientific-Studies"]',
#     INGREDIENTS='//*[@id="tab__Nutritional-Info"]/div/p[2]',
#     ANALYSIS='//*[@id="tab__Nutritional-Info"]/div/p[5]',
#     CALORIE_CONTENT='//*[@id="tab__Nutritional-Info"]/div/p[3]',
#     JAVASCRIPT=for_script
# )
# for_scrapper.save()

# koo_scrapper = WebScrapper("KOOKUT")
# koo_scrapper.index_number = 2
# koo_scrapper.crawl(
#     DESC_PATH='//*[@id="ProductSection-product-template"]/div/div[2]/div[3]/div[3]/div/div/div/div/p',
#     BENEFIT_PATH='//*[@id="ProductSection-product-template"]/div/div[2]/div/div/strong',
#     INGREDIENTS='//*[@id="ProductSection-product-template"]/div/div[2]/div[3]/div[3]/div/div/div/div/p[5]',
#     ANALYSIS='//*[@id="ProductSection-product-template"]/div/div[2]/div[3]/div[3]/div/div/div/div/p[6]',
#     CALORIE_CONTENT='//*[@id="ProductSection-product-template"]/div/div[2]/div[3]/div[3]/div/div/div/div/p[7]',
# )
# koo_scrapper.save()

# meo_scrapper = WebScrapper("MeowMix")
# meo_scrapper.index_number = 4
# meo_script = """
# document.querySelectorAll(".tab-pane").forEach(e=>e.classList.add('active'));
# """
# meo_scrapper.crawl(
#     DESC_PATH='//*[@id="tab-description-0"]/div/div[1]/p',
#     BENEFIT_PATH='//*[@id="tab-description-0"]/div/div[2]/ul/li',
#     INGREDIENTS='//*[@id="tab-nutrition-collapse-0"]/div/div[1]/p',
#     ANALYSIS='//*[@id="tab-nutrition-collapse-0"]/div/div[2]/div[1]/div/div',
#     CALORIE_CONTENT='//*[@id="tab-nutrition-collapse-0"]/div/div[2]/div[2]/p',
#     JAVASCRIPT=meo_script
# )
# meo_scrapper.save()

# zwp_scrapper = WebScrapper("ZiwiPeak")
# ziwi_script = """
# document.querySelectorAll("#quickset-tabs_air_dried_and_canned_no_ta > div > div.view.view-pdp-2019-page-elements.view-id-pdp_2019_page_elements.resp-tab-content").forEach(e=> e.style='display:block');
# """
# zwp_scrapper.crawl(
#     DESC_PATH='//*[@id="pdp-panels"]/div[2]/div[2]/div[3]/div/div/p[1]',
#     BENEFIT_PATH='//*[@id="quickset-tabs_air_dried_and_canned_no_ta"]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[3]',
#     INGREDIENTS='//*[@id="quickset-tabs_air_dried_and_canned_no_ta"]/div/div[2]/div/div/div/div/div/div[2]',
#     ANALYSIS='//*[@id="quickset-tabs_air_dried_and_canned_no_ta"]/div/div[3]/div[2]/div/div/div',
#     JAVASCRIPT=ziwi_script
# )
# zwp_scrapper.save()