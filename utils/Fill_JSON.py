import json
from selenium import webdriver
import os


brand_list = [
    # "A La CARTE",
    # "Aatas Cat",
    # "Absolute Holistic",
    # "Addiction",
    # "Adirondack",
    # "Ancestry",
    # "AnnaMaet",
    # "Artemis",
    # "Aujou by RAWZ",
    # "BEST BREED",
    # "Blue Buffalo",
    # "Bonachibo",
    # "Bravery Pet Food",
    # "Canagan",
    # "Canidae Per Foods",
    # "Caru",
    # "Diamond Pet Foods Premium Edge",
    # "Dr. Clauder's Best Choice",
    # "Earthborn",
    # "Evanger's GrainFree",
    # "Evolve",
    # "Grandma mae's",
    # "Kongo",
    # "Lily's Kitchen",
    # "Little BigPaw",
    # "Marp",
    # "Miamor (German)",
    # "Naturliebe HappyCat",
    # "Naturo",
    # "North Paw",
    # "NOW FRESH",
    # "NutraGold",
    # "Openfarm Korea",
    # "Orijen Cat",
    # "PRO PAC Ultimates",
    # "Pro-Nutrition PureLife",
    # "Rex Catfood",
    "Smack Raw Hydrate Cat Food",
    "SmartHeartGold 9 care",
    "Steve's Real Food",
    "Supreme Source",
    "Taste of the Wild",
    "TOMOJO Pet Food",
    "TRULINE",
    "TUSCAN NATURAL",
    "Vet's Kitchen",
    "Wishbone",
    "ZEAL Canada"
]

driver = webdriver.Chrome()
for brand in brand_list:
    filepath = f"./data/0001_{brand}.json"
    with open(file=filepath, mode="r", encoding="UTF-8", newline="") as input_file:
        formulas0 = json.load(input_file)
        formulas1 = sorted(formulas0, key=(lambda x: x['url']))
        for formula in formulas1:
            for key, value in formula.items():
                if not value:
                    driver.get(formula['url'])
                    value0 = input(f'"{key}" => // ')
                    if '["' in value0 and '"]' in value0:
                        value1 = value0[2:-2]
                        value0 = value1.split('", "')
                    formula[key] = value0
    if os.path.exists(filepath):
        os.remove(filepath)
    with open(file=f"./data/{brand}.json", mode="w", encoding="UTF-8", newline="") as output_file:
        json.dump(formulas1, output_file, indent=4, ensure_ascii=False, allow_nan=True)
