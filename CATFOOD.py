import pandas as pd
import matplotlib.pyplot as plt
import json

catpre = open('./json/CATPRESIDENT.json', 'r', encoding='utf8', newline="")
president = json.load(catpre)
brands_table = pd.DataFrame(data=president['brands'], columns=['id', 'name'])
ID_brands = brands_table.set_index('id')['name']
options_table = pd.DataFrame(data=president['options'])
options_table.set_index('id', inplace=True)
content_table = pd.DataFrame(data=president['content']['content'])
content_table.dropna(axis=1, how="any", inplace=True)
content_table['Brand'] = content_table['productBrandId'].map(ID_brands)
print(content_table['Brand'].unique())
print(content_table.columns)
