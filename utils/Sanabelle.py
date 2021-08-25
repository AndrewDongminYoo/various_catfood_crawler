from objective_scraper import WebScrapper


scrapper = WebScrapper("Sanabelle")
script = """
const activate = (selector, classProp, style) => {
    document.querySelector(selector).classList.add(classProp);
    document.querySelector(selector).setAttribute('style', style);
};
activate("#zusatzstoffe", "in", "display: block; padding-right: 17px;");
activate("#analyt", "in", "display: block; padding-right: 17px;");
"""

scrapper.crawl(
    DESC_PATH='//*[@id="htmlID"]/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/main/div[2]/div/div[3]/p',
    BENEFIT_PATH='//*[@id="htmlID"]/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/main/div[2]/div/div[1]/div[2]/ul/li',
    INGREDIENTS='/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/div/main/div[5]/div/p',
    ANALYSIS='//*[@id="analyt"]/div/div/div[2]',
    ADDITIVES='//*[@id="zusatzstoffe"]/div/div/div[2]',
    JAVASCRIPT=script
)
scrapper.save()
