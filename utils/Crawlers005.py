from import_csv import result
from objective_scraper import WebScrapper

brand_list = ['AATU', 'ACANA', 'ADVANCE', 'Animonda', 'Avoderm', 'Fish4Cats',
              'Husse', 'Josera', 'Me-O', 'MEOW Cat Food', 'Oven-Baked Traditional',
              'PRIMAL PET FOODS', 'PureLuxe', 'Schesir', 'TOTAL ALIMENTOS EQUILIBRIO',
              "Tuffy's Purevita", 'Verus', 'Vitakraft Cat Food', 'Wysong']
for brand in brand_list:
    print(result[brand][0])

aatu_scrapper = WebScrapper("AATU")
aatu_script = """
let trigger = document.querySelector("div.prd-DetailContent_HeaderText > div.prd-DetailContent_DescriptionContainer")
trigger.setAttribute('aria-hidden',true);
"""
aatu_script2 = """
document.querySelectorAll("#shopify-section-product div.prd-Detail_Accordion > div").forEach(e=>{
    e.setAttribute('aria-expanded',true)
});
"""
aatu_scrapper.crawl(
    DESC_PATH='//*[@id="shopify-section-product"]/div/div/div/div/div[2]/div[2]/div/header/div[1]/div/div[2]/p',
    BENEFIT_PATH='//*[@id="shopify-section-product"]/div/div/div/div/div[1]/div/div[3]/div[1]/div[2]/div/ul/li',
    INGREDIENTS='//*[@id="shopify-section-product"]/div/div/div/div/div[1]/div/div[3]/div[3]/div[2]/div/div/div[1]/p',
    ANALYSIS='//*[@id="shopify-section-product"]/div/div/div/div/div[1]/div/div[3]/div[3]/div[2]/div/div/div[2]/p',
    ADDITIVES='//*[@id="shopify-section-product"]/div/div/div/div/div[1]/div/div[3]/div[3]/div[2]/div/div/div[3]/p',
    JAVASCRIPT=aatu_script,
    JAVASCRIPT_DESC=aatu_script2
)
aatu_scrapper.save()
acana_scrapper = WebScrapper("ACANA")
acana_script = """
document.querySelectorAll("div.panel.entry-content.wc-tab").forEach(e=>e.setAttribute('style','display:block;'))
"""
acana_scrapper.crawl(
    DESC_PATH='//*[@id="tab-description"]/div/div[1]/p[2]',
    INGREDIENTS='//*[@id="tab-composition"]/p[1]',
    ANALYSIS='//*[@id="tab-analytical-constituents"]/ul/li',
    JAVASCRIPT=acana_script
)
acana_scrapper.save()
advance_scrapper = WebScrapper("ADVANCE")
advance_script = """
document.querySelectorAll('.tab-content').forEach(e=>e.setAttribute('style','max-height: 100vh;padding-bottom: 15px;'));
"""
template = '//*[@id="shopify-section-product-template"]/section[1]/div[1]/div[2]'
advance_scrapper.crawl(
    DESC_PATH=template+'/div/div/div[1]/div[6]/div',
    BENEFIT_PATH=template+'/section[2]/div[2]/div/div/div',
    INGREDIENTS=template+'/div/div/div[3]/div/div/div/div[1]/div/p[2]',
    ANALYSIS=template+'/div/div/div[3]/div/div/div/div[2]/div/table/tbody/tr',
    CALORIE_CONTENT=template+'/div/div/div[3]/div/div/div/div[2]/div/table/tbody/tr[last()]/td[1]',
    JAVASCRIPT=advance_script
)
advance_scrapper.save()
ani_scrapper = WebScrapper("Animonda")
ani_script = """
let english = document.querySelector("li.lang-nav > ul > li:nth-child(2) > a").getAttribute('href');
location.replace(english);
"""
ani_script2 = """
document.querySelectorAll("div.card.tab-pane.fade").forEach(e=>{
    e.classList.add('active');
    e.classList.add('show');
})
document.querySelectorAll("div.collapse").forEach(e=>e.classList.add('show'));
"""
ani_scrapper.crawl(
    DESC_PATH='/html/body/div[1]/main/div[1]/section[1]/div/div/div[2]/div/div[1]/div/p[1]',
    BENEFIT_PATH='/html/body/div[1]/main/div[1]/section[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]',
    INGREDIENTS='/html/body/div[1]/main/div[1]/section[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/p',
    ANALYSIS='/html/body/div[1]/main/div[1]/section[2]/div/div/div[2]/div[2]/div[2]/div/div/table/tbody/tr',
    ADDITIVES='/html/body/div[1]/main/div[1]/section[2]/div/div/div[2]/div[3]/div[2]/div/ul/li',
    CALORIE_CONTENT='/html/body/div[1]/main/div[1]/section[2]/div/div/div[2]/div[4]/div[2]/div',
    JAVASCRIPT=ani_script,
    JAVASCRIPT_DESC=ani_script2
)
ani_scrapper.save()
avocado_scrapper = WebScrapper("Avoderm")
avocado_script = """
document.querySelectorAll('.woocommerce-Tabs-panel').forEach(e=>e.setAttribute('style','display:block;'));
"""
avocado_scrapper.crawl(
    DESC_PATH='/html/body/div[1]/div[2]/main/div/div[1]/section/div[2]/div[2]/div/div[3]/div/div/div[1]/div/p[1]',
    BENEFIT_PATH='//*[@id="product-1258"]/div[2]/div/div[3]/div/div/div/p',
    INGREDIENTS='//*[@id="tab-ingredients"]/p',
    ANALYSIS='//*[@id="tab-guaranteed-analysis"]/table/tbody/tr',
    CALORIE_CONTENT='//td[contains(text(),"KCAL")]',
    ADDITIVES='//*[@id="tab-nutrient-analysis"]/table/tbody/tr',
    JAVASCRIPT=avocado_script
)
avocado_scrapper.save()
fish_scrapper = WebScrapper("Fish4Cats")
fish_script = """
document.querySelectorAll('div.data.item.content')[1].setAttribute('style','display:block;');
"""
fish_scrapper.crawl(
    DESC_PATH='//*[@id="description"]/div/div/p',
    INGREDIENTS='//*[@id="nutrition"]/div/div/p[2]',
    ANALYSIS='//*[@id="nutrition"]/div/div/p[1]',
    CALORIE_CONTENT='//*[@id="nutrition"]/div/div/p[4]',
    ADDITIVES='//*[@id="nutrition"]/div/div/p[3]',
    JAVASCRIPT_INGR=fish_script
)
fish_scrapper.save()
husse_scrapper = WebScrapper("Husse")
husse_script = """
document.querySelectorAll('.easytabs-content').forEach(e=>{
    e.classList.add('active');
    e.style = 'display: block;'
});
"""
husse_scrapper.crawl(
    DESC_PATH='//*[@id="product_tabs_description_tabbed_contents"]/div[1]/p[2]',
    BENEFIT_PATH='//*[@id="product_tabs_description_tabbed_contents"]/div[2]/ul/li',
    INGREDIENTS='//*[@id="product_tabs_Ingredients_contents"]/div/p[1]',
    ANALYSIS='//*[@id="product_tabs_Ingredients_contents"]/div/p[2]',
    ADDITIVES='//*[@id="product_tabs_Ingredients_contents"]/div/p[3]',
    JAVASCRIPT=husse_script
)
husse_scrapper.save()
jos_scrapper = WebScrapper("Josera")
jos_script = """
document.querySelectorAll("div.tab-pane.fade").forEach(e=>{
    e.classList.add('active');
    e.classList.add('show');
})
"""
jos_scrapper.crawl(
    DESC_PATH='//*[@id="content"]/div[1]/div/div[2]/div/ul[1]/li',
    BENEFIT_PATH='//*[@id="content"]/div[4]/div/div/div/div[1]/div/div[2]/div',
    INGREDIENTS='//div[@class="pdp-keyfacts__text"]',
    ANALYSIS='//*[@id="tab3"]/div/div/div/div/table/tbody/tr',
    JAVASCRIPT=jos_script
)
jos_scrapper.save()
meo_scrapper = WebScrapper("Me-O")
meo_scrapper.crawl(
    DESC_PATH='/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/p[1]',
    BENEFIT_PATH='/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/ul/li'
)
meo_scrapper.save()
meow_scrapper = WebScrapper("MEOW Cat Food")
meow_scrapper.crawl(
    DESC_PATH='//div[@id="SITE_PAGES"]/div/div/div[2]/div/div/div/section[1]/div[2]/div/div[2]/div/section/div[2]/div/div[2]/div/div/div[2]/div/div[3]/p[3]/span',
    INGREDIENTS='//div[@id="SITE_PAGES"]/div/div/div[2]/div/div/div/section[1]/div[2]/div/div[2]/div/section/div[2]/div/div[2]/div/div/div[2]/div/div[3]/p[7]/span/a',
    ANALYSIS='//p[contains(text(),"%")]',
    CALORIE_CONTENT='//p[contains(text(),"kcal/kg")]'
)
meow_scrapper.save()
oven_scrapper = WebScrapper("Oven-Baked Traditional")
oven_script = """
document.querySelectorAll(".product__single__right__ingredients__list__accordions--content").forEach(e=>e.classList.add('show'));
"""
oven_scrapper.crawl(
    DESC_PATH='//div[@class="product__single__right__advantage__item--text"]',
    BENEFIT_PATH='//*[@class="product__single__right__ingredients__list__accordions--content show"]/p',
    INGREDIENTS='//*[@id="ingredients"]/div[2]/div[2]/p',
    ANALYSIS='//*[@id="nothing-to-hide"]/div[4]/h3/ul/li',
    CALORIE_CONTENT='//*[@id="nothing-to-hide"]/div[6]/p[1]',
    JAVASCRIPT=oven_script
)
oven_scrapper.save()
prime_scrapper = WebScrapper("PRIMAL PET FOODS")
prime_script = """
document.querySelectorAll("div.product__data-panel").forEach(e=>{
    e.classList.add('parent-is-active')
});
document.querySelectorAll("div.product__data-panel > button").forEach(e=>{
    e.classList.add('is-active');
    e.setAttribute('data-is-open',true);
});
document.querySelectorAll("div.product__data-content").forEach(e=>{
    e.setAttribute('aria-hidden',false);
    e.classList.remove('hidden');
});
"""
prime_scrapper.crawl(
    DESC_PATH='//*[@id="shopify-section-product"]/div/section[1]/div[3]/div[2]/span',
    BENEFIT_PATH='//*[@id="shopify-section-product"]/div/section[2]/div[2]/div/ul/li',
    INGREDIENTS='//*[@id="shopify-section-product"]/div/section[3]/div/div[1]/div[1]/div/div',
    ANALYSIS='//*[@id="shopify-section-product"]/div/section[3]/div/div[1]/div[2]/div/div/figure/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="shopify-section-product"]/div/section[3]/div/div[2]/div/ul/li[1]/div[1]',
    ADDITIVES='//*[@id="shopify-section-product"]/div/section[3]/div/div[2]/div/ul/li[2]/div/figure/table/tbody/tr',
    JAVASCRIPT=prime_script
)
prime_scrapper.save()
pure_scrapper = WebScrapper("PureLuxe")
pure_script = """
document.querySelectorAll("div.accordion").forEach(e=>e.classList.add('active'));
document.querySelectorAll("div.acc-content").forEach(e=>e.style="display:block;");
"""
pure_scrapper.crawl(
    DESC_PATH='/html/body/div[3]/section[2]/div/div/div[1]/p',
    BENEFIT_PATH='/html/body/div[3]/section[1]/ul/li',
    INGREDIENTS='/html/body/div[3]/section[2]/div/div/div[1]/div[1]/div[1]/div[2]/p[1]',
    ANALYSIS='/html/body/div[3]/section[2]/div/div/div[1]/div[1]/div[2]/div[2]/ul/li',
    CALORIE_CONTENT='/html/body/div[3]/section[2]/div/div/div[1]/div[1]/div[2]/div[2]/p[4]',
    JAVASCRIPT=pure_script
)
pure_scrapper.save()
sche_scrapper = WebScrapper("Schesir")
sche_scrapper.crawl(
    DESC_PATH='/html/body/div[1]/div[2]/main/div/div[1]/section/div[2]/div[5]/div[1]/p',
    BENEFIT_PATH='/html/body/div[1]/div[2]/main/div/div[1]/section/div[2]/div[5]/div[2]/ul/li',
    INGREDIENTS='/html/body/div[1]/div[2]/main/div/div[1]/section/div[2]/div[5]/p[2]',
    ANALYSIS='/html/body/div[1]/div[2]/main/div/div[1]/section/div[2]/div[5]/p[4]',
    ADDITIVES='//p[contains(text(),"g.")]'
)
sche_scrapper.save()
total_scrapper = WebScrapper("TOTAL ALIMENTOS EQUILIBRIO")
total_scrapper.crawl()
total_scrapper.save()
nutri_scrapper = WebScrapper("Tuffy's Purevita")
nutri_scrapper.crawl(
    DESC_PATH='/html/body/div[1]/div/div/div/div/div/article/div[2]/div/div/div/div[2]/div/div[2]/div[4]/div/ul/li',
    BENEFIT_PATH='//*[@id="et-boc"]/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[2]',
    INGREDIENTS='//*[@id="ingredients-nutrition"]/div[2]/div[1]/div[1]/div/p[1]',
    ANALYSIS='//*[@id="ingredients-nutrition"]/div[2]/div[2]/div/div/table/tbody/tr'
)
nutri_scrapper.save()
verus_scrapper = WebScrapper("Verus")
verus_scrapper.crawl(
    DESC_PATH='//*[@id="main-content"]/div/div/div/div[1]/p[13]',
    BENEFIT_PATH='//*[@id="main-content"]/div/div/div/div[1]/p[12]',
    INGREDIENTS='//*[@id="main-content"]/div/div/div/div[1]/p[2]',
    ANALYSIS='//*[@id="main-content"]/div/div/div/div[2]/div/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="main-content"]/div/div/div/div[1]/p[6]'
)
verus_scrapper.save()
poesie_scrapper = WebScrapper("Vitakraft Cat Food")
poesie_scrapper.crawl(
    TITLE_PATH='//*[@id="viewName"]',
    INGREDIENTS='//*[@id="content_view_desc"]/dl[6]/dd',
    ANALYSIS='//*[@id="content_view_desc"]/dl[7]/dd'
)
poesie_scrapper.save()
song_scrapper = WebScrapper("Wysong")
song_scrapper.crawl(
    DESC_PATH='',
    BENEFIT_PATH='//*[@id="description_loader"]/ul/li[1]',
    INGREDIENTS='//*[@id="description_loader"]'
)
song_scrapper.save()
