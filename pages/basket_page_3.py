import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
import pickle

class Basket_page(Base):
    driver = webdriver.Chrome()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    basket_btn = "//div[@class='HeaderToolBar_basket__EvY2T']" #кнопка корзины
    empty_basket_text = "//p[contains(text(),'В вашей корзине пока пусто')]"
    clear_basket_btn = "//span[contains(text(),'Очистить корзину')]"
    go_to_catalog_btn = "#__next > main > div > div > div > div.BasketEmptyView_buttonWrapper__uZe3m > a > div"

    #Getters

    def button_basket(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_btn)))


    #Actions - действия

    def button_basket_click(self):
        self.button_basket().click()
        time.sleep(5)
        print("Нажали на кнопку корзины")

    def assert_url_basket(self, result): #проверка, что открыта страница корзины
        get_url = self.driver.current_url
        assert get_url == result
        print("Cсылка верная, открыта корзина")

    def empty_basket_1(self): #пустая корзина
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.empty_basket_text)))

    def full_basket(self): #полная корзина
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.clear_basket_btn)))
    def full_basket_clear(self):
        self.full_basket().click()
        print("полная корзина очищена")

    def go_to_catalog(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.go_to_catalog_btn)))
    def go_to_catalog_click(self):
        self.go_to_catalog().click()
        print("перешли в каталог из пустой корзины ")

    def clear_basket(self): #очищаем полную корзину
        try:
            if self.empty_basket_1():
                self.go_to_catalog()
                self.go_to_catalog_click()
                time.sleep(5)
        except TimeoutException:
            self.full_basket_clear()


    #Metods - методы, что делаем

    def empty_basket(self):
        self.get_current_url()
        self.button_basket_click()
        self.assert_url_basket("https://www.coolclever.ru/basket")
        self.clear_basket()


