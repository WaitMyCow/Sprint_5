from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from ulrs import Urls
from utils import Utils


class TestRegistration:
    #Успешная регистрация. 
    def test_registration(driver): 
        #вход через кнопку «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Зарегистрироваться
        login_page = LoginPage(driver)
        login_page.click_on_registration_button()
        #Регистрация
        register_page = RegisterPage(driver)
        register_page.registration(Utils.generate_name(), Utils.generate_email(), Utils.generate_password())
        register_page.wait_for_url(Urls.LOGIN_URL)
        assert register_page.get_current_url() == Urls.LOGIN_URL

    #Ввод менее 6 символов в поле пароль
    def test_password_length_lower_than_6(driver): 
        #вход через кнопку «Личный кабинет»
        home_page = HomePage(driver)
        home_page.click_on_cabinet_button()
        #Зарегистрироваться
        login_page = LoginPage(driver)
        login_page.click_on_registration_button()        
        #Попытка регистрации
        register_page = RegisterPage(driver)
        register_page.registration(Utils.generate_name(), Utils.generate_email(), Utils.generate_password_length_lower_than_6())
        assert register_page.is_password_wrong()

