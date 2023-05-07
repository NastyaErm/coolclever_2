from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.products_details_5 import Products_details
from pages.login_page_1 import Login_page

service = Service('path/to/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = "https://www.coolclever.ru/"

def test_add_products():

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    lp = Login_page(driver)
    lp.modal_window_click()

    pd = Products_details(driver)
    pd.basket_setup_click()
    driver.quit()