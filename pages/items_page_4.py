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
    close_modal_btn = ".FreeDeliveryBanner_buttons__Af1VW button:nth-child(2)"
    filter_all_btn = "//span[contains(text(),'Все фильтры')]"
    filter_all_modal_window = "//div[@class='ModalFilter_formWarpper__aYwiJ']"
    filter_no_sugar_btn = "//label[@for='87442']" #фильтр без сахара
    #filter_ccal_slider = "#prices .rc-slider.rc-slider-horizontal .rc-slider-handle.rc-slider-handle-2"
    #filter_ccal_slider = "//*[@id='prices']/div/div/div[2]/div[5]"
    #filter_ccal_slider = driver.find_element(By.XPATH, "//*[@id='prices']/div/div/div[2]/div[5]")
    #all = "//div[@class='CatalogPage_productList__BC7TO']"


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

    # def slider_ccal_find(self):
    #     return WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, self.filter_ccal_slider)))


    # def filter_no_sugar_1(self):
    # #button2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Для детей')]")))
    #     button3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='87435']")))
    #     #button2.location_once_scrolled_into_view()
    #     #button3.click()
    #     time.sleep(3)
    #     #print("нажали на фильтр без сахара")

    def filter_ccal_active(self):
        #driver = webdriver.Chrome()
        ccal = ActionChains(driver)
        filter_ccal_slider = driver.find_element(By.XPATH, "//*[@id='prices']/div/div/div[2]/div[5]")

        #ccal.click_and_hold(self.slider_ccal_find()).move_by_offset(10, 0).release().perform()
        ccal.drag_and_drop_by_offset(filter_ccal_slider, 50, 0).perform()

        time.sleep(3)
        #ccal.click_and_hold(piano_thumb).move_by_offset(-200, 0).release().perform()





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

    #Metods - методы, что делаем

    def products(self):
        self.all_products_click()
        self.all_sections_find()
        self.filter_cheap_click()
        self.filter_expensive_click()
        #self.all_sections_find()
        #self.filter_hits_click()
        self.all_sections_find()
        self.close_modal_click()
        self.all_filter_click()
       # self.filter_no_sugar_1()
        self.filter_ccal_active()








