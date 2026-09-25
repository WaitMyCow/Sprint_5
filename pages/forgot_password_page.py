from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_login(self):
        self.click_element(ForgotPasswordPageLocators.LOGIN_BUTTON)
    