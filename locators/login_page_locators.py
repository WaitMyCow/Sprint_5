from selenium.webdriver.common.by import By

class LoginPageLocators:
    REGISTRATION_BUTTON = [By.LINK_TEXT, "Зарегистрироваться"] #можно с XPATH [By.XPATH, "//a[@href='/register']"]
    EMAIL_FIELD = [By.XPATH, "//input[@name='name']"] 
    PASSWORD_FIELD = [By.XPATH, "//input[@name='Пароль']"]
    LOGIN_BUTTON = [By.XPATH, "//button[text()='Войти']"]
    FORGOT_PASSWORD = [By.XPATH, "//a[@href='/forgot-password']"]