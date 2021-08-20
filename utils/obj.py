from selenium import webdriver
import csv
from urllib import parse
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
brand_list_english =  ['A La CARTE', 'AATU', 'Absolute Holistic', 'ACANA', 'Addiction', 'Adirondack', 'ADVANCE',
                       'Against The Grain', 'AIXIA', 'AlmoNature', 'Alpha Spririt', 'AlphaVET', 'Ancestry', 'ANF',
                       'Animonda', 'AnnaMaet', 'Artemis', 'Atas Cat', 'Aujou by RAWZ', 'Avoderm', 'Beaphar',
                       'BEST BREED', 'BlackHawk', 'Blackwood PetFood', 'Blue Buffalo', 'BlueBay Animate PetFood',
                       'Bonachibo', 'BOREAL', 'Bravery PetFood', 'Canada Fresh', 'Canagan', 'Canidae Per Foods',
                       'Cardinal Fussie Cat', 'Cargill Nutrena', 'Carna4', 'Caru', 'Catz finefood',
                       'Celtic Connection Holistic Pet Food', 'Chicken Soup for the Soul', 'Comanion Pets Classic',
                       'Diamond Pet Foods Premium Edge', "Dr. Clauder's Best Choice", 'Dr.Link', 'Earthborn',
                       'Economy ROYAL', 'Entoma PetFood', 'Essential The Jaguar', "Evanger's GrainFree", 'Evolve',
                       'Farmina Vet Life Feline', 'Feline Natural', 'First Choice Canada', 'FirstMate', 'Fish4Dog',
                       'Forza10 USA', 'GATHER', 'Go! Solution', 'Go! Solutions', 'Good Friends', 'Gosbi',
                       "Grandma mae's", 'Hagen Catit Dinner', 'HALO', 'Halo pets', 'Healthy Shores Canada',
                       "Hill's Science Diet", 'Hi-tek Naturals', 'Husse', 'Instinct Pet Food', 'iti Pet Food',
                       'Josera', 'Kirkland Signature', 'Kongo', 'KOOKUT', 'Leonardo Catfood', "Lilly's Kitchen",
                       'Little BigPaw', 'Lotus', 'Maria Pet Food', 'Marp', 'Me-O', 'MEOW Cat Food', 'MeowMix',
                       'Mera Finest', 'Merrick', 'Miamor (German)', 'Miaw Miaw', 'Micho', 'Mito', 'Monge',
                       'Natural Balance', 'Natural Greatness', 'Natural Planet', "Nature's Logic",
                       "Nature's Protection", "Nature's Variety", 'Naturliebe FairCat', 'Naturliebe HappyCat', 'Naturo',
                       'NEKKO', 'New Origin Pet Bakery', 'Nisshin Kaiseki', 'North Paw', 'Northwest Naturals',
                       'NOW FRESH', 'Nulo Freestyle', 'NutraGold', 'Nutram Canada', 'Nutrena Little Lion',
                       'Nutrena Real O Plus', 'Nutrience', 'Nutrio', 'nutripe classic', 'NutriSource',
                       'Nutro Natural Choice', 'Openfarm Korea', 'Optimanova', 'Orgameal', 'Organix', 'Orijen Cat',
                       "O'stech", 'Oven-Baked Traditional', 'Oven-Baked Traditional', 'PRIMAL PET FOODS',
                       'PRO PAC® Ultimates', 'Pronature Canada', 'Pro-Nutrition PureLife', 'PureLuxe', 'Raws',
                       'Rex Catfood', 'RoyalCanin', 'Sanabelle', 'Schesir', 'Sheba', 'Smack Raw HydratE Cat Food',
                       'SmartHeartGold 9 care', 'Snappy Tom', 'SolidGold Perfood', 'Specific', 'Stella and Chewys',
                       "Steve's Real Food", 'Supreme Source', 'Taste of the Wild', 'Tender & True',
                       'Terra Canis & Terra Fellis', 'Thai Union Manufacturing Co.,Ltd', 'Thrive complete', 'TIKI PETS',
                       'TOMOJO Pet Food', 'TOTAL ALIMENTOS EQUILIBRIO', 'TROVET', 'TRUELINE',
                       "Tuffy's Petfoods Dinnertime", "Tuffy's Purevita", 'TUSCAN NATURAL', 'Verus',
                       "Vet's Complete Life", "Vet's CompleteLife", "Vet's Kitchen", 'Vigor&Sage', 'Vintage Cat food',
                       'Vitakraft CatFood', 'Vital Essentials', 'Vital Essentials', 'Wahre Liebe', 'Wellnesss',
                       'Weruba Catfood', 'Whiskas', 'Wishbone', 'Wysong', 'ZEAL Canada', 'ZiwiPeak']

with open("./data/0004.csv", mode="w", encoding="ansi", newline="") as input_file:
    writer = csv.writer(input_file, dialect="excel")
    for i, brand in enumerate(brand_list_english):
        driver.get("https://www.google.com/search?q=" + brand.replace(" ", "+") + "+cat+food")
        time.sleep(1.2)
        row = [brand]
        links = driver.find_elements_by_css_selector('div.yuRUbf > a')
        for link in links:
            href = link.get_attribute('href')
            row.append(href)
        writer.writerow(row)