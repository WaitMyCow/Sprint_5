from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.forgot_password_page import ForgotPasswordPage
from ulrs import Urls
from utils import Utils

#Проверь:
#вход по кнопке «Войти в аккаунт» на главной,
#вход через кнопку «Личный кабинет»,
#вход через кнопку в форме регистрации,
#вход через кнопку в форме восстановления пароля.
class TestLogin:
    #вход по кнопке «Войти в аккаунт» на главной
    def test_login_enter_in_account_button(driver): 
        #Кнопка «Войти в аккаунт»
        home_page = HomePage(driver)
        home_page.click_on_enter_button()
        #Авторизация
        login_page = LoginPage(driver)
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()
        assert home_page.get_current_url() == Urls.ACCOUNT_URL

    #вход через кнопку «Личный кабинет»
    def test_login_personal_account_button(driver): 
        #Кнопка «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Авторизация
        login_page = LoginPage(driver)
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()
        assert home_page.get_current_url() == Urls.ACCOUNT_URL

    #вход через кнопку в форме регистрации
    def test_registration_page_login_button(driver): 
        #вход через кнопку «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Зарегистрироваться
        login_page = LoginPage(driver)
        login_page.click_on_registration_button()
        #Нажимаем "Вход"
        register_page = RegisterPage(driver)
        register_page.login_button_click()
        #Авторизация
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()
        assert home_page.get_current_url() == Urls.ACCOUNT_URL

    #вход через кнопку в форме восстановления пароля.
    def test_forgot_password_login_button(driver):
        #вход через кнопку «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Восстановить пароль
        login_page = LoginPage(driver)
        login_page.click_on_forgot_password_button()
        #Вспомнили пароль? Войти
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.click_on_login()
        #Авторизация
        login_page.login_in(Utils.my_email(), Utils.my_password())
        #Входим в профиль
        home_page.click_on_cabinet_button()
        assert home_page.get_current_url() == Urls.ACCOUNT_URL