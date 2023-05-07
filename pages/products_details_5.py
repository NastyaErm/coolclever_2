import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Products_details(Base):
    driver = webdriver.Chrome()

    def __init__(self, driver):
        super().__init__(driver)
        self.webdriver = webdriver
        self.driver = driver

    #Locators

    basket_setup_header = "//div[@class='BasketSetupWidget_wrapper__44onx']"

    #Getters

    def basket_setup(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.basket_setup_header)))

    # Actions - действия

    def basket_setup_click(self):
        self.basket_setup().click()
        print("Клик на баскет сетап")
        time.sleep(5)

