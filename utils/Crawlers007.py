from import_csv import result
from objective_scraper import WebScrapper

brand_list = ['Aatas Cat', 'Aujou by RAWZ', 'Bravery Pet Food', 'Canagan', "Dr. Clauder's Best Choice", 'Evolve',
              "Grandma mae's", 'Little BigPaw', 'Orijen Cat', 'Rex Catfood', "Steve's Real Food", 'Absolute Holistic',
              'AIXIA', 'ANF', 'Bonachibo', 'Canidae Per Foods', 'Caru', "Evanger's GrainFree", "Lily's Kitchen",
              'Miamor (German)', 'Naturo', 'NutraGold', 'Openfarm Korea', 'Pro-Nutrition PureLife',
              'SmartHeartGold 9 care', 'ZEAL Canada']
for brand in brand_list:
    print(result[brand][0])

bore_scrapper = WebScrapper('Aatas Cat')
bore_script = """
document.querySelectorAll("div.section-wrap").forEach(e=>e.style="display:block;");
"""
bore_scrapper.crawl(
    DESC_PATH='//*[@id="content"]/p[contains(text(),"Bor")]',
    BENEFIT_PATH='//*[@id="content"]/p[3]',
    INGREDIENTS='//*[@id="content"]/div[4]/h6[1]',
    ANALYSIS='//*[@id="content"]/div[6]/p[1]',
    CALORIE_CONTENT='//*[@id="content"]/div[6]/p[3]',
    JAVASCRIPT=bore_script
)
bore_scrapper.save()

farm_scrapper = WebScrapper('Aujou by RAWZ')
farm_scrapper.crawl(
    DESC_PATH='//*[@id="content-top"]/div/div[2]/div/div/div[6]/p',
    BENEFIT_PATH='//*[@id="content-middle"]/div/div[3]/div[1]/div[1]/p',
    INGREDIENTS='//*[@id="content-middle"]/div/div[1]/div/p',
    ANALYSIS='//*[@id="content-middle"]/div/div[3]/div[1]/div[2]/p[1]',
    CALORIE_CONTENT='//*[@id="content-middle"]/div/div[3]/div[1]/div[2]/p[2]'
)
farm_scrapper.save()

halo_scrapper = WebScrapper('Bravery Pet Food')
halo_scrapper.crawl(
    DESC_PATH='//*[@id="shop-feature"]/div[3]/div[2]/div/div/div/div/div/div/p',
    BENEFIT_PATH='//*[@id="shop-feature"]/div[3]/div[1]/div/div/div/div/div[1]/div',
    INGREDIENTS='//*[@id="shop-feature"]/div[3]/div[5]/div/div[2]',
    ANALYSIS='//*[@id="shop-feature"]/div[3]/div[6]/div/div/div[1]/div[1]/div/div[2]/div/div',
    CALORIE_CONTENT='//*[@id="shop-feature"]/div[3]/div[6]/div/div/div[1]/div[1]/div/div[3]/div[3]'
)
halo_scrapper.save()

iti_scrapper = WebScrapper('Canagan')
iti_scrapper.crawl(
    DESC_PATH='//*[@id="product-166"]/div[2]/div[1]/p',
    INGREDIENTS='//*[@id="tab-description"]/p[2]',
    ANALYSIS='//*[@id="tab-description"]/p[3]',
    CALORIE_CONTENT='//*[@id="tab-description"]/p[4]'
)
iti_scrapper.save()

mera_scrapper = WebScrapper("Dr. Clauder's Best Choice")
mera_script = """
document.querySelectorAll(".accordion-body").forEach(e=>e.classList.add('show'));
"""
mera_scrapper.crawl(
    DESC_PATH='//*[@id="product-accordion-body-1"]/div/p',
    BENEFIT_PATH='/html/body/main/div[2]/span/div[1]/div[1]/div/div/div[2]/div[2]/ul/li',
    INGREDIENTS='//*[@id="product-accordion-body-2"]/div/p[1]',
    ADDITIVES='//*[@id="product-accordion-body-2"]/div/p[2]',
    ANALYSIS='//*[@id="product-accordion-body-2"]/div/p[3]',
    CALORIE_CONTENT='//*[@id="product-accordion-body-3"]/div/div/div[1]/div/p',
    JAVASCRIPT=mera_script
)
mera_scrapper.save()

canada_scrapper = WebScrapper('Evolve')
canada_script = """
document.querySelectorAll("#shopify-section-product__main ul.tabs-content > li").forEach(e=>{
    e.classList.add('is-active');
    e.style="display:block;";
});
"""
canada_scrapper.crawl(
    DESC_PATH='//*[@id="shopify-section-product__main"]/section/div/div/div[2]/div[3]/div[1]/div[2]',
    BENEFIT_PATH='//*[@id="shopify-section-product__main"]/section/div/div/div[2]/div[3]/div[1]/div[1]/ul[1]/li',
    INGREDIENTS='//*[@id="tab1"]/div/p',
    ANALYSIS='//*[@id="tab2"]/div/p[2]',
    CALORIE_CONTENT='//*[@id="tab3"]/div/p',
    JAVASCRIPT=canada_script
)
canada_scrapper.save()

cp_scrapper = WebScrapper("Grandma mae's")
cp_scrapper.crawl(
    DESC_PATH='/html/body/main/section[3]/div/div/div[1]/p',
    INGREDIENTS='/html/body/main/section[4]/div[2]/div[6]/div[2]/p',
    ANALYSIS='/html/body/main/section[4]/div[2]/div[7]/div[2]/ul/li'
)
cp_scrapper.save()

first_scrapper = WebScrapper('Little BigPaw')
first_script = """
document.querySelectorAll("div.tab-pane.fade").forEach(e=>e.classList.add('active','in'))
"""
first_scrapper.crawl(
    DESC_PATH='//*[@id="body"]/div[4]/div/div[1]/div/div[2]/div/p',
    BENEFIT_PATH='//*[@id="body"]/div[4]/div/div[2]/div/div/div/div/ul/li/p',
    INGREDIENTS='//*[@id="ingredients"]/div/div/div[1]/ul/li',
    ANALYSIS='//*[@id="analysis"]/div/div/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="analysis"]/div/div/table/tbody/tr[last()]',
    JAVASCRIPT=first_script
)
first_scrapper.save()

go_scrapper = WebScrapper('Orijen Cat')
go_script = """
document.querySelectorAll("#main-content > div > div > ul > li").forEach(e=>e.classList.add('active'));
"""
go_scrapper.crawl(
    DESC_PATH='//*[@id="main-content"]/div/section[1]/div[2]/p[2]',
    BENEFIT_PATH='//*[@id="main-content"]/div/div[1]/ul[2]/li[1]/section/ul/li/div/div[2]',
    INGREDIENTS='//*[@id="main-content"]/div/div[1]/ul[2]/li[2]/section/div/div/div[1]/div[1]/p',
    ANALYSIS='//*[@id="main-content"]/div/div[1]/ul[2]/li[2]/section/div/div/div[2]/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="main-content"]/div/div[1]/ul[2]/li[2]/section/div/div/div[1]/div[2]/div',
    JAVASCRIPT=go_script
)
go_scrapper.save()

big_scrapper = WebScrapper('Rex Catfood')
big_script = """
document.querySelectorAll("div.woocommerce-Tabs-panel").forEach(e=>e.style="display:block;");
"""
big_scrapper.crawl(
    DESC_PATH='//*[@id="tab-description"]/p',
    BENEFIT_PATH='/html/body/div[3]/div/main/div/div/div/article/div[2]/div[2]/div[2]/ul/li',
    INGREDIENTS='//*[@id="tab-composition"]/p[1]',
    ANALYSIS='//*[@id="tab-composition"]/p[2]',
    ADDITIVES='//*[@id="tab-composition"]/p[3]',
    CALORIE_CONTENT='//*[@id="tab-composition"]/ul/li',
    JAVASCRIPT=big_script
)
big_scrapper.save()

nul_scrapper = WebScrapper("Steve's Real Food")
nul_script = """
document.querySelectorAll(".accordion-content").forEach(e=>e.style="display:block;");
"""
nul_scrapper.crawl(
    DESC_PATH='//*[@id="ProductSection--product-template"]/div/div/div[2]/div[4]/p',
    BENEFIT_PATH='//*[@id="shopify-section-product-template"]/div[2]/div/div/div[1]/div/p',
    INGREDIENTS='//*[@id="ingredients-analysis"]/div[1]/p[1]',
    ANALYSIS='//*[@id="ingredients-analysis"]/div[2]/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="ingredients-analysis"]/div[1]/p[2]',
    JAVASCRIPT=nul_script
)
nul_scrapper.save()

