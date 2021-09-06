import requests
from bs4 import BeautifulSoup
from import_csv import result
from pymongo import MongoClient
import json
import time

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbMyProject
col = db.catfood
access_token = "EAAFdHXLlGFgBAIlMg30A3GSYx15ZCpuU2Q9IfryNQl6UVxaI4tt4NiUVnwLZCfIW7LbcZAZCbAN" \
         + "sp07KaSLku7nZApLFx4CCVm1f7nidZAUh8KHJEigd0aBE3Kh9rEE1AF0NAz6EdQPFJ8E5UMWI4u3" \
         + "rN8yr1LEApFZBqmvlkaT2woGlqhP4CSKDgkD9ufnkoOJC91rZClSurwZDZD"


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
        time.sleep(2)
        data = requests.post(new_url)
        response = data.json()
        return response['image'][0]['url']


brand_list = [
    "A La CARTE", "Aatas Cat", "AATU", "Absolute Holistic", "ACANA", "Addiction", "Adirondack", "ADVANCE",
    "Against The Grain", "AlmoNature", "Ancestry", "Animonda", "AnnaMaet", "Artemis", "Aujou by RAWZ",
    "Avoderm", "BEST BREED", "BlackHawk", "Blackwood Pet Food", "Blue Buffalo", "Bonachibo", "BOREAL",
    "Bravery Pet Food", "Canada Fresh", "Canagan", "Canidae Per Foods", "Cardinal Fussie Cat", "Carna4",
    "Caru", "Catz finefood", "Celtic Connection Holistic Pet Food", "Chicken Soup for the Soul",
    "Companion Pets Classic", "Diamond Pet Foods Premium Edge", "Dr. Clauder's Best Choice", "Dr.Link",
    "Earthborn", "Economy ROYAL", "Entoma", "Essential The Jaguar", "Evanger's GrainFree", "Evolve",
    "Farmina Vet Life Feline", "Feline Natural", "First Choice Canada", "FirstMate", "Fish4Cats",
    "Forza10 USA", "GATHER", "Go! Solutions", "Gosbi", "Grandma mae's", "Hagen Catit Dinner", "Halo pets",
    "Healthy Shores Canada", "Hi-tek Naturals", "Hills", "Husse", "Instinct", "iti Pet Food", "Josera",
    "Kirkland Signature", "Kongo", "KOOKUT", "Leonardo Catfood", "Lily's Kitchen", "Little BigPaw", "Lotus",
    "Maria Pet Food", "Marp", "Me-O", "MEOW Cat Food", "MeowMix", "Mera Finest", "Merrick", "Miamor (German)",
    "Micho", "Mito", "Monge", "Natural Balance", "Natural Greatness", "Nature's Logic", "Nature's Protection",
    "Naturliebe FairCat", "Naturliebe HappyCat", "Naturo", "New Origin Pet Bakery", "North Paw",
    "Northwest Naturals", "NOW FRESH", "Nulo Freestyle", "NutraGold", "Nutram Canada", "Nutrience",
    "NutriSource", "Nutro", "Openfarm Korea", "Organix", "Orijen Cat", "Oven-Baked Traditional",
    "PRIMAL PET FOODS", "PRO PAC Ultimates", "Pro-Nutrition PureLife", "Pronature Canada", "PureLuxe",
    "Rawz", "Rex Catfood", "Royal_Canin", "Sanabelle", "Schesir", "Sheba", "Smack Raw Hydrate Cat Food",
    "SmartHeartGold 9 care", "SolidGold Petfood", "Specific", "Stella and Chewys", "Steve's Real Food",
    "Supreme Source", "Taste of the Wild", "Tender and True", "Terra Felis", "Thrive complete", "TIKI CATS",
    "TOMOJO Pet Food", "TOTAL ALIMENTOS EQUILIBRIO", "Trovet", "TRULINE", "Tuffy's Petfoods Dinnertime",
    "Tuffy's Purevita", "TUSCAN NATURAL", "Verus", "Vet's Complete Life", "Vet's Kitchen", "Vigor and Sage",
    "Vintage Cat food", "Vitakraft Cat Food", "Vital Essentials", "Wellness", "Weruva Catfood", "Whiskas",
    "Wishbone", "Wysong", "ZEAL Canada", "ZiwiPeak"]


if __name__ == '__main__':
    for brand in brand_list:
        input_file = open(f"./data/{brand}.json", mode="r", encoding="utf8", newline="")
        formulas = json.load(input_file)
        if type(formulas) is list:
            for formula in formulas:
                time.sleep(2)
                image = get_meta_img_tag(formula['url'])
                print(image)
                formula_id = formula['title']
                db.users.update_one({'title': formula_id}, {'$set': {'image': image}})
            with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
                json.dump(formulas, out, ensure_ascii=False, allow_nan=True)
        else:
            formulas['image'] = get_meta_img_tag(formulas['url'])




