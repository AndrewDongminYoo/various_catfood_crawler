from selenium.common.exceptions import NoSuchElementException, JavascriptException
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.set_window_size(height=1900, width=900)
driver.minimize_window()
driver.implicitly_wait(10)

# ws.append(['brand', 'formula', 'price', 'age', 'moisture_type', 'weight', 'main_ingredients', 'special_diets', 'calorie_content', 'manufacturer', 'check_point', 'kor_ingredients', 'eng_ingredients', 'caution', 'kor_analysis', 'eng_analysis', 'environment', 'recall', 'texture', 'package_img'])

# driver.get('https://www.purplesto.re/products/sales/list/?type=category&value=19')
# time.sleep(5)
# driver.execute_script("document.getElementById('catFilterBtn').setAttribute('aria-pressed','true');")
# link_list = []
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # scrollHeight 까지 스크롤
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # 새로운 내용 로딩될때까지 기다림
#     time.sleep(5)
#     # 새로운 내용 로딩됐는지 확인
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
# response = driver.page_source
# soup = BeautifulSoup(response, 'html.parser')
# links = soup.select('a.saleCard__link')
# for link in links:
#     if link.get('href') not in link_list:
#         link_list.append(link.get('href'))
# print(link_list)

sales_list = ['/products/sales/3542/', '/products/sales/4401/', '/products/sales/4400/', '/products/sales/4399/', '/products/sales/4398/', '/products/sales/4397/', '/products/sales/4396/', '/products/sales/4354/', '/products/sales/4353/', '/products/sales/4352/', '/products/sales/4351/', '/products/sales/4350/', '/products/sales/4349/', '/products/sales/4001/', '/products/sales/3998/', '/products/sales/3992/', '/products/sales/3840/', '/products/sales/3839/', '/products/sales/3838/', '/products/sales/3833/', '/products/sales/3832/', '/products/sales/3831/', '/products/sales/3804/', '/products/sales/3803/', '/products/sales/3802/', '/products/sales/3760/', '/products/sales/3759/', '/products/sales/3758/', '/products/sales/3741/', '/products/sales/3740/', '/products/sales/3739/', '/products/sales/3738/', '/products/sales/3737/', '/products/sales/3736/', '/products/sales/3735/', '/products/sales/3734/', '/products/sales/3733/', '/products/sales/3732/', '/products/sales/3731/', '/products/sales/3730/', '/products/sales/3729/', '/products/sales/3711/', '/products/sales/3710/', '/products/sales/3709/', '/products/sales/3708/', '/products/sales/3707/', '/products/sales/3706/', '/products/sales/3705/', '/products/sales/3704/', '/products/sales/3703/', '/products/sales/3702/', '/products/sales/3701/', '/products/sales/3685/', '/products/sales/3684/', '/products/sales/3683/', '/products/sales/3641/', '/products/sales/3640/', '/products/sales/3639/', '/products/sales/3638/', '/products/sales/3499/', '/products/sales/3495/', '/products/sales/3491/', '/products/sales/3487/', '/products/sales/3486/', '/products/sales/3457/', '/products/sales/3456/', '/products/sales/3455/', '/products/sales/3454/', '/products/sales/3449/', '/products/sales/3448/', '/products/sales/3447/', '/products/sales/3434/', '/products/sales/3298/', '/products/sales/3297/', '/products/sales/3296/', '/products/sales/3295/', '/products/sales/3286/', '/products/sales/3211/', '/products/sales/3014/', '/products/sales/3013/', '/products/sales/3012/', '/products/sales/3011/', '/products/sales/3004/', '/products/sales/3003/', '/products/sales/3002/', '/products/sales/3001/', '/products/sales/2993/', '/products/sales/2992/', '/products/sales/2991/', '/products/sales/2990/', '/products/sales/2989/', '/products/sales/2988/', '/products/sales/2974/', '/products/sales/2973/', '/products/sales/2972/', '/products/sales/2970/', '/products/sales/2967/', '/products/sales/2966/', '/products/sales/2948/', '/products/sales/2947/', '/products/sales/2938/', '/products/sales/2937/', '/products/sales/2918/', '/products/sales/2840/', '/products/sales/2839/', '/products/sales/2838/', '/products/sales/2837/', '/products/sales/2836/', '/products/sales/2835/', '/products/sales/2746/', '/products/sales/2745/', '/products/sales/2742/', '/products/sales/2741/', '/products/sales/2740/', '/products/sales/2705/', '/products/sales/2704/', '/products/sales/2703/', '/products/sales/2702/', '/products/sales/2701/', '/products/sales/2700/', '/products/sales/2699/', '/products/sales/2698/', '/products/sales/2697/', '/products/sales/2696/', '/products/sales/2695/', '/products/sales/1714/', '/products/sales/1716/', '/products/sales/2574/', '/products/sales/2573/', '/products/sales/1684/', '/products/sales/2542/', '/products/sales/2540/', '/products/sales/2539/', '/products/sales/1936/', '/products/sales/1935/', '/products/sales/1934/', '/products/sales/1932/', '/products/sales/1931/', '/products/sales/1930/', '/products/sales/1929/', '/products/sales/1928/', '/products/sales/1927/', '/products/sales/1926/', '/products/sales/1925/', '/products/sales/1870/', '/products/sales/1682/', '/products/sales/1598/', '/products/sales/1597/', '/products/sales/1596/', '/products/sales/1595/', '/products/sales/1594/', '/products/sales/1592/', '/products/sales/1591/', '/products/sales/1541/', '/products/sales/1540/', '/products/sales/1539/', '/products/sales/1538/', '/products/sales/1534/', '/products/sales/1533/', '/products/sales/1528/', '/products/sales/1527/', '/products/sales/1526/', '/products/sales/1525/', '/products/sales/1513/', '/products/sales/1512/', '/products/sales/1499/', '/products/sales/1498/', '/products/sales/1492/', '/products/sales/1491/', '/products/sales/1490/', '/products/sales/1472/', '/products/sales/1262/', '/products/sales/1259/', '/products/sales/1255/', '/products/sales/1252/', '/products/sales/1133/', '/products/sales/1132/', '/products/sales/1131/', '/products/sales/1130/', '/products/sales/1128/', '/products/sales/1127/', '/products/sales/1126/', '/products/sales/1125/', '/products/sales/1124/', '/products/sales/1042/', '/products/sales/1038/', '/products/sales/1034/', '/products/sales/1028/', '/products/sales/1027/', '/products/sales/1005/', '/products/sales/1004/', '/products/sales/970/', '/products/sales/901/', '/products/sales/900/', '/products/sales/899/']
url = "https://www.purplesto.re"
formulas_list = []
for link in sales_list:
    diction = {}
    driver.get(url + link)
    diction['id'] = len(formulas_list)
    diction['Manufacturer'] = driver.find_element(By.CLASS_NAME, 'productInfo__title').text
    diction['name_product'] = driver.find_element(By.CLASS_NAME, 'productInfo__name').text
    if any(number in diction['name_product'] for number in ['2종', '3종', '4종', '5종', '6종', '7종', '8종', '9종']):
        continue
    status = driver.find_element(By.CLASS_NAME, 'productInfo__soldout').get_attribute('style')
    if 'display: none' in status:
        diction['price'] = driver.find_element(By.XPATH, '//*[@id="product_price"]/div[1]').text
    else:
        diction['status'] = 'sold-out'
    indexes = driver.find_elements(By.CSS_SELECTOR, 'productSubInfo__detail-table__row .title')
    rows = driver.find_elements(By.CSS_SELECTOR, 'productSubInfo__detail-table__row .text')
    for key, value in zip(indexes, rows):
        diction[key] = value
    ingredientCheck = driver.find_elements(By.XPATH, '//*[@id="detailTab"]/section[1]/div[2]/div[2]/ul/li')
    check_list = []
    for check in ingredientCheck:
        check_list.append(check.text.strip())
    diction['good_point'] = check_list
    ingredientCheck = driver.find_elements(By.XPATH, '//*[@id="detailTab"]/section[1]/div[3]/div[2]/ul/li')
    check_list = []
    for check in ingredientCheck:
        check_list.append(check.text.strip())
    diction['bad_point'] = check_list
    try:
        driver.execute_script("document.getElementById('indredient_original').classList.add('show');")
    except JavascriptException:
        pass
    diction['korean_ing'] = driver.find_element(By.ID, 'indredient_korean').text
    diction['english_ing'] = driver.find_element(By.ID, 'indredient_original').text
    try:
        diction['caution'] = driver.find_element(By.CLASS_NAME, 'ingredientCheck__caution').text
    except NoSuchElementException:
        pass
    try:
        driver.execute_script("document.getElementById('nutrition_original').classList.add('show');")
    except JavascriptException:
        pass
    diction['ko_analysis'] = driver.find_element(By.XPATH, '//*[@id="nutrition_korean"]/div').text.split(', ')
    diction['en_analysis'] = driver.find_element(By.XPATH, '//*[@id="nutrition_original"]/div').text.split(', ')
    env_list = []
    environment = driver.find_elements(By.CSS_SELECTOR, '.safetyCheck__environment__container > ul > li')
    if len(environment) > 0:
        for env in environment:
            env_list.append(env.text.strip())
        diction['environment'] = env_list
    else:
        diction['environment'] = ""
    diction['recall_count'] = driver.find_element(By.CSS_SELECTOR, '.safetyCheck__content .productDetail__subtitle p .num').text.replace('건', '')
    if diction['recall_count'] == "0" or diction['recall_count'] == 0:
        diction['recallHistory'] = "No Recall"
        diction['recall_count'] = 0
    else:
        diction['recallHistory'] = driver.find_element(By.CSS_SELECTOR, '.safetyCheck__content-box > ul > li').text
    try:
        driver.execute_script("document.getElementById('brand_more').classList.add('show');")
    except JavascriptException:
        pass
    diction['brand_info'] = driver.find_element(By.XPATH, '//*[@id="brand_more"]/div').text
    diction['texture'] = driver.find_element(By.CLASS_NAME, 'feedingGuide__summary').text.replace('"', '')
    diction['infoImage'] = driver.find_element(By.CLASS_NAME, 'packageCheck__image').get_attribute('src')
    formulas_list.append(diction)
    print(len(formulas_list), diction['name_product'])
driver.quit()
with open('./PURPLE.json', 'w', encoding='utf8', newline="") as output_file:
    json.dump(formulas_list, output_file, indent=2, ensure_ascii=False)



