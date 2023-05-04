import pickle
import time
import pytest
from selenium import webdriver
from webdriver_manager import drivers
from webdriver_manager.chrome import ChromeDriverManager
from pages.basket_page_3 import Basket_page
from pages.catalog_page_2 import Catalog_page
from pages.items_page_4 import Items_page
from pages.login_page_1 import Login_page
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service('path/to/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
def test_login_page():

    driver = webdriver.Chrome()

    # авторизация для сохранения кук
    login = Login_page(driver)
    login.autorization_without_cookie()
    pickle.dump(driver.get_cookies(), open("cookies_01.pkl", "wb"))
    print("куки сохранены")
    time.sleep(5)

    # авторизация с уже сохраненными куками
    # login = Login_page(driver)
    # login.autorization_with_cookie()
    # for cookie in pickle.load(open("cookies_01.pkl", "rb")):
    #     driver.add_cookie(cookie)
    # time.sleep(5)
    # drivers.get("https://www.coolclever.ru/")
    # time.sleep(7)

    cp = Catalog_page(driver)
    cp.catalog()

    bp = Basket_page(driver)
    bp.empty_basket()

    ip = Items_page(driver)
    ip.products()
    driver.quit()







