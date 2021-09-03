from import_csv import result
from objective_scraper import WebScrapper
import json

brand_list = [
    'Aatas Cat', 'Aujou by RAWZ', 'Bravery Pet Food', 'Canagan', "Dr. Clauder's Best Choice", 'Evolve',  'BEST BREED',
    "Grandma mae's", 'Little BigPaw', 'Orijen Cat', 'Rex Catfood', "Steve's Real Food",  'A La CARTE', 'Adirondack',
    'Absolute Holistic', 'Bonachibo', 'Canidae Per Foods', 'Caru', "Evanger's GrainFree", "Lily's Kitchen",
    'Miamor (German)', 'Naturo', 'NutraGold','Openfarm Korea', 'Pro-Nutrition PureLife', 'SmartHeartGold 9 care',
    'ZEAL Canada', 'Addiction', 'AnnaMaet', 'Artemis', 'Blue Buffalo', 'Kongo', 'Marp', 'Naturliebe HappyCat',
    'North Paw', 'NOW FRESH', 'Smack Raw Hydrate Cat Food', 'TUSCAN NATURAL', 'Wishbone', 'Essential The Jaguar',
    'Diamond Pet Foods Premium Edge', 'Earthborn', 'PRO PAC Ultimates', 'Supreme Source', 'Taste of the Wild',
    'TOMOJO Pet Food', 'TRULINE', "Vet's Kitchen", 'Ancestry', 'Beaphar', 'Carna4', 'Economy ROYAL', 'Entoma',
    'Celtic Connection Holistic Pet Food', 'GATHER', 'Hagen Catit Dinner', 'Healthy Shores Canada', 'Micho', 'Mito',
    'Hi-tek Naturals', 'Kirkland Signature', 'Naturliebe FairCat', 'New Origin Pet Bakery',
    'Northwest Naturals', "Tuffy's Petfoods Dinnertime", "Vet's Complete Life", 'Vintage Cat food'
]

indexes = ["javascript", "descriptions", "key_benefits", "ingredients", "analysis", "additives", "calorie"]


for brand in brand_list:
    xpath_selector_list = []
    some_scrapper = WebScrapper(brand)
    driver = some_scrapper.driver
    driver.get(result[brand][0])
    if len(result[brand]) > 1:
        for item in indexes:
            input_value = input(f'"{item} => //')
            if "/" in input_value or "document" in input_value:
                xpath_selector_list.append(input_value)
            else:
                xpath_selector_list.append("")
        some_scrapper.crawl(
            DESC_PATH=xpath_selector_list[1],
            BENEFIT_PATH=xpath_selector_list[2],
            INGREDIENTS=xpath_selector_list[3],
            ANALYSIS=xpath_selector_list[4],
            ADDITIVES=xpath_selector_list[5],
            CALORIE_CONTENT=xpath_selector_list[6],
            JAVASCRIPT=xpath_selector_list[0]
        )
        some_scrapper.save()
    else:
        formula = {'url': result[brand][0], 'brand': brand}
        formula['title'] = driver.title
        for item in indexes[1:]:
            value0 = input(f'"{item}" => // ')
            if '["' in value0 and '"]' in value0:
                value1 = value0[2:-2]
                value0 = value1.split('", "')
            formula[item] = value0
        driver.quit()
        with open(file=f"./data/{brand}.json", mode="w", encoding="UTF-8", newline="") as output_file:
            json.dump(formula, output_file, indent=4, ensure_ascii=False, allow_nan=True)