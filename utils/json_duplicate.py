import json
from collections import OrderedDict

from import_csv import result
import requests
from selenium import webdriver

brand_list = ["A La CARTE", "Aatas Cat", "AATU", "Absolute Holistic", "ACANA", "Addiction", "Adirondack", "ADVANCE", "Against The Grain", "AlmoNature", "Ancestry", "Animonda", "AnnaMaet", "Artemis", "Aujou by RAWZ", "Avoderm", "BEST BREED", "BlackHawk", "Blackwood Pet Food", "Blue Buffalo", "Bonachibo", "BOREAL", "Bravery Pet Food", "Canada Fresh", "Canagan", "Canidae Per Foods", "Cardinal Fussie Cat", "Carna4", "Caru", "Catz finefood", "Celtic Connection Holistic Pet Food", "Chicken Soup for the Soul", "Companion Pets Classic", "Diamond Pet Foods Premium Edge", "Dr. Clauder's Best Choice", "Dr.Link", "Earthborn", "Economy ROYAL", "Entoma", "Essential The Jaguar", "Evanger's GrainFree", "Evolve", "Farmina Vet Life Feline", "Feline Natural", "First Choice Canada", "FirstMate", "Fish4Cats", "Forza10 USA", "GATHER", "Go! Solutions", "Gosbi", "Grandma mae's", "Hagen Catit Dinner", "Halo pets", "Healthy Shores Canada", "Hi-tek Naturals", "Hills", "Husse", "Instinct", "iti Pet Food", "Josera", "Kirkland Signature", "Kongo", "KOOKUT", "Leonardo Catfood", "Lily's Kitchen", "Little BigPaw", "Lotus", "Maria Pet Food", "Marp", "Me-O", "MEOW Cat Food", "MeowMix", "Mera Finest", "Merrick", "Miamor (German)", "Micho", "Mito", "Monge", "Natural Balance", "Natural Greatness", "Nature's Logic", "Nature's Protection", "Naturliebe FairCat", "Naturliebe HappyCat", "Naturo", "New Origin Pet Bakery", "North Paw", "Northwest Naturals", "NOW FRESH", "Nulo Freestyle", "NutraGold", "Nutram Canada", "Nutrience", "NutriSource", "Nutro", "Openfarm Korea", "Organix", "Orijen Cat", "Oven-Baked Traditional", "PRIMAL PET FOODS", "PRO PAC Ultimates", "Pro-Nutrition PureLife", "Pronature Canada", "PureLuxe", "Rawz", "Rex Catfood", "Royal_Canin", "Sanabelle", "Schesir", "Sheba", "Smack Raw Hydrate Cat Food", "SmartHeartGold 9 care", "SolidGold Petfood", "Specific", "Stella and Chewys", "Steve's Real Food", "Supreme Source", "Taste of the Wild", "Tender and True", "Terra Felis", "Thrive complete", "TIKI CATS", "TOMOJO Pet Food", "TOTAL ALIMENTOS EQUILIBRIO", "Trovet", "TRULINE", "Tuffy's Petfoods Dinnertime", "Tuffy's Purevita", "TUSCAN NATURAL", "Verus", "Vet's Complete Life", "Vet's Kitchen", "Vigor and Sage", "Vintage Cat food", "Vitakraft Cat Food", "Vital Essentials", "Wellness", "Weruva Catfood", "Whiskas", "Wishbone", "Wysong", "ZEAL Canada", "ZiwiPeak"]
key_list = ['site', 'url', 'brand', 'title', 'image', 'descriptions', 'key_benefits', 'ingredients', 'analysis', 'additive', 'calorie']
# driver = webdriver.Chrome()

if __name__ == "__main__":
    for brand in brand_list:
        with open(f"./data/{brand}.json", mode='r', encoding='UTF-8') as input_file:
            formulas = json.load(input_file)
            if type(formulas) is list:
                some_list = []
                title = ""
                for formula in formulas:
                    if formula['title'] == title:
                        some_list.append(title)
                    title = formula['title']
                if some_list:
                    print(some_list)
            elif type(formulas) is dict:
                # print("single formula:", formulas['title'])
                pass
