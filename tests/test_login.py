from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.forgot_password_page import ForgotPasswordPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Проверь:
#вход по кнопке «Войти в аккаунт» на главной,
#вход через кнопку «Личный кабинет»,
#вход через кнопку в форме регистрации,
#вход через кнопку в форме восстановления пароля.

#вход по кнопке «Войти в аккаунт» на главной
def test_login_enter_in_account_button(driver): 
    #Кнопка «Войти в аккаунт»
    home_page = HomePage(driver)
    home_page.click_on_enter_button()
    print("Войти в аккаунт нажат")
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    #Авторизация
    login_page = LoginPage(driver)
    login_page.login_in("1234q!")
    print("Пользователь вошёл")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"
        
    #Входим в профиль
    home_page.click_on_cabinet_button()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"


#вход через кнопку «Личный кабинет»
def test_login_personal_account_button(driver): 
    #Кнопка «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_cabinet_button()
    print("Личный кабинет нажат")
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    #Авторизация
    login_page = LoginPage(driver)
    login_page.login_in("1234q!")
    print("Пользователь вошёл")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"
        
    #Входим в профиль
    home_page.click_on_cabinet_button()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

#вход через кнопку в форме регистрации
def test_registration_page_login_button(driver): 
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
        
    #Нажимаем "Вход"
    register_page = RegisterPage(driver)
    register_page.login()

    #Авторизация
    login_page.login_in("1234q!")
    print("Пользователь вошёл")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    #Входим в профиль
    home_page.click_on_cabinet_button()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

def test_forgot_password_login_button(driver):
     #вход через кнопку «Личный кабинет»
    home_page = HomePage(driver)
    home_page.click_on_cabinet_button()
    print("Личный кабинет нажат")
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"

    #Восстановить пароль
    login_page = LoginPage(driver)
    login_page.click_on_forgot_password_button()
    print("Регистрация нажата")
    assert driver.current_url == "https://stellarburgers.education-services.ru/forgot-password"

    #Вспомнили пароль? Войти
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.click_on_login()

    #Авторизация
    login_page.login_in("1234q!")
    print("Пользователь вошёл")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    #Входим в профиль
    home_page.click_on_cabinet_button()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"