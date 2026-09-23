from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#Переход в личный кабинет. Проверь переход по клику на «Личный кабинет».
def test_personal_account_button(driver): 
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


#Переход из личного кабинета в конструктор. 
#Проверь переход по клику на «Конструктор»...
def test_personal_account_constructor_button(driver): 
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

    #кликаем на "Конструктор"
    profile_page = ProfilePage(driver)
    profile_page.click_on_constructor()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

#...и на логотип Stellar Burgers. 
def test_personal_account_logo_button(driver): 
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

    #кликаем на лого "Stellar Burgers"
    profile_page = ProfilePage(driver)
    profile_page.click_on_logo()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

#Выход из аккаунта. Проверь выход по кнопке «Выйти» в личном кабинете.
def test_personal_account_exit_button(driver): 
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

    #Выходим из профиля
    profile_page = ProfilePage(driver)
    profile_page.click_on_exit()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/login"
    
    