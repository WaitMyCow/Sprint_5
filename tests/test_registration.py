from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



#Успешная регистрация. Не пройдёт если пользователь уже есть. 
#Заменить Имя Email можно в register_page.py, а пароль внутри тестов
def test_registration(driver): 
    #вход через кнопку «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_cabinet_button()
    print("Личный кабинет нажат")
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    #Зарегистрироваться
    login_page = LoginPage(driver)
    login_page.click_on_registration_button()
    print("Регистрация нажата")
    assert driver.current_url == "https://stellarburgers.education-services.ru/register"
        
    #Регистрация
    register_page = RegisterPage(driver)
    register_page.registration("1234q!") #корректный пароль
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

#Неверный пароль
def test_wrong_password_registration(driver): 
    #вход через кнопку «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_cabinet_button()
    print("Личный кабинет нажат")
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    #Зарегистрироваться
    login_page = LoginPage(driver)
    login_page.click_on_registration_button()
    print("Регистрация нажата")
    assert driver.current_url == "https://stellarburgers.education-services.ru/register"
        
    #Попытка регистрации
    register_page = RegisterPage(driver)
    register_page.registration("1234") #НЕ корректный пароль
    assert register_page.find_element((By.XPATH, "//*[text()='Некорректный пароль']")).text == "Некорректный пароль"

