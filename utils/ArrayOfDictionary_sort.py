import json

input1 = open("./data/Nutro.json", mode="r", encoding="utf8", newline="")
input2 = open("./data/0001_Nutro.json", mode="r", encoding="utf8", newline="")
json1 = json.load(input1)
json2 = json.load(input2)
formulas = sorted(json1, key=(lambda x: x['url']))
formulas2 = sorted(json1, key=(lambda x: x['url']))
output1 = open("./data/Nutro_.json", mode="w", encoding="utf8", newline="")
output2 = open("./data/0001_Nutro_.json", mode="w", encoding="utf8", newline="")
json.dump(formulas, output1, indent=4, ensure_ascii=False, allow_nan=True)
json.dump(formulas2, output2, indent=4, ensure_ascii=False, allow_nan=True)