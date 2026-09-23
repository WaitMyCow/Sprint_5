from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def registration(self, password):
        name = 'Danila_Stepanov'
        email = 'Danila_Stepanov_53_140@yandex.ru'

        self.find_element(RegistrationPageLocators.LOGIN_FIELD).send_keys(name)
        self.find_element(RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        self.find_element(RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self.click_element(RegistrationPageLocators.REGISTRATION_BUTTON)

    def login(self):
        self.click_element(RegistrationPageLocators.LOGIN_BUTTON)
    