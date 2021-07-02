from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 1)
wb = Workbook()
ws = wb.active
# ws.append(['brand', 'formula', 'price', 'age', 'moisture_type', 'weight', 'main_ingredients', 'special_diets', 'calorie_content', 'manufacturer', 'check_point', 'kor_ingredients', 'eng_ingredients', 'caution', 'kor_analysis', 'eng_analysis', 'environment', 'recall', 'texture', 'package_img'])

# driver.get('https://www.purplesto.re/products/sales/list/?type=name&value=%EC%A2%85')
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


url = "https://www.purplesto.re"
sales_list = ['/products/sales/4030/', '/products/sales/4029/', '/products/sales/4028/', '/products/sales/4027/',
              '/products/sales/4026/', '/products/sales/4025/', '/products/sales/4001/', '/products/sales/3998/', '/products/sales/3992/', '/products/sales/3840/', '/products/sales/3839/', '/products/sales/3838/', '/products/sales/3833/', '/products/sales/3832/', '/products/sales/3831/', '/products/sales/3804/', '/products/sales/3803/', '/products/sales/3802/', '/products/sales/3760/', '/products/sales/3759/', '/products/sales/3758/', '/products/sales/3741/', '/products/sales/3740/', '/products/sales/3739/', '/products/sales/3738/', '/products/sales/3737/', '/products/sales/3736/', '/products/sales/3735/', '/products/sales/3734/', '/products/sales/3733/', '/products/sales/3732/', '/products/sales/3731/', '/products/sales/3730/', '/products/sales/3729/', '/products/sales/3711/', '/products/sales/3710/', '/products/sales/3709/', '/products/sales/3708/', '/products/sales/3707/', '/products/sales/3706/', '/products/sales/3705/', '/products/sales/3704/', '/products/sales/3703/', '/products/sales/3702/', '/products/sales/3701/', '/products/sales/3685/', '/products/sales/3684/', '/products/sales/3683/', '/products/sales/3641/', '/products/sales/3640/', '/products/sales/3639/', '/products/sales/3638/', '/products/sales/3499/', '/products/sales/3495/', '/products/sales/3491/', '/products/sales/3487/', '/products/sales/3457/', '/products/sales/3456/', '/products/sales/3455/', '/products/sales/3454/', '/products/sales/3449/', '/products/sales/3448/', '/products/sales/3447/', '/products/sales/3434/', '/products/sales/3298/', '/products/sales/3297/', '/products/sales/3296/', '/products/sales/3295/', '/products/sales/3286/', '/products/sales/3211/', '/products/sales/3014/', '/products/sales/3013/', '/products/sales/3012/', '/products/sales/3011/', '/products/sales/3004/', '/products/sales/3003/', '/products/sales/3002/', '/products/sales/3001/', '/products/sales/2993/', '/products/sales/2992/', '/products/sales/2991/', '/products/sales/2990/', '/products/sales/2989/', '/products/sales/2988/', '/products/sales/2974/', '/products/sales/2973/', '/products/sales/2972/', '/products/sales/2970/', '/products/sales/2967/', '/products/sales/2966/', '/products/sales/2948/', '/products/sales/2947/', '/products/sales/2945/', '/products/sales/2938/', '/products/sales/2937/', '/products/sales/2918/', '/products/sales/2840/', '/products/sales/2839/', '/products/sales/2838/', '/products/sales/2837/', '/products/sales/2836/', '/products/sales/2835/', '/products/sales/2746/', '/products/sales/2745/', '/products/sales/2742/', '/products/sales/2741/', '/products/sales/2740/', '/products/sales/2705/', '/products/sales/2704/', '/products/sales/2703/', '/products/sales/2702/', '/products/sales/2701/', '/products/sales/2700/', '/products/sales/2699/', '/products/sales/2698/', '/products/sales/2697/', '/products/sales/2696/', '/products/sales/2695/', '/products/sales/1714/', '/products/sales/1716/', '/products/sales/2574/', '/products/sales/2573/', '/products/sales/1683/', '/products/sales/1684/', '/products/sales/2542/', '/products/sales/2541/', '/products/sales/2540/', '/products/sales/2539/', '/products/sales/1936/', '/products/sales/1935/', '/products/sales/1934/', '/products/sales/1932/', '/products/sales/1931/', '/products/sales/1930/', '/products/sales/1929/', '/products/sales/1928/', '/products/sales/1927/', '/products/sales/1926/', '/products/sales/1925/', '/products/sales/1870/', '/products/sales/1686/', '/products/sales/1685/', '/products/sales/1681/', '/products/sales/1680/', '/products/sales/1604/', '/products/sales/1598/', '/products/sales/1597/', '/products/sales/1596/', '/products/sales/1595/', '/products/sales/1594/', '/products/sales/1592/', '/products/sales/1591/', '/products/sales/1541/', '/products/sales/1540/', '/products/sales/1539/', '/products/sales/1538/', '/products/sales/1534/', '/products/sales/1533/', '/products/sales/1528/', '/products/sales/1527/', '/products/sales/1526/', '/products/sales/1525/', '/products/sales/1513/', '/products/sales/1512/', '/products/sales/1505/', '/products/sales/1499/', '/products/sales/1498/', '/products/sales/1492/', '/products/sales/1491/', '/products/sales/1490/', '/products/sales/1472/', '/products/sales/1259/', '/products/sales/1255/', '/products/sales/1252/', '/products/sales/1133/', '/products/sales/1132/', '/products/sales/1131/', '/products/sales/1130/', '/products/sales/1128/', '/products/sales/1127/', '/products/sales/1126/', '/products/sales/1125/', '/products/sales/1124/', '/products/sales/1042/', '/products/sales/1038/', '/products/sales/1034/', '/products/sales/1028/', '/products/sales/1027/', '/products/sales/1005/', '/products/sales/1004/', '/products/sales/970/', '/products/sales/968/', '/products/sales/901/', '/products/sales/900/', '/products/sales/899/']
