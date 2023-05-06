import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Items_page(Base):
    driver = webdriver.Chrome()

    def __init__(self, driver):
        super().__init__(driver)
        self.webdriver = webdriver
        self.driver = driver

    # Locators

    all_products_btn = ".ShopLayout_sidebarWrapper__uqS00 .SectionsList_sectionList__LODPu [href='/catalog/myasnov/all']"
    all_products_short = ".CatalogPage_productList__BC7TO .ProductCard_card__Tgxo4" #короткие карточки
    filter_cheap_btn = ".swiper-slide.swiper-slide-next .SortTabs_tab__iI5DN" #сначала недорогие
    filter_expensive_btn = ".SortTabs_sortWrapper__EdOEN div:nth-child(3)" #сначала дорогие
    filter_hits_btn = ".SortTabs_sortWrapper__EdOEN div:nth-child(5)" #хиты
    close_modal_btn = ".GiftBanner_controls__wk_NU button:nth-child(2)"
    filter_all_btn = "//span[contains(text(),'Все фильтры')]"
    filter_all_modal_window = "//div[@class='ModalFilter_formWarpper__aYwiJ']"
    filter_italia_btn = "//label[@for='873380']" #фильтр италия
    filter_show_items = "/html/body/div[4]/div/div[2]/div[3]/button[1]" #показать отфильтрованные товары

    #Getters

    def all_products(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.all_products_btn)))

    def all_sections_1(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.all_products_short)))

    def filter_cheap(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_cheap_btn)))

    def filter_expensive(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_expensive_btn)))

    def filter_hits(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.filter_hits_btn)))

    def close_modal(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.close_modal_btn)))

    def filter_all(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_all_btn)))

    def filter_italia(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_italia_btn)))

    def filter_show(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_show_items)))


    # def filter_ccal_active(self):
    #
    #     ccal = ActionChains(driver)
    #     filter_ccal_slider = driver.find_element(By.XPATH, "//*[@id='prices']/div/div/div[2]/div[5]")
    #
    #     ccal.click_and_hold(self.slider_ccal_find()).move_by_offset(10, 0).release().perform()
    #     ccal.drag_and_drop_by_offset(filter_ccal_slider, 50, 0).perform()


    #Actions - действия

    def all_products_click(self):
        self.all_products().click()
        time.sleep(2)
        print("Нажали на кнопку Все товары в разделе")

    def all_sections_find(self):
        self.all_sections_1()
        print("Все короткие карточки пришли")
        time.sleep(2)

    def filter_cheap_click(self):
        self.filter_cheap().click()
        print("Нажали на сортировку Сначала недорогие")
        time.sleep(5)

    def filter_expensive_click(self):
        self.filter_expensive().click()
        print("Нажали на сортировку Сначала дорогие")
        time.sleep(2)

    def filter_hits_click(self):
        self.filter_hits().click()
        print("Нажали на сортировку Хиты")
        time.sleep(2)

    def close_modal_click(self):
        self.close_modal().click()
        print("закрыли модалку")
        time.sleep(2)

    def all_filter_click(self):
        self.filter_all().click()
        print("Нажали на кнопку Все фильтры")
        time.sleep(3)

    def italia_filter_click(self):
        self.filter_italia().click()
        print("Нажали на кнопку Без сахара")
        time.sleep(3)

    def filter_show_click(self):
        self.filter_show().click()
        print("Нажали на кнопку Показать ... товаров ")
        time.sleep(3)

    #Metods - методы, что делаем

    def products(self):
        self.all_products_click()
        self.all_sections_find()
        self.filter_cheap_click()
        self.filter_expensive_click()
        #self.all_sections_find()
        self.filter_hits_click()
        self.all_sections_find()
        self.close_modal_click()
        self.all_filter_click()
        self.italia_filter_click()
        self.filter_show_click()









