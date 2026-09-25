from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_registration_button(self):
        self.click_element(LoginPageLocators.REGISTRATION_BUTTON)

    def click_on_forgot_password_button(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD)

    def login_in(self, email, password):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)