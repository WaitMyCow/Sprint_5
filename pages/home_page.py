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

    #Нажать кнопку "Булки"
    def click_on_buns_button(self):
        self.click_element(HomePageLocators.BUNS_BUTTON)

    #Булки выбраны?
    def is_buns_button_selected(self):
        element = self.find_element(HomePageLocators.BUNS_BUTTON)
        return "tab_tab_type_current" in element.get_attribute("class")

    #Нажать кнопку "Соусы"
    def click_on_sauces_button(self):
        self.click_element(HomePageLocators.SAUCES_BUTTON)

    #Соусы выбраны?
    def is_sauces_button_selected(self):
        element = self.find_element(HomePageLocators.SAUCES_BUTTON)
        return "tab_tab_type_current" in element.get_attribute("class")
    
    #Нажать кнопку "Начинки"
    def click_on_filling_button(self):
        self.click_element(HomePageLocators.FILLING_BUTTON)

    #Начинки выбраны?
    def is_filling_button_selected(self):
        element = self.find_element(HomePageLocators.FILLING_BUTTON)
        return "tab_tab_type_current" in element.get_attribute("class")