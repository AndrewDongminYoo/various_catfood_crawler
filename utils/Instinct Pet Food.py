from objective_scraper import WebScrapper

script = """document
.querySelectorAll
("fieldset.group_type-htab.form-wrapper.horizontal-tabs-pane")
.forEach(e => e.classList.remove('horizontal-tab-hidden'));"""
scraper = WebScrapper("Instinct Pet Food")
scraper.crawl(
    DESC_PATH='//*[@id="block-system-main"]/div/div[2]/div/div/div[1]/div/div[2]/div/div[3]/div/div/p',
    BENEFIT_PATH='//*[@id="block-system-main"]/div/div[2]/div/div/div[1]/div/div[2]/div/div[4]/div/div',
    INGREDIENTS='//*[@id="block-system-main"]/div/div[2]/div/div/div[2]/div/div/div/div/fieldset[1]/div/div/div/div/p[1]',
    ANALYSIS='//*[@id="ga-table"]/tbody/tr',
    CALORIE_CONTENT='//*[@id="block-system-main"]/div/div[2]/div/div/div[2]/div/div/div/div/fieldset[3]/div/div/div/div/div/div[3]/div[2]/div[2]/div/p',
    JAVASCRIPT=script
)
scraper.save()