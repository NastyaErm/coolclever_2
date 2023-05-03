import pickle
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.basket_page_3 import Basket_page
from pages.catalog_page_2 import Catalog_page
from pages.items_page_4 import Items_page
from pages.login_page_1 import Login_page
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def test_login_page():
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #s = Service('C:\\Users\\anast\\chromedriver.exe')
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # login = Login_page(driver)
    # login.autorization_without_cookie() #авторизация для сохранения кук
    # pickle.dump(driver.get_cookies(), open("cookies_01.pkl", "wb"))
    # print("куки сохранены")
    # time.sleep(5)

    login = Login_page(driver)
    login.autorization_with_cookie() #авторизация с уже сохраненными куками
    for cookie in pickle.load(open("cookies_01.pkl", "rb")):
        driver.add_cookie(cookie)
    time.sleep(5)
    # driver.get("https://www.coolclever.ru/")
    # time.sleep(7)


    cp = Catalog_page(driver)
    cp.catalog()

    # bp = Basket_page(driver)
    # bp.empty_basket()

    ip = Items_page(driver)
    ip.products()








