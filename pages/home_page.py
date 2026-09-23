from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
#Главная страница
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #Личный кабинет
    def click_on_cabinet_button(self): 
        self.click_element(HomePageLocators.CABINET_BUTTON)

    #Кнопка "Войти в аккаунт"
    def click_on_enter_button(self):
        self.click_element(HomePageLocators.ENTER_BUTTON)

    #Булки
    def click_on_buns_button(self):
        self.click_element(HomePageLocators.BUNS_BUTTON)

    #Соусы
    def click_on_sauces_button(self):
        self.click_element(HomePageLocators.SAUCES_BUTTON)
        
    #Начинки 
    def click_on_filling_button(self):
        self.click_element(HomePageLocators.FILLING_BUTTON)