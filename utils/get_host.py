import json
from urllib.parse import urlparse, urljoin

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
    'Wishbone', 'Wysong', 'Wellness', 'ZEAL Canada', 'ZiwiPeak']


def get_host_name(url):
    parsed = urlparse(url)
    scheme = parsed.scheme
    host = parsed.hostname
    return f"{scheme}://{host}"


if __name__ == '__main__':
    for brand in brand_list:
        input_file = open(f"./data/{brand}.json", mode="r", encoding="utf8", newline="")
        formulas = json.load(input_file)
        if type(formulas) is list:
            for formula in formulas:
                formula['site'] = get_host_name(formula['url'])
                print(formula['site'])
            with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
                json.dump(formulas, out, indent=4, ensure_ascii=False, allow_nan=True)
        else:
            formulas['site'] = get_host_name(formulas['url'])
            with open(f"./data/{brand}.json", mode="w", encoding="utf8", newline="") as out:
                json.dump(formulas, out, indent=4, ensure_ascii=False, allow_nan=True)