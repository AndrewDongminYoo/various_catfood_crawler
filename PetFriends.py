import json

with open('./petfriends.json', 'r', encoding='utf8', newline="") as input:
    data = json.load(input)
    formulas_list = data['table']
    list = []
    for formula in formulas_list:
        if formula['brand_name'] not in list:
            list.append(formula['brand_name'])
    list.sort()
for item in list:
    print(item)
