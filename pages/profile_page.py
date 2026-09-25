from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_exit(self):
        self.click_element(ProfilePageLocators.EXIT_BUTTON)

    def click_on_constructor(self):
        self.click_element(ProfilePageLocators.CONSTRUCTION_BUTTON)

    def click_on_logo(self):
        self.click_element(ProfilePageLocators.LOGO_BUTTON)