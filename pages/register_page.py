from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def registration(self, name, email, password):
        self.find_element(RegistrationPageLocators.LOGIN_FIELD).send_keys(name)
        self.find_element(RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        self.find_element(RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self.click_element(RegistrationPageLocators.REGISTRATION_BUTTON)

    def login_button_click(self):
        self.click_element(RegistrationPageLocators.LOGIN_BUTTON)

    def is_password_wrong(self):
        self.find_element(RegistrationPageLocators.WRONG_PASSWORD_LABEL)
        return True
    