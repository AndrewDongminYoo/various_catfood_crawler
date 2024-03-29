from pymongo import MongoClient
import json
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.get_database("Cat-Foods")

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
    "Kongo", "KOOKUT", "Leonardo Catfood", "Lily's Kitchen", "Little BigPaw", "Lotus",
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

for brand in brand_list:
    with open(f"./data/{brand}.json", mode="r", encoding="utf8", newline="") as input_file:
        col = db.get_collection(brand)
        col.delete_many({})
        data = json.load(input_file)
        if type(data) is dict:
            if type(data['descriptions']) is list:
                data['descriptions'] = "; ".join(data['descriptions'])
            if type(data['key_benefits']) is list:
                data['key_benefits'] = "; ".join(data['key_benefits'])
            col.update_one({"title": data['title']}, {"$set": data}, True)
        elif type(data) is list:
            for formula in data:
                if type(formula['descriptions']) is list:
                    formula['descriptions'] = "; ".join(formula['descriptions'])
                if type(formula['key_benefits']) is list:
                    formula['key_benefits'] = "; ".join(formula['key_benefits'])
                col.update_one({"title": formula['title']}, {"$set": formula}, True)
