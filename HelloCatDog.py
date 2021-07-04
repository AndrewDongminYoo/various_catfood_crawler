from selenium import webdriver
import json
import time
from bs4 import BeautifulSoup


# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.set_window_size(height=1900, width=900)
driver.minimize_window()
driver.implicitly_wait(10)

category = ['002', '021']
dried_wet = dict()
for cate in category:
    driver.get(
        f'https://www.hellocatdog.com/goods/goods_list.php?cateCd={cate}&pageNum=250')
    time.sleep(5)
    diction = dict()
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # scrollHeight 까지 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 새로운 내용 로딩될때까지 기다림
        time.sleep(5)
        # 새로운 내용 로딩됐는지 확인
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.select(
        '#contents > div > div.content > div.goods_list_item > div.goods_list > div > div.item_basket_type > ul > li > div > div.PJ_good_table > div > div.item_tit_box > a')
    for link in links:
        if link.text not in diction.keys():
            diction[link.text] = link.get('href')
    if cate == '002':
        dried_wet['dried'] = diction
    else:
        dried_wet['wet'] = diction


with open('./cat_dog.json', 'w', encoding='utf8', newline="") as output:
    json.dump(dried_wet, output, ensure_ascii=False, sort_keys=True, indent=4)
