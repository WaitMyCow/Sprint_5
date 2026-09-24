from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    LOGIN_FIELD = [By.XPATH, "//input[@name='name']"] 
    EMAIL_FIELD = [By.XPATH, "//div[label[text()='Email']]/input"]
    PASSWORD_FIELD = [By.XPATH, "//input[@name='Пароль']"]
    REGISTRATION_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"]
    LOGIN_BUTTON = [By.XPATH, "//a[@href='/login']"]
    WRONG_PASSWORD_LABEL = [By.XPATH, "//*[text()='Некорректный пароль']"]
