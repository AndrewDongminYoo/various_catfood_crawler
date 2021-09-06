import json
from collections import OrderedDict

from import_csv import result
import requests
from selenium import webdriver

brand_list = ["A La CARTE", "Aatas Cat", "AATU", "Absolute Holistic", "ACANA", "Addiction", "Adirondack", "ADVANCE", "Against The Grain", "AlmoNature", "Ancestry", "Animonda", "AnnaMaet", "Artemis", "Aujou by RAWZ", "Avoderm", "BEST BREED", "BlackHawk", "Blackwood Pet Food", "Blue Buffalo", "Bonachibo", "BOREAL", "Bravery Pet Food", "Canada Fresh", "Canagan", "Canidae Per Foods", "Cardinal Fussie Cat", "Carna4", "Caru", "Catz finefood", "Celtic Connection Holistic Pet Food", "Chicken Soup for the Soul", "Companion Pets Classic", "Diamond Pet Foods Premium Edge", "Dr. Clauder's Best Choice", "Dr.Link", "Earthborn", "Economy ROYAL", "Entoma", "Essential The Jaguar", "Evanger's GrainFree", "Evolve", "Farmina Vet Life Feline", "Feline Natural", "First Choice Canada", "FirstMate", "Fish4Cats", "Forza10 USA", "GATHER", "Go! Solutions", "Gosbi", "Grandma mae's", "Hagen Catit Dinner", "Halo pets", "Healthy Shores Canada", "Hi-tek Naturals", "Hills", "Husse", "Instinct", "iti Pet Food", "Josera", "Kirkland Signature", "Kongo", "KOOKUT", "Leonardo Catfood", "Lily's Kitchen", "Little BigPaw", "Lotus", "Maria Pet Food", "Marp", "Me-O", "MEOW Cat Food", "MeowMix", "Mera Finest", "Merrick", "Miamor (German)", "Micho", "Mito", "Monge", "Natural Balance", "Natural Greatness", "Nature's Logic", "Nature's Protection", "Naturliebe FairCat", "Naturliebe HappyCat", "Naturo", "New Origin Pet Bakery", "North Paw", "Northwest Naturals", "NOW FRESH", "Nulo Freestyle", "NutraGold", "Nutram Canada", "Nutrience", "NutriSource", "Nutro", "Openfarm Korea", "Organix", "Orijen Cat", "Oven-Baked Traditional", "PRIMAL PET FOODS", "PRO PAC Ultimates", "Pro-Nutrition PureLife", "Pronature Canada", "PureLuxe", "Rawz", "Rex Catfood", "Royal_Canin", "Sanabelle", "Schesir", "Sheba", "Smack Raw Hydrate Cat Food", "SmartHeartGold 9 care", "SolidGold Petfood", "Specific", "Stella and Chewys", "Steve's Real Food", "Supreme Source", "Taste of the Wild", "Tender and True", "Terra Felis", "Thrive complete", "TIKI CATS", "TOMOJO Pet Food", "TOTAL ALIMENTOS EQUILIBRIO", "Trovet", "TRULINE", "Tuffy's Petfoods Dinnertime", "Tuffy's Purevita", "TUSCAN NATURAL", "Verus", "Vet's Complete Life", "Vet's Kitchen", "Vigor and Sage", "Vintage Cat food", "Vitakraft Cat Food", "Vital Essentials", "Wellness", "Weruva Catfood", "Whiskas", "Wishbone", "Wysong", "ZEAL Canada", "ZiwiPeak"]
key_list = ['url', 'brand', 'title', 'descriptions', 'key_benefits', 'ingredients', 'analysis', 'additive', 'calorie']
# driver = webdriver.Chrome()


# for brand in brand_list:
#     with open(f"./data/{brand}.json", mode='r', encoding='UTF-8') as input_file:
#         formulas = json.load(input_file)
#         if type(formulas) is list:
#             some_list = []
#             for formula in formulas:
#                 some_dict = dict()
#                 some_dict[key_list[0]] = formula.get(key_list[0])
#                 some_dict[key_list[1]] = formula.get(key_list[1])
#                 some_dict[key_list[2]] = formula.get(key_list[2])
#                 some_dict[key_list[3]] = formula.get(key_list[3])
#                 some_dict[key_list[4]] = formula.get(key_list[4])
#                 some_dict[key_list[5]] = formula.get(key_list[5])
#                 some_dict[key_list[6]] = formula.get(key_list[6])
#                 some_dict[key_list[7]] = formula.get(key_list[7])
#                 some_dict[key_list[8]] = formula.get(key_list[8])
#                 some_list.append(some_dict)
#             with open(f"./data/{brand}.json", mode='w', encoding='UTF-8') as output:
#                 json.dump(some_list, output, indent=4, ensure_ascii=False, allow_nan=True)
#         elif type(formulas) is dict:
#             formula = formulas
#             some_dict = dict()
#             some_dict[key_list[0]] = formula.get(key_list[0])
#             some_dict[key_list[1]] = formula.get(key_list[1])
#             some_dict[key_list[2]] = formula.get(key_list[2])
#             some_dict[key_list[3]] = formula.get(key_list[3])
#             some_dict[key_list[4]] = formula.get(key_list[4])
#             some_dict[key_list[5]] = formula.get(key_list[5])
#             some_dict[key_list[6]] = formula.get(key_list[6])
#             some_dict[key_list[7]] = formula.get(key_list[7])
#             some_dict[key_list[8]] = formula.get(key_list[8])
#             with open(f"./data/{brand}.json", mode='w', encoding='UTF-8') as output:
#                 json.dump(some_dict, output, indent=4, ensure_ascii=False, allow_nan=True)
