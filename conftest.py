from selenium import webdriver
from ulrs import Urls
import pytest


@pytest.fixture(scope="function") #scope - время жизни фикстуры. В данном случае она перезапускается для каждого теста (функции)
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()