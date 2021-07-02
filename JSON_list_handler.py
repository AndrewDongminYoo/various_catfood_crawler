import json

with open('./PURPLE.json', 'r', encoding='utf8', newline="") as input:
    formulas_list = json.load(input)
    I_am_on_the_next_level = []

    for formula in formulas_list:
        dict = {}
        for key, value in formula.items():
            if type(value) == float:
                dict[key] = value
            elif type(value) is str and any(listed in key for listed in ["english_ing", "korean_ing", "영양보충제 함량", "additives per kg"]):
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
                    dict[key] = value.split('; ')[:]
                elif ', ' in value:
                    dict[key] = value.split(', ')[:]
            else:
                dict[key] = value
        I_am_on_the_next_level.append(dict)
with open("./purple_.json", 'w', encoding='UTF-8') as output:
    json.dump(I_am_on_the_next_level, output, indent=2,
              ensure_ascii=False, allow_nan=False)
