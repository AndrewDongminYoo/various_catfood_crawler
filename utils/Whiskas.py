from objective_scraper import WebScrapper

scrapper = WebScrapper("Whiskas")
scrapper.crawl(
    DESC_PATH='/html/body/main/div[1]/section[1]/div/div[2]/div[1]/div[2]',
    BENEFIT_PATH='/html/body/main/div[1]/section[1]/div/div[2]/div[1]/div[3]',
    INGREDIENTS='/html/body/main/div[1]/section[2]/div/div[1]/div',
    ANALYSIS='/html/body/main/div[1]/section[3]/div/div[2]/div[1]/table/tbody/tr',
    CALORIE_CONTENT='/html/body/main/div[1]/section[3]/div/div[2]/div[2]/div'
)
scrapper.save()
