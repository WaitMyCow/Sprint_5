from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from ulrs import Urls
from utils import Utils

class TestPersonalAccount:
    #Переход в личный кабинет. Проверь переход по клику на «Личный кабинет».
    def test_personal_account_button(driver): 
        #Кнопка «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Авторизация
        login_page = LoginPage(driver)
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()
        assert home_page.get_current_url() == Urls.ACCOUNT_URL


    #Переход из личного кабинета в конструктор. 
    #Проверь переход по клику на «Конструктор»...
    def test_personal_account_constructor_button(driver): 
        #Кнопка «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Авторизация
        login_page = LoginPage(driver)
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()

        #кликаем на "Конструктор"
        profile_page = ProfilePage(driver)
        profile_page.click_on_constructor()
        assert home_page.get_current_url() == Urls.BASE_URL

    #...и на логотип Stellar Burgers. 
    def test_personal_account_logo_button(driver): 
        #Кнопка «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Авторизация
        login_page = LoginPage(driver)
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()

        #кликаем на лого "Stellar Burgers"
        profile_page = ProfilePage(driver)
        profile_page.click_on_logo()
        assert home_page.get_current_url() == Urls.BASE_URL

    #Выход из аккаунта. Проверь выход по кнопке «Выйти» в личном кабинете.
    def test_personal_account_exit_button(driver): 
        #Кнопка «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Авторизация
        login_page = LoginPage(driver)
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()

        #Выходим из профиля
        profile_page = ProfilePage(driver)
        profile_page.click_on_exit()
        profile_page.wait_for_url(Urls.LOGIN_URL)
        assert home_page.get_current_url() == Urls.LOGIN_URL
    
    