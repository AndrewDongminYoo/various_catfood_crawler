import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

brand_list = [
    'A La CARTE', 'Aatas Cat', 'AATU', 'Absolute Holistic', 'ACANA', 'Addiction', 'Adirondack', 'ADVANCE', 'AlmoNature',
    'Ancestry', 'AnnaMaet', 'Artemis', 'Aujou by RAWZ', 'Avoderm', 'Against The Grain', 'Animonda', 'BEST BREED',
    'BlackHawk', 'Blackwood Pet Food', 'Blue Buffalo', 'Bonachibo', 'BOREAL', 'Bravery Pet Food', 'Canada Fresh',
    'Canagan', 'Cardinal Fussie Cat', 'Carna4', 'Caru', 'Catz finefood', 'Canidae Per Foods', 'Companion Pets Classic',
    'Chicken Soup for the Soul', 'Celtic Connection Holistic Pet Food', 'Diamond Pet Foods Premium Edge',
    "Dr. Clauder's Best Choice", 'Dr.Link', 'Earthborn', 'Economy ROYAL', 'Entoma', 'Essential The Jaguar',
    "Evanger's GrainFree", 'Evolve', 'Feline Natural', 'First Choice Canada', 'FirstMate', 'Fish4Cats', 'Forza10 USA',
    'Farmina Vet Life Feline', 'GATHER', 'Go! Solutions', 'Gosbi', "Grandma mae's", 'Hagen Catit Dinner', 'Halo pets',
    'Hills', 'Hi-tek Naturals', 'Healthy Shores Canada', 'Husse', 'Instinct', 'iti Pet Food', 'Josera', 'KOOKUT',
    'Kirkland Signature', 'Kongo', "Lily's Kitchen", 'Little BigPaw', 'Leonardo Catfood', 'Lotus', 'Miamor (German)',
    'Monge', 'Marp', 'MeowMix', 'Mera Finest', 'Maria Pet Food', 'Me-O', 'MEOW Cat Food', 'Merrick', 'Micho', 'Mito',
    'Natural Balance', 'Natural Greatness', 'Naturo', 'NOW FRESH', 'Nulo Freestyle', 'Nutram Canada', 'Nutrience',
    'NutriSource', 'Nutro', "Nature's Logic", "Nature's Protection", 'Naturliebe FairCat', 'Naturliebe HappyCat',
    'New Origin Pet Bakery', 'North Paw', 'Northwest Naturals', 'NutraGold', 'Openfarm Korea', 'Oven-Baked Traditional',
    'Organix', 'Orijen Cat', 'PRIMAL PET FOODS', 'Pronature Canada', 'PureLuxe', 'PRO PAC Ultimates',
    'Pro-Nutrition PureLife', 'Rawz', 'Royal_Canin', 'Rex Catfood', 'Schesir', 'Smack Raw Hydrate Cat Food',
    'SolidGold Petfood', 'Sanabelle', 'Sheba', 'SmartHeartGold 9 care', 'Specific', 'Stella and Chewys',
    "Steve's Real Food", 'Supreme Source', 'Taste of the Wild', 'Terra Felis', 'Thrive complete', 'TIKI CATS',
    'TOMOJO Pet Food', 'TRULINE', "Tuffy's Purevita", 'Tender and True', 'TOTAL ALIMENTOS EQUILIBRIO', 'Trovet',
    "Tuffy's Petfoods Dinnertime", 'TUSCAN NATURAL', "Vet's Kitchen", 'Vitakraft Cat Food', 'Verus',
    "Vet's Complete Life", 'Vigor and Sage', 'Vintage Cat food', 'Vital Essentials', 'Weruva Catfood', 'Whiskas',
    'Wishbone', 'Wysong', 'Wellness', 'ZEAL Canada', 'ZiwiPeak'
]

except_list = [
    'Against The Grain', 'Bravery Pet Food', 'Celtic Connection Holistic Pet Food', 'Chicken Soup for the Soul',
    "Dr. Clauder's Best Choice", 'Gosbi', "Grandma mae's", 'Husse', 'Instinct', 'iti Pet Food',
    'Kongo', 'Lotus', 'MEOW Cat Food', 'Maria Pet Food', 'Me-O', 'Merrick', 'Companion Pets Classic', 'Josera',
    "Nature's Logic", 'Naturliebe FairCat', 'Naturliebe HappyCat', 'NutraGold', 'Organix', 'Orijen Cat',
    'Pro-Nutrition PureLife', 'Rex Catfood', 'Sanabelle', 'SmartHeartGold 9 care', 'Specific', "Steve's Real Food",
    'Supreme Source', 'TOTAL ALIMENTOS EQUILIBRIO', 'TUSCAN NATURAL', 'Tender and True', 'Trovet',
    "Tuffy's Petfoods Dinnertime", 'Verus', 'Vigor and Sage', 'Vintage Cat food', 'Vital Essentials',
    'Wellness', 'ZiwiPeak'
]

driver = Chrome()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, timeout=5)


def finda(XPATH):
    return wait.until(EC.element_to_be_clickable((By.XPATH, XPATH)))


def search_google_img_get_first(product):
    url = product['url']
    driver.get(f"https://www.google.com/search?q={url}&tbm=isch")
    finda('//*[@id="islrg"]/div[1]/div[1]/a[1]').click()
    finda('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[1]').click()
    finda('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/div[2]/div/a').click()
    return finda('//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/div/div[4]/a').text


if __name__ == '__main__':
    for brand in except_list:
        input_file = open(f"./data/{brand}.json", mode="r", encoding="utf8", newline="")
        formulas = json.load(input_file)
        if type(formulas) is list:
            for formula in formulas:
                formula['image'] = search_google_img_get_first(formula)
                print(formula['image'])
            with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
                json.dump(formulas, out, indent=4, ensure_ascii=False, allow_nan=True)
        else:
            formulas['image'] = search_google_img_get_first(formulas)
            print(formulas['image'])
            with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
                json.dump(formulas, out, indent=4, ensure_ascii=False, allow_nan=True)
