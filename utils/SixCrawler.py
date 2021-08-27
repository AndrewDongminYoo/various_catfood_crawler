from objective_scraper import WebScrapper

# soup_scrapper = WebScrapper("Chicken Soup for the Soul")
# print(soup_scrapper.url_list[0])
# soup_scrapper.crawl(
#     BENEFIT_PATH='/html/body/div/div[2]/div/div[2]/main/section/div/section/article/div[1]/div[2]/div[4]/div/div/div/ul/li',
#     INGREDIENTS='/html/body/div/div[2]/div/div[2]/main/section/div/section/article/div[2]/div[2]/div/div/p[1]',
#     ANALYSIS='/html/body/div/div[2]/div/div[2]/main/section/div/section/article/div[2]/div[3]/div/div/table/tbody/tr',
#     CALORIE_CONTENT='/html/body/div/div[2]/div/div[2]/main/section/div/section/article/div[2]/div[4]/div/div/p[1]'
# )
# soup_scrapper.save()
#
# mer_scrapper = WebScrapper("Merrick")
# print(mer_scrapper.url_list[0])
# mer_scrapper.crawl(
#     DESC_PATH='//*[@id="componentProductDetail"]/div/div[1]/div[2]/div[3]',
#     BENEFIT_PATH='//*[@id="componentProductDetail"]/div/div[1]/div[2]/div[3]/ul/li',
#     INGREDIENTS='//*[@id="ingredients"]/p',
#     ANALYSIS='//*[@id="guaranteed-analysis"]/div/div[1]/div',
#     CALORIE_CONTENT='//*[@id="feeding-guide"]/div[2]/div[2]/p[2]'
# )
# mer_scrapper.save()
#
# src_scrapper = WebScrapper("NutriSource")
# print(src_scrapper.url_list[0])
# src_scrapper.crawl(
#     DESC_PATH='//*[@id="et-boc"]/div/div/div[2]/div/div[2]/div[4]/div/ul/li',
#     BENEFIT_PATH='//*[@id="et-boc"]/div/div/div[2]/div/div[1]/div[3]/div/div/div',
#     INGREDIENTS='//*[@id="ingredients-nutrition"]/div[2]/div[1]/div[1]/div/p[1]',
#     ANALYSIS='//*[@id="ingredients-nutrition"]/div[2]/div[1]/div[2]/div/table/tbody/tr',
#     CALORIE_CONTENT='//*[@id="ingredients-nutrition"]/div[2]/div[2]/div/div/table/tbody/tr'
# )
# src_scrapper.save()
#
# org_scrapper = WebScrapper("Organix")
# print(org_scrapper.url_list[0])
# org_scrapper.crawl(
#     DESC_PATH='//*[@id="feedingGuideContentContainer"]/div/div/label/p[3]',
#     BENEFIT_PATH='//*[@id="firstFive"]/ul/li',
#     INGREDIENTS='//*[@id="ingredientsContentContainer"]/div/p[1]',
#     ANALYSIS='//*[@id="analysisContentContainer"]/div/div/table/tr',
#     CALORIE_CONTENT='//*[@id="feedingGuideContentContainer"]/div/div/label/p[6]',
# )
# org_scrapper.save()

thr_scrapper = WebScrapper("Thrive complete")
print(thr_scrapper.url_list[0])
thr_script = """
document.querySelectorAll(".proptions").forEach(e => e.classList.add('active'));
"""
thr_scrapper.crawl(
    DESC_PATH='//*[@id="po1"]/p',
    BENEFIT_PATH='//*[@id="po1"]/ul/li',
    INGREDIENTS='//*[@id="po2"]',
    ANALYSIS='//*[@id="po3"]',
    JAVASCRIPT=thr_script
)
thr_scrapper.save()


wer_scrapper = WebScrapper("Weruva Catfood")
print(wer_scrapper.url_list[0])
wer_scrapper.crawl(
    DESC_PATH='//*[@id="main"]/div[2]/div/div[1]/div[2]/div/div[3]',
    INGREDIENTS='//*[@id="nutritionDetailInfo"]/div/div[3]/div[1]/p[2]',
    ANALYSIS='//*[@id="nutritionDetailInfo"]/div/div[1]/div[2]/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="nutritionDetailInfo"]/div/div[1]/div[1]/table/tbody/tr'
)
wer_scrapper.save()

opt_scrapper = WebScrapper("Optimanova")
print(opt_scrapper.url_list[0])
opt_script = """
document.querySelectorAll('.info').forEach(e => e.setAttribute('style','display:block;'));
"""
opt_scrapper.crawl(
    DESC_PATH='//*[@id="bodycontent"]/section[1]/div/div/div[2]/p',
    BENEFIT_PATH='//*[@id="contenido-2"]/div/div/div[2]/div[2]/div[1]/ul/li',
    INGREDIENTS='//*[@id="contenido-2"]/div/div/div[2]/div[2]/div[2]/div[2]',
    ANALYSIS='//*[@id="contenido-2"]/div/div/div[2]/div[2]/div[3]/div[2]',
    ADDITIVES='//*[@id="contenido-2"]/div/div/div[2]/div[2]/div[4]/div[2]',
    JAVASCRIPT=opt_script
)
opt_scrapper.save()

raw_scrapper = WebScrapper("Rawz")
print(raw_scrapper.url_list[0])
raw_script = """

"""
raw_scrapper.crawl(
    DESC_PATH='//*[@id="product-layout-cta-0"]/div/div[2]',
    BENEFIT_PATH='//*[@id="our-recipe"]/div[2]/div[1]/ul/li',
    INGREDIENTS='//*[@id="our-recipe"]/div[2]/div[2]/div',
    ANALYSIS='//*[@id="guaranteed-analysis"]/div/div/div/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="transitioning-to-rawz"]/div/div[2]/p[3]',
    JAVASCRIPT=raw_script
)
raw_scrapper.save()

tro_scrapper = WebScrapper("TROVET")
print(tro_scrapper.url_list[0])
tro_scrapper.crawl(
    DESC_PATH='/html/body/div[5]/div/div[1]/div[5]/p',
    BENEFIT_PATH='/html/body/div[5]/div/div[1]/ul[2]/li',
    INGREDIENTS='/html/body/div[5]/div/div[1]/div[19]/p',
    ANALYSIS='//*[@id="productvorm-Dry"]/div[4]/div',
    CALORIE_CONTENT='/html/body/div[5]/div/div[1]/div[19]'
)
tro_scrapper.save()
