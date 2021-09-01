import json
from selenium import webdriver


brand_list = [
    "BOREAL",
    "Canada Fresh",
    "Companion Pets Classic",
    "Dr.Link",
    "Farmina Vet Life Feline",
    "FirstMate",
    "Go! Solutions",
    "Halo pets",
    "iti Pet Food",
    "Little BigPaw",
    "Mera Finest",
    "Nulo Freestyle",
    "Pronature Canada",
    "Specific",
    "Stella and Chewys",
    "Tender and True",
    "TIKI CATS",
]

driver = webdriver.Chrome()
for brand in brand_list:
    with open(file=f"./data/0001_{brand}.json", mode="r", encoding="UTF-8", newline="") as input_file:
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
    with open(file=f"./data/{brand}.json", mode="w", encoding="UTF-8", newline="") as output_file:
        json.dump(formulas1, output_file, indent=4, ensure_ascii=False, allow_nan=True)
