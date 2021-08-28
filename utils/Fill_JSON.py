import json
from selenium import webdriver


brand_list = [
    # "Against The Grain",
    # "AlmoNature",
    # "Blackwood Pet Food",
    # "Cardinal Fussie Cat",
    # "Chicken Soup for the Soul",
    # "Evolve",
    # "Forza10 USA",
    # "Hills",
    # "Instinct",
    # "KOOKUT",
    # "Leonardo Catfood",
    # "MeowMix",
    # "Merrick",
    # "Natural Balance",
    # "Natural Greatness",
    # "Nature's Logic",
    # "Nutram Canada",
    # "Nutrience",
    # "NutriSource",
    # "Nutro",
    # "Organix",
    # "Rawz",
    # "Royal_Canin",
    # "Sanabelle",
    "Terra Felis",
    "Thrive complete",
    "Trovet",
    "Wellness",
    "Weruva Catfood",
    "Whiskas",
    "ZiwiPeak"
]


driver = webdriver.Chrome()
for brand in brand_list:
    with open(file=f"./data/{brand}.json", mode="r", encoding="UTF-8", newline="") as input_file:
        formulas0 = json.load(input_file)
        formulas1 = sorted(formulas0, key=(lambda x: x['url']))
        for formula in formulas1:
            for key, value in formula.items():
                if not value:
                    driver.get(formula['url'])
                    formula[key] = input(f'"{key}" => // ')
    if formulas1 == sorted(formulas0, key=(lambda x: x['url'])):
        with open(file=f"./data/{brand}.json", mode="w", encoding="UTF-8", newline="") as output_file:
            json.dump(formulas1, output_file, indent=4, ensure_ascii=False, allow_nan=True)
    else:
        with open(file=f"./data/{brand}_.json", mode="w", encoding="UTF-8", newline="") as output_file:
            json.dump(formulas1, output_file, indent=4, ensure_ascii=False, allow_nan=True)
