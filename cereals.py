import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from datetime import date
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
url = "https://www.luluhypermarket.com/en-ae"

# Maximize the window and access the URL
driver.maximize_window()
driver.get(url)

def loading(url):
    #Maximizes the size of the window
    driver.maximize_window()
    #Acceses the URL link
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(0.01)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new content to load
        time.sleep(random.randint(1,4))  # Adjust the sleep time if necessary

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(random.randint(2,4))
        if new_height == last_height:
            # If heights are the same, no more content is loading
            break
        
        last_height = new_height
    
    time.sleep(3)

def getting_data():
    products = driver.find_elements(By.XPATH, "//*[contains(@id, 'productName')]")
    price = driver.find_elements(By.XPATH, "//*[contains(@id, 'productPrice')]")
    try:
        category = driver.find_element(By.CLASS_NAME, "mb-1")
    except:
         category = "undefined"
    for x in products:
        product_names.append(x.text)
    for y in price:
        prices.append(y.text)
        categories.append(category.text)


product_names = []
prices = []
categories = []

ids_to_extract = ["https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-breakfast-spreads-cereals/c/HY00214914", 
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-breakfast-spreads-oats-bars/c/HY00214918",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-breakfast-spreads-jams/c/HY00214986",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-breakfast-spreads-honey/c/HY00214913",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-dressings-table-sauces-sides-salad-dressing/c/HY00214942",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-dressings-table-sauces-sides-bottled-olives-pickles/c/HY00214946",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-drinking-water/c/HY00214908",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-tea/c/HY00215230",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-coffee/c/HY00215232",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-softdrinks-juices/c/HY00214907",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-sports-energy-drinks/c/HY00214906",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-powdered-drinks/c/HY00214911",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-long-life-milk/c/HY00216092",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-dairy-alternatives/c/HY00216091",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-beverage-milk-powder/c/HY00216093",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-cooking-ingredients-sauces-and-cream/c/HY00214933",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-cooking-ingredients-oils-ghee/c/HY00214934",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-cooking-ingredients-salt-pepper/c/HY00215950",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-cooking-ingredients-pulses/c/HY00214935",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-cooking-ingredients-spices-herbs/c/HY00214936",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-cooking-ingredients-condiments/c/HY00214944",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-arabic/c/HY00115005",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-filipino/c/HY00115004",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-indian/c/HY00215003",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-korean/c/HY00115001",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-chinese/c/HY00215001",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-japanese/c/HY00115002",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-thai/c/HY00215999",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-mexican/c/HY00115006",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-italian/c/HY00115003",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-world-foods-other-ethnic/c/HY00214989",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-rice-pasta-noodles/c/HY00214958",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-rice-pasta-noodles/c/HY00214960",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-rice-pasta-noodles-soups/c/HY00214948",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-ice-cream/c/HY00215066",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-ready-meals-snacks/c/HY00215068",
                   "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-burgers/c/HY00505001",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-pastry-sheets-dough/c/HY00215065",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-meat-poultry/c/HY00215070",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-fruits-vegetables/c/HY00215074",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-dairy/c/HY00503001",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-frozen-fish-seafood/c/HY00215072",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-biscuits-confectionery/c/HY00214972",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-biscuits-confectionery-chocolate/c/HY00214974",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-biscuits-confectionery-candy/c/HY00214973",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-biscuits-confectionery-gums-mints/c/HY00214971",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-canned-foods-vegetables/c/HY00214922",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-canned-foods-beans/c/HY00214924",
                   "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-canned-foods-meat/c/HY00214926",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-canned-foods-fish/c/HY00214928",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-canned-foods-fruits/c/HY00214930",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-chips-snacks/c/HY00214964",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-chips-snacks/c/HY00214966",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-chips-snacks-popcorn/c/HY00214968",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-chips-snacks-nuts-dates/c/HY00216160",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-home-baking-sweeteners-products/c/HY00214952",
                  "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-cupboard-home-baking-sweeteners-sugar-other/c/HY00214954",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-milk/c/HY00216103",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-long-life-milk/c/HY00216114",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-alternatives/c/HY00216115",
                   "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-laban-flavoured-milk/c/HY00216083",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-yoghurt-chilled-desserts/c/HY00216084",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-cream/c/HY00216085",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese/c/HY00216095",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese-butter-margarine/c/HY00216094",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-dairy-eggs-cheese/c/HY00216096",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-ready-meals-bakes-grills/c/HY00216156",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-bakery-bread-basket/c/HY00216108",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-bakery-cake-house/c/HY00216109",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-bakery-arabic/c/HY00216110",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-bakery-asian/c/HY00216111",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-bakery-croissant-and-savories-corner/c/HY00216112",
                   "https://www.luluhypermarket.com/en-ae/fresh-food-bakery-healthy-bake-shop/c/HY00216113",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-juice-salads-pizzas/c/HY00216159",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-juice-salads-sandwiches-burger/c/HY00217443",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-juice-salads/c/HY00216145",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-delicatessen-cold-cuts-prepacked-cooked-meats/c/HY00216152",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-delicatessen-olives-pickles/c/HY00216153",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-delicatessen-indian-ready-mix/c/HY00216163",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-delicatessen-oriental/c/HY00216154",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-delicatessen-hummus-labneh-other-prepacked-deli/c/HY00216141",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-fruits-vegetables/c/HY00216101",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-fruits-vegetables/c/HY00216102",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-fruits-vegetables-salad/c/HY00600300",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-fruits-vegetables-fruit-cuts/c/HY01000600",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-meat-poultry-beef-veal/c/HY00216147",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-meat-poultry-lamb-mutton/c/HY00216148",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-meat-poultry-chicken/c/HY00216100",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-seafood-fish/c/HY00216149",
                  "https://www.luluhypermarket.com/en-ae/fresh-food-seafood-smoked-fish-dried/c/HY00216143"]

for povezava in ids_to_extract:
            loading(povezava)
            getting_data()

driver.close()

dataframe = pd.DataFrame()
dataframe["product_names"] = product_names
dataframe["prices"] = prices
dataframe["category"] = categories
dataframe = dataframe.set_index("product_names")

today = date.today()
current_year = today.year
current_month = today.month
current_day = today.day
#dataframe.to_csv("test.csv")
dataframe.to_csv(f"data_{str(current_day)}{str(current_month)}{str(current_year)}.csv")