pro_scrapper = WebScrapper('Absolute Holistic')
pro_script = """
document.querySelectorAll(".accordion__item-content").forEach(e=>e.style="display:block;");
"""
pro_scrapper.crawl(
    DESC_PATH='/html/body/section[1]/div/div/div[1]/p',
    BENEFIT_PATH='/html/body/section[1]/div/div/div[2]/div/div/div[2]/p',
    INGREDIENTS='/html/body/section[2]/div/div/ul/li[2]/div[2]/p',
    ANALYSIS='/html/body/section[2]/div/div/ul/li[3]/div[2]/p',
    CALORIE_CONTENT='//*[@id="tab-baby"]/table/tbody/tr[23]/td/div[2]',
    JAVASCRIPT=pro_script
)
pro_scrapper.save()

spec_scrapper = WebScrapper('AIXIA')
spec_script = """
document.querySelectorAll("div.tab-pane.fade").forEach(e=>e.classList.add('active','in'))
"""
spec_scrapper.crawl(
    DESC_PATH='/html/body/div[3]/main/article/section/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div[1]/p[2]',
    BENEFIT_PATH='/html/body/div[3]/main/article/section/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div[2]/ul/li',
    INGREDIENTS='//*[@id="specific-ingredients"]',
    ANALYSIS='//*[@id="specific-nutrient-content"]/table/tbody/tr[2]',
    CALORIE_CONTENT='//*[@id="specific-nutrient-content"]/table/tbody/tr',
    JAVASCRIPT=spec_script
)
spec_scrapper.save()

chewy_scrapper = WebScrapper('Bonachibo')
chewy_scrapper.crawl(
    DESC_PATH='//*[@id="content"]/header/div[2]/div[1]/section/ul/li',
    BENEFIT_PATH='//*[@id="content"]/section[1]/div/div',
    INGREDIENTS='//*[@id="content"]/section[2]/div[2]/section[2]/div/p',
    ANALYSIS='//*[@id="content"]/section[2]/div[1]/section[1]/table/tbody/tr',
    CALORIE_CONTENT='//*[@id="content"]/section[2]/div[1]/section[1]/table/tbody/tr[last()]'
)
chewy_scrapper.save()

ten_scrapper = WebScrapper('Caru')
ten_script = """
document.querySelectorAll("div.tab-pane.fade").forEach(e=>e.classList.add('active','in'));
"""
ten_scrapper.crawl(
    DESC_PATH='/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div[2]/div/div[2]/p',
    BENEFIT_PATH='/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div[2]/div/div[2]/ul/li/h3',
    INGREDIENTS='/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div[3]/div/div[3]/div[2]/div[4]/p[2]',
    ANALYSIS='//div/table/tbody/tr',
    CALORIE_CONTENT='/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div[3]/div/div[3]/div[2]/div[4]/p[1]',
    JAVASCRIPT=ten_script
)
ten_scrapper.save()

tiki_scrapper = WebScrapper("Evanger's GrainFree")
tiki_script = """
document.querySelectorAll("div.tab-pane.fade").forEach(e=>e.classList.add('active','show'));
"""
tiki_scrapper.crawl(
    DESC_PATH='//*[@id="product-banner"]/div[4]/div[2]/p',
    BENEFIT_PATH='//*[@id="product-banner"]/div[4]/div[2]/ul/li',
    INGREDIENTS='//*[@id="collapse-A"]/div/p',
    ANALYSIS='//*[@id="collapse-B"]/div/table/tbody/tr',
    CALORIE_CONTENT='//div[@class="card-body"]/p[contains(text(),"kcal")]',
    JAVASCRIPT=tiki_script
)
tiki_scrapper.save()

link_scrapper = WebScrapper("Lily's Kitchen")

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('Miamor (German)')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('Naturo')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('NutraGold')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('Openfarm Korea')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('Pro-Nutrition PureLife')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('SmartHeartGold 9 care')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()

link_scrapper = WebScrapper('ZEAL Canada')

link_scrapper.crawl(
    DESC_PATH='//*[@id="collateral-tabs"]/dd[1]/div/div',
    BENEFIT_PATH='//*[@id="product_addtocart_form"]/div[3]/div[4]/div/ul/li'
    # INGREDIENTS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ANALYSIS='//*[@id="collateral-tabs"]/dd[1]/div/div',
    # ADDITIVES='//*[@id="collateral-tabs"]/dd[1]/div/div'
)
link_scrapper.save()