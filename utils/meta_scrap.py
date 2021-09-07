import requests
from bs4 import BeautifulSoup
from import_csv import result
from pymongo import MongoClient
import json
import time

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbMyProject
col = db.catfood
access_token = "EAAFdHXLlGFgBAC78qFFDR6QAc8eQdSJcZBDO0bktnJdK9rUsYDi6fdgZBddd88mvx59OFUqJTVWdp9De2zGbPk8u6KZAqjTZBDZCfnU4oNsfyMmgookDDWYWtUlpi2AewOhIdME5FQi4z0VjBviyUnfnsEks2BLC8Q0cmtnBASQg06VbjWF49Fj2E8swLTDU3ZAmVfYLtuxzLmzndx8gZAZB"


def get_meta_img_tag(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    new_url = "https://graph.facebook.com/v9.0/?scrape=true&id=" + url.replace(':', "%3A").replace('/', '%2F')\
        + "&access_token=" + access_token
    try:
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        return soup.select_one('meta[property="og:image"]')['content']
    except TypeError:
        data = requests.post(new_url)
        time.sleep(5)
        response = data.json()
        print("fb", end=" ")
        return response['image'][0]['url']


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
    'Companion Pets Classic', "Dr. Clauder's Best Choice", 'Gosbi', "Grandma mae's", 'Husse', 'Instinct',
    'iti Pet Food', 'Josera', 'Kongo', 'Lotus', 'MEOW Cat Food', 'Maria Pet Food', 'Me-O', 'Merrick',
    "Nature's Logic", 'Naturliebe FairCat', 'Naturliebe HappyCat', 'NutraGold', 'Organix', 'Orijen Cat',
    'Pro-Nutrition PureLife', 'Rex Catfood', 'Sanabelle', 'SmartHeartGold 9 care', 'Specific', "Steve's Real Food",
    'Supreme Source', 'TOTAL ALIMENTOS EQUILIBRIO', 'TUSCAN NATURAL', 'Tender and True', 'Trovet',
    "Tuffy's Petfoods Dinnertime", 'Verus', 'Vigor and Sage', 'Vintage Cat food', 'Vital Essentials',
    'Wellness', 'ZiwiPeak']


# if __name__ == '__main__':
#     prev = None
#     for brand in sorted(brand_list):
#         input_file = open(f"./data/{brand}.json", mode="r", encoding="utf8", newline="")
#         formulas = json.load(input_file)
#         try:
#             if type(formulas) is list:
#                 for formula in formulas:
#                     if "image" not in formula.keys():
#                         image = get_meta_img_tag(formula['url'])
#                         if image and prev != image:
#                             formula['image'] = image
#                             print(brand, formula['image'])
#                             prev = image
#                         else:
#                             print(brand, "same image again")
#                             formula['image'] = None
#                             except_list.add(brand)
#                             continue
#                     # formula_id = formula['title']
#                     # col.update_one({'title': formula_id}, {'$set': {'image': image}})
#                 with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
#                     json.dump(formulas, out, indent=4, ensure_ascii=False, allow_nan=True)
#             else:
#                 formulas['image'] = get_meta_img_tag(formulas['url'])
#                 with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
#                     json.dump(formulas, out, indent=4, ensure_ascii=False, allow_nan=True)
#         except:
#             print(brand, "cannot reach image")
#             except_list.add(brand)
#             continue
# print(f"exception_list = {except_list}")