# brands_list = ['/products/brands/159/', '/products/brands/151/', '/products/brands/89/', '/products/brands/91/',
#                '/products/brands/99/', '/products/brands/65/', '/products/brands/64/', '/products/brands/53/', '/products/brands/55/', '/products/brands/78/', '/products/brands/138/', '/products/brands/84/', '/products/brands/127/', '/products/brands/124/', '/products/brands/120/', '/products/brands/59/', '/products/brands/67/', '/products/brands/75/', '/products/brands/86/', '/products/brands/72/', '/products/brands/57/', '/products/brands/54/']

ws.append(['Manufacturer', 'name_product', 'option[0]', 'price[0]', 'option[1]', 'price[1]', 'option[2]', 'price[2]'])
for link in sales_list:
    driver.get(url + link)
    actions = ActionChains(driver)
    Manufacturer = driver.find_element(By.CLASS_NAME, 'productInfo__title').text
    name_product = driver.find_element(By.CLASS_NAME, 'productInfo__name').text

# 실험용 코드
    if "종" not in name_product:
        continue
    driver.execute_script("document.getElementById('purchaseBtn').click();")
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "popupOptionSelectBtn")))
        driver.execute_script("document.getElementById('popupOptionSelectBtn').click();")
    except ElementClickInterceptedException:
        continue
    except TimeoutException:
        continue
    options = driver.find_elements(By.CLASS_NAME, 'purchasePopup__option__name')
    prices = driver.find_elements(By.CLASS_NAME, 'purchasePopup__option__price')
    opt_list = []
    for opt, pri in zip(options, prices):
        opt_list.extend([opt.text, pri.get_attribute('data-price')])
    if len(opt_list) <= 2:
        opt_list.extend(['', '', '', ''])
    elif len(opt_list) <= 4:
        opt_list.extend(['', ''])
    row = [Manufacturer, name_product]
    row.extend(opt_list)
    print(row)


# 실험용 코드

#     status = driver.find_element(By.CLASS_NAME, 'productInfo__soldout').get_attribute('style')
#     if 'display: none' in status:
#         price = driver.find_element(By.XPATH, '//*[@id="product_price"]/div[1]').text
#     else:
#         price = 'sold out'
#     try:
#         feeding_ages = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[0].text
#     except IndexError:
#         continue
#     moisture_wod = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[1].text
#     productWeight = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[2].text
#     main_ingredient = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[3].text
#     special_diet = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[4].text
#     calorie_cont = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[5].text
#     made_in_nation = driver.find_elements(By.CSS_SELECTOR, '.productSubInfo__detail-table__row .text')[6].text
#     ingredientCheck = driver.find_elements(By.CSS_SELECTOR, 'div.ingredientCheck__summary-content ul li')
#     check_list = []
#     for check in ingredientCheck:
#         check_list.append(check.text.replace('\n', ' '))
#     ingredientCheck = ", ".join(check_list)
#     driver.execute_script("document.getElementById('indredient_original').classList.add('show');")
#     korean_ = driver.find_element(By.ID, 'indredient_korean').text
#     english = driver.find_element(By.ID, 'indredient_original').text
#     try:
#         caution = driver.find_element(By.CLASS_NAME, 'ingredientCheck__caution').text
#     except NoSuchElementException:
#         caution = ""
#     driver.execute_script("document.getElementById('nutrition_original').classList.add('show');")
#     ko_analysis = driver.find_element(By.XPATH, '//*[@id="nutrition_korean"]/div').text
#     en_analysis = driver.find_element(By.XPATH, '//*[@id="nutrition_original"]/div').text
#     env_list = []
#     environment = driver.find_elements(By.CSS_SELECTOR, '.safetyCheck__environment__container > ul > li')
#     if len(environment) > 0:
#         for env in environment:
#             env_list.append(env.text.strip())
#         environment = ", ".join(env_list)
#     else:
#         environment = ""
#     recall_count = driver.find_element(By.CSS_SELECTOR, '.safetyCheck__content .productDetail__subtitle p .num').text
#     if recall_count == "0건":
#         recallHistory = ""
#     else:
#         recallHistory = driver.find_element(By.CSS_SELECTOR, '.safetyCheck__content-box > ul > li').text
#     texture_of = driver.find_element(By.CLASS_NAME, 'feedingGuide__summary').text
#     packageImage = driver.find_element(By.CLASS_NAME, 'packageCheck__image').get_attribute('src')
#     ws.append([Manufacturer, name_product, price, feeding_ages, moisture_wod, productWeight, main_ingredient, special_diet, calorie_cont, made_in_nation, ingredientCheck, korean_, english, caution, ko_analysis, en_analysis, environment, recallHistory, texture_of, packageImage])
#
# wb.save('퍼플스토어.xlsx')
# driver.quit()



