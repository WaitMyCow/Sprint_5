from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="function") #scope - время жизни фикстуры. В данном случае она перезапускается для каждого теста (функции)
def driver():
    print("Создаём Chrome")
    driver = webdriver.Chrome()
    print("Chrome создан")
    driver.get("https://stellarburgers.education-services.ru/")
    print("Сайт открыт")
    yield driver
    driver.quit()