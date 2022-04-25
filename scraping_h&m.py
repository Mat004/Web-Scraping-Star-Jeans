import time
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bts
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


#########################################################
# Auxiliar Functions
#########################################################

def main_website(total_vitrine, size, composition, materials, number_art, fit, price, color, name, price_new):

    for i in range(1, total_vitrine+1):

        time.sleep(2)
        try:
            url ="/html/body/main/div/div/div/div[3]/ul/li[" + str(i) + "]/article/div[1]/a/img"
            ad1 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, url)))
            ad1.click()

            for j in range(1, 10):
                time.sleep(2)
                try:
                    url1 = "/html/body/main/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]/ul/li[1]/ul/li[" + str(j) + "]/a"
                    ad1 = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, url1)))
                    ad1.click()

                    try:
                        first = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dt'))).text
                        if first == "Size":

                            size.append(WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)
                        else:
                            size.append("NaN")
                    except:
                        None

                    try:
                        second = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]/dt'))).text
                        if first == "Fit":
                            fit.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)

                        elif second == "Fit":
                            fit.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]/dd'))).text)
                        else:
                            fit.append("NaN")
                    except:
                        if first == "Fit":
                            fit.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)
                        else:
                            fit.append("NaN")
                    try:
                        third = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[3]/dt'))).text
                        if first == "Composition":
                            composition.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]'))).text)
                        elif second == "Composition":
                            composition.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]'))).text)
                        elif third == "Composition":
                            composition.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[3]'))).text)
                        else:
                            composition.append("NaN")
                    except:
                        if first == "Composition":
                            composition.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]'))).text)
                        elif second == "Composition":
                            composition.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]'))).text)
                        else:
                            composition.append("NaN")

                    try:
                        fourth = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[4]/dt'))).text
                        if first == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)
                        elif second == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]/dd'))).text)
                        elif third == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[3]/dd'))).text)
                        elif fourth == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[4]/dd'))).text)
                        else:
                            materials.append("NaN")
                    except:
                        if first == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)
                        elif second == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]/dd'))).text)
                        elif third == "More sustainable materials":
                            materials.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[3]/dd'))).text)
                        else:
                            materials.append("NaN")

                    try:
                        fifth = WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[5]/dt'))).text
                        if first == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)
                        elif second == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]/dd'))).text)
                        elif third == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[3]/dd'))).text)
                        elif fourth == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[4]/dd'))).text)
                        elif fifth == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[5]/dd'))).text)
                        else:
                            number_art.append("NaN")

                    except:
                        if first == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[1]/dd'))).text)
                        elif second == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[2]/dd'))).text)
                        elif third == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[3]/dd'))).text)
                        elif fourth == "Art. No.":
                            number_art.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                    (By.XPATH, '//*[@id="js-product-description"]/div/dl/div[4]/dd'))).text)
                        else:
                            number_art.append("NaN")

                    try:
                        price.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="product-price"]/div/span'))).text)
                    except:
                        price.append("NaN")

                    try:
                        price_new.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="product-price"]/div/span[2]'))).text)
                    except:
                        price_new.append("NaN")

                    try:
                        color.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/h3'))).text)
                    except:
                        color.append("NaN")

                    try:
                        name.append(WebDriverWait(driver, 1).until(EC.presence_of_element_located(
                                (By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/div[1]/div[1]/div/section/h1'))).text)
                    except:
                        color.append("NaN")
                except:
                    break

            time.sleep(2)

            driver.execute_script("window.history.go(-1)")

        except:
            break


    return size, fit, composition, materials, number_art, price, color, name, price_new


#########################################################
# 0 - Getting page number
#########################################################

url_i = 'https://www2.hm.com/en_us/men/products/jeans.html'
headers = {
            'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
          }

page_i = requests.get(url_i, headers=headers)
soup_i = bts(page_i.text, 'html.parser')

total_page = soup_i.find('h2', class_='load-more-heading')
items = int(total_page.get('data-items-shown'))
total_vitrine = int(total_page.get('data-total'))
total_page_number = np.ceil(int(total_page.get('data-total')) / items)

url = url_i + "?page-size=" + str(int(total_page_number*items))


#########################################################
# 1 - Opening Website
#########################################################

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--start-maximized")


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url)

time.sleep(2)

#########################################################
# 2 - Accept "Cookies"
#########################################################

try:
    cookie = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
    cookie.click()
except:
    None


#########################################################
# 3 - Extracting data
#########################################################

size = []
fit = []
composition = []
materials = []
number_art = []
price = []
color = []
name = []
price_new = []

main_website(total_vitrine, size, composition, materials, number_art, fit, price, color, name, price_new)

driver.quit()

#########################################################
# 4 - Creating dataframe
#########################################################

data1 = pd.DataFrame([number_art, name, price, price_new,color, fit, size, materials, composition]).T
data1.columns = ['product_id', 'product_name', 'product_price', 'product_price_new', 'product_color', 'product_fit',
                 'product_size', 'product_materials', 'product_composition']

data1['data_scrapy'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

data = pd.read_csv('data.csv')

data_final = pd.concat([data1, data], axis=0, ignore_index=True)

data_final.to_csv('data.csv', index=False)
