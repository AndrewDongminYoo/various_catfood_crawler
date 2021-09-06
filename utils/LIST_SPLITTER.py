import json

brand_list = ["A La CARTE", "Aatas Cat", "AATU", "Absolute Holistic", "ACANA", "Addiction", "Adirondack", "ADVANCE", "Against The Grain", "AlmoNature", "Ancestry", "Animonda", "AnnaMaet", "Artemis", "Aujou by RAWZ", "Avoderm", "BEST BREED", "BlackHawk", "Blackwood Pet Food", "Blue Buffalo", "Bonachibo", "BOREAL", "Bravery Pet Food", "Canada Fresh", "Canagan", "Canidae Per Foods", "Cardinal Fussie Cat", "Carna4", "Caru", "Catz finefood", "Celtic Connection Holistic Pet Food", "Chicken Soup for the Soul", "Companion Pets Classic", "Diamond Pet Foods Premium Edge", "Dr. Clauder's Best Choice", "Dr.Link", "Earthborn", "Economy ROYAL", "Entoma", "Essential The Jaguar", "Evanger's GrainFree", "Evolve", "Farmina Vet Life Feline", "Feline Natural", "First Choice Canada", "FirstMate", "Fish4Cats", "Forza10 USA", "GATHER", "Go! Solutions", "Gosbi", "Grandma mae's", "Hagen Catit Dinner", "Halo pets", "Healthy Shores Canada", "Hi-tek Naturals", "Hills", "Husse", "Instinct", "iti Pet Food", "Josera", "Kirkland Signature", "Kongo", "KOOKUT", "Leonardo Catfood", "Lily's Kitchen", "Little BigPaw", "Lotus", "Maria Pet Food", "Marp", "Me-O", "MEOW Cat Food", "MeowMix", "Mera Finest", "Merrick", "Miamor (German)", "Micho", "Mito", "Monge", "Natural Balance", "Natural Greatness", "Nature's Logic", "Nature's Protection", "Naturliebe FairCat", "Naturliebe HappyCat", "Naturo", "New Origin Pet Bakery", "North Paw", "Northwest Naturals", "NOW FRESH", "Nulo Freestyle", "NutraGold", "Nutram Canada", "Nutrience", "NutriSource", "Nutro", "Openfarm Korea", "Organix", "Orijen Cat", "Oven-Baked Traditional", "PRIMAL PET FOODS", "PRO PAC Ultimates", "Pro-Nutrition PureLife", "Pronature Canada", "PureLuxe", "Rawz", "Rex Catfood", "Royal_Canin", "Sanabelle", "Schesir", "Sheba", "Smack Raw Hydrate Cat Food", "SmartHeartGold 9 care", "SolidGold Petfood", "Specific", "Stella and Chewys", "Steve's Real Food", "Supreme Source", "Taste of the Wild", "Tender and True", "Terra Felis", "Thrive complete", "TIKI CATS", "TOMOJO Pet Food", "TOTAL ALIMENTOS EQUILIBRIO", "Trovet", "TRULINE", "Tuffy's Petfoods Dinnertime", "Tuffy's Purevita", "TUSCAN NATURAL", "Verus", "Vet's Complete Life", "Vet's Kitchen", "Vigor and Sage", "Vintage Cat food", "Vitakraft Cat Food", "Vital Essentials", "Wellness", "Weruva Catfood", "Whiskas", "Wishbone", "Wysong", "ZEAL Canada", "ZiwiPeak"]
splittable = ['descriptions', 'key_benefits', 'ingredients', 'analysis', 'additive', 'calorie']

for brand in brand_list:
    with open(f'./data/{brand}.json', 'r', encoding='utf8', newline="") as input_file:
        formulas_list0 = json.load(input_file)
        formulas = json.dumps(formulas_list0)
        formulas_list = json.loads(formulas)
        new_formulas_list = []
        for formula in formulas_list:
            new_formula = {}
            for key, value in formula.items():
                if type(value) is str and any(spt in key for spt in splittable):
                    if '(' in value:
                        bracket = 0
                        for i in range(len(value)):
                            if value[i] == '(':
                                bracket += 1
                                print(value)
                            elif value[i] == ')':
                                bracket -= 1
                                print(value)
                            if value[i] == ',':
                                if bracket == 0:
                                    value = value[:i] + ';' + value[i+1:]
                                    print(value)
                    if '(' in value and '; ' in value:
                        new_formula[key] = value.split('; ')
                    elif ', ' in value:
                        new_formula[key] = value.split(', ')
                else:
                    new_formula[key] = value
            new_formulas_list.append(new_formula)
    if formulas_list0 == formulas_list:
        with open(f"./data/{brand}.json", 'w', encoding='UTF-8') as output:
            json.dump(new_formulas_list, output, indent=4)
    else:
        with open(f"./data/{brand}_.json", 'w', encoding='UTF-8') as output:
            json.dump(new_formulas_list, output, indent=4)
