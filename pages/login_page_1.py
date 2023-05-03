import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
import pickle

class Login_page(Base):
    driver = webdriver.Chrome()
    url = "https://www.coolclever.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    modal_18 = "//div[@class='ModalAdultConfirm_buttonWrapper__udfd7']"
    input_btn = "//button[@title='Личный кабинет']" #кнопка Войти
    input_wrapper = "//input[@inputmode='numeric']"
    getting_code = "//span[contains(text(),'Получить код')]"
    entrance_window = "//input[@inputmode='numeric']"
    input_btn_2 = "//div[@class='Login_firstBtn__SuPuM']"

    #Getters
    def modal_window(self):  #модалка 18 лет
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.modal_18)))

    def input_button(self):  #клик на Войти
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_btn)))

    def entering_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_wrapper)))

    def get_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.getting_code)))

    def entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entrance_window)))

    def input_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_btn_2)))


    #Actions - действия

    def modal_window_click(self): #клик на модалку 18 лет
        self.modal_window().click()
        print("Закрыли модалку Мне есть 18 лет")

    def input_button_click(self):
        self.input_button().click()
        print("Нажали на Войти")

    def entering_phone_number(self, number):
        self.entering_phone().send_keys(number)
        print("Ввели номер")

    def get_code_click(self):
        self.get_code().click()
        time.sleep(3)
        print("Нажали на получение кода")

    def entrance_click(self):
        self.entrance().click()

    def entrance_code(self):
        self.entrance().send_keys("0000")
        print("Ввели код")

    def input_button_2_click(self):
        self.input_button_2().click()
        print("Вход выполнен")
        time.sleep(5)

    def input_bth_check(self): #проверка пропала ли кнопка Войти
        if len(self.input_btn) > 0:
            print("Вход произведен")
        else:
            print("Вход не произведен")


    # pickle.dump(driver.get_cookies(), open("cookies_01.pkl", "wb"))
    # print("куки сохранены")
    # time.sleep(5)

    #Metods - методы, что делаем

    def autorization_without_cookie(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.modal_window_click()
        self.input_button_click()
        self.entering_phone_number("9200352271")
        self.get_code_click()
        self.entrance_click()
        self.entrance_code()
        self.input_button_2_click()
        self.input_bth_check()

    def autorization_with_cookie(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.modal_window_click()
        time.sleep(5)





