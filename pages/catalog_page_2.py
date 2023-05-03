import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
import pickle

class Catalog_page(Base):
    driver = webdriver.Chrome()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_btn = "div.HeaderToolBar_toolbarWrapper__4CGaZ div.HeaderToolBar_buttons__d6ACX"
    otdohni_sidebar = ".ShopLayout_main__XP7jH .SidebarCatalog_tabsWrapper__zTBVJ a:nth-child(2)"
    myasnov_sidebar = ".ShopLayout_main__XP7jH .SidebarCatalog_tabsWrapper__zTBVJ a:nth-child(1)"
    sections_page_images = ".ShopLayout_sectionContent__ImaK5 .SectionPage_sectionList__p2iei" #секции каталога
    sections_page = ".SectionsList_listItem__UxUUY"

    #Getters

    def button_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog_btn)))

    def otdohni_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.otdohni_sidebar)))

    def sections_page_find(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.sections_page)))
    # print("разделы в левом меню есть")

    def sections_page_images_find(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.sections_page_images)))



    #Actions - действия

    def button_catalog_click(self):
        self.button_catalog().click()
        time.sleep(5)
        print("Нажали на кнопку Каталога")

    def assert_url_myasnov(self, result): #проверка, что открыта страница каталог Мяснов
        get_url = self.driver.current_url
        assert get_url == result
        print("Cсылка верная, открыт каталог Мяснов")


    def otdohni_btn_click(self):
        self.otdohni_btn().click()
        time.sleep(5)
        print("Нажали на кнопку Отдохни в сайдбаре")

    def assert_url_otdohni(self, result): #проверка, что открыта страница каталог Отдохни
        get_url = self.driver.current_url
        assert get_url == result
        print("Cсылка верная, открыт каталог Отдохни")

    def sections_page_find_1(self):
        self.sections_page_find()
        print("Разделы есть")
        time.sleep(5)

    def sections_page_images_find_1(self):
        self.sections_page_images_find()
        print("Разделы с картинками есть")
        time.sleep(3)

    #Metods - методы, что делаем

    def catalog(self):
        self.get_current_url()
        self.button_catalog_click()
        self.assert_url_myasnov("https://www.coolclever.ru/catalog/myasnov")
        #self.otdohni_btn_click()
        #self.assert_url_otdohni("https://www.coolclever.ru/catalog/otdokhni")
        self.sections_page_find_1()
        self.sections_page_images_find_1()






