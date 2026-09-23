from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Проверь, что работают переходы к разделам:
#«Булки»,
def test_constructor_buns_button(driver): 
    #вход через кнопку «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_buns_button
    assert "tab_tab_type_current" in driver.find_element(*HomePageLocators.BUNS_BUTTON).get_attribute("class")

#«Соусы»,
def test_constructor_sauces_button(driver): 
    #вход через кнопку «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_sauces_button()
    assert "tab_tab_type_current" in driver.find_element(*HomePageLocators.SAUCES_BUTTON).get_attribute("class")

#«Начинки».
def test_constructor_filling_button(driver): 
    #вход через кнопку «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_filling_button()
    assert "tab_tab_type_current" in driver.find_element(*HomePageLocators.FILLING_BUTTON).get_attribute("class")