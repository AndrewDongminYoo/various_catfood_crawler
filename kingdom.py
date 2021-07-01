with open('./catkingdom1.txt', 'r', encoding='utf8', newline="") as input:
    line_list = []
    for line in input.readlines():
        if "category=007" in line or "category=008" in line or "category" not in line:
            line_list.append(line)
with open('./catkingdom1.txt', 'w', encoding='utf8', newline="") as output:
    for li in line_list:
        output.write(li)
