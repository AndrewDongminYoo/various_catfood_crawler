from objective_scraper import WebScrapper
from import_csv import result
targets = ['BlackHawk', 'Catz finefood', 'First Choice Canada', 'Monge', "Nature's Protection", 'Sheba', 'SolidGold Petfood', 'Vigor and Sage', 'Vital Essentials']
for target in targets:
    print(result[target][0])


# BlHawk_scrapper = WebScrapper("BlackHawk")
# BlHawk_script = """
# document.querySelectorAll(".ui-tabs-panel").forEach(e=>{
#     e.setAttribute('style','display:block;');
#     e.setAttribute('aria-hidden',false);
# });
# """
# BlHawk_scrapper.crawl(
#     DESC_PATH='/html/body/div[2]/section[2]/div[1]/div[2]/div/p',
#     BENEFIT_PATH='/html/body/div[2]/section[2]/div[2]/div[2]/div[2]/div',
#     INGREDIENTS='//*[@id="tabs-2"]/div/p',
#     ANALYSIS='//*[@id="tabs-3"]/div/table[1]/tbody/tr',
#     CALORIE_CONTENT='//*[@id="tabs-3"]/div/table[1]/tbody/tr[last()]',
#     JAVASCRIPT=BlHawk_script
# )
# BlHawk_scrapper.save()
# fine_scrapper = WebScrapper("Catz finefood")
# fine_scrapper.crawl(
#     DESC_PATH='/html/body/div[1]/section/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/p[2]',
#     INGREDIENTS='/html/body/div[1]/section/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/p[3]',
#     ANALYSIS='/html/body/div[1]/section/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/p[5]/span',
#     ADDITIVES='/html/body/div[1]/section/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/p[6]/span',
#     CALORIE_CONTENT='/html/body/div[1]/section/div/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/p[4]'
# )
# fine_scrapper.save()a
# first_scrapper = WebScrapper("First Choice Canada")
# first_script = """
# document.querySelectorAll("div.accordion__item-content").forEach(e=>e.setAttribute('style','display:block;'));
# """
# first_scrapper.crawl(
#     DESC_PATH='/html/body/section[1]/div/div/div[2]/p',
#     BENEFIT_PATH='/html/body/div[4]/section/div/div/p',
#     INGREDIENTS='/html/body/section[2]/div/div/ul/li[2]/div[2]/p',
#     ANALYSIS='/html/body/section[2]/div/div/ul/li[3]/div[2]/p',
#     CALORIE_CONTENT='/html/body/section[2]/div/div/ul/li[1]/div[2]/div/div[2]/table/tbody/tr[10]/td/div[2]',
#     JAVASCRIPT=first_script
# )
# first_scrapper.save()
# mon_scrapper = WebScrapper("Monge")
# mon_script = """
# document.querySelectorAll(".tab-pane").forEach(e=>{
#     e.classList.add('active');
#     e.classList.add('in');
# });
# """
# mon_scrapper.crawl(
#     DESC_PATH='/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/p[1]',
#     BENEFIT_PATH='/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[2]/div[3]/span/img',
#     INGREDIENTS='/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[5]/div/div[2]/div[1]/p',
#     ANALYSIS='/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[5]/div/div[2]/div[2]/p',
#     ADDITIVES='/html/body/div[1]/div[4]/div/div[1]/div/div[1]/div[5]/div/div[2]/div[3]/p',
#     JAVASCRIPT=mon_script
# )
# mon_scrapper.save()
# protect_scrapper = WebScrapper("Nature's Protection")
# protect_script = """
# document.querySelectorAll("td.content").forEach(e => e.style = 'display: block;');
# """
# protect_scrapper.crawl(
#     DESC_PATH='/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div[4]/table[1]/tbody/tr/td/ul/li/div',
#     BENEFIT_PATH='//*[@id="txt_cont"]/div[2]/div[2]/div[4]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/span',
#     INGREDIENTS='//*[@id="txt_cont"]/div[2]/div[2]/div[4]/div/table/tbody/tr/td[2]/div[1]/div[1]/div/span[2]',
#     ANALYSIS='//*[@id="txt_cont"]/div[2]/div[2]/div[4]/div/table/tbody/tr/td[4]',
#     ADDITIVES='//*[@id="txt_cont"]/div[2]/div[2]/div[4]/div/table/tbody/tr/td[2]/div[1]/div[5]/span[2]',
#     JAVASCRIPT=protect_script
# )
# protect_scrapper.save()
# she_scrapper = WebScrapper("Sheba")
# she_script = """
# document.querySelectorAll('.content').forEach(e=>{
#     document.querySelector("#content > article > div.product-details > div.tab.guidelines").append(e)
# });
# """
# she_scrapper.crawl(
#     DESC_PATH='//*[@id="content"]/article/div[3]/div[1]/div[5]/span[2]',
#     BENEFIT_PATH='//*[@id="content"]/article/div[2]/div[2]',
#     INGREDIENTS='//*[@id="content"]/article/div[3]/div[1]/div[4]',
#     ANALYSIS='//*[@id="content"]/article/div[3]/div[1]/div[2]',
#     CALORIE_CONTENT='//*[@id="content"]/article/div[3]/div[1]/div[3]',
#     JAVASCRIPT=she_script
# )
# she_scrapper.save()
# gold_scrapper = WebScrapper("SolidGold Petfood")
# gold_script = """
# document.querySelectorAll("div.clearfix").forEach(e=>{e.classList.remove('inactive'); e.classList.add('active');});
# """
# gold_scrapper.crawl(
#     DESC_PATH='//*[@id="content"]/div[2]/div/section[1]/div/div/div[2]/div/div/div[4]/div/div/p',
#     INGREDIENTS='/html/body/div[2]/div[1]/div[2]/div/section[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/span',
#     ANALYSIS=
#     '/html/body/div[2]/div[1]/div[2]/div/section[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr',
#     CALORIE_CONTENT='/html/body/main/section[1]/div[3]/div[2]/div[1]',
#     JAVASCRIPT=gold_script
# )
# gold_scrapper.save()
# vigor_scrapper = WebScrapper("Vigor and Sage")
# vigor_script = """
# document.querySelectorAll(".woocommerce-Tabs-panel").forEach(e=>e.classList.add('active'));
# """
# vigor_scrapper.crawl(
#     DESC_PATH='/html/body/div[1]/main/div/div[2]/div/section/div[2]/div/div[2]/div/div[4]//p',
#     BENEFIT_PATH=
#     '/html/body/div[1]/main/div/div[2]/div/section/div[2]/div/div[3]/div/div/div/div[2]/div[12]/div[2]/div/h4',
#     INGREDIENTS=
#     '/html/body/div[1]/main/div/div[2]/div/section/div[2]/div/div[3]/div/div/div/div[3]/table/tbody/tr[1]/td/p[1]',
#     ADDITIVES=
#     '/html/body/div[1]/main/div/div[2]/div/section/div[2]/div/div[3]/div/div/div/div[3]/table/tbody/tr[1]/td/p[2]',
#     ANALYSIS=
#     '/html/body/div[1]/main/div/div[2]/div/section/div[2]/div/div[3]/div/div/div/div[3]/table/tbody/tr[2]/td/p',
#     JAVASCRIPT=vigor_script
# )
# vigor_scrapper.save()
vita_scrapper = WebScrapper("Vital Essentials")
vita_script = """
document.querySelectorAll("div.tab.clearfix").forEach(e=>{
    e.classList.add('active');
    e.style='display: block;';
});
let t = document.querySelector("div.tab.nutrition.clearfix > div:nth-child(1)").innerText;
let regex = /[0-9]+ kcal\/kg/;
calorie = regex.exec(t)[0]
document.querySelector("div.tab.nutrition.clearfix > div:nth-child(1) > h3:nth-child(3)").innerText = calorie;
"""
vita_scrapper.crawl(
    DESC_PATH='/html/body/main/section[1]/div[3]/div[1]/div[1]/div/p[1]',
    BENEFIT_PATH='/html/body/main/section[1]/div[3]/div[1]/div[2]/ul/li',
    INGREDIENTS='/html/body/main/section[1]/div[3]/div[2]/div[1]/p',
    ANALYSIS='/html/body/main/section[1]/div[3]/div[2]/div[2]/table/tbody/tr',
    CALORIE_CONTENT='/html/body/main/section[1]/div[3]/div[2]/div[1]/h3[2]',
    JAVASCRIPT=vita_script
)
vita_scrapper.save()
