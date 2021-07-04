import json

with open('./cat_dog.json', 'r', encoding='utf8', newline="") as input:
    formulas_dict = json.load(input)
    dried_dict = formulas_dict['dried']
    wet_dict = formulas_dict['wet']

    dried_list = []
    wet_list = []
    for formula in dried_dict.keys():
        if formula.split(' ')[0] not in dried_list:
            dried_list.append(formula.split(' ')[0])
    for formula in wet_dict.keys():
        if formula.split(' ')[0] not in wet_list:
            wet_list.append(formula.split(' ')[0])
print("dried")
for item in sorted(dried_list):
    print(item)
print("wet")
for item in sorted(wet_list):
    print(item)
