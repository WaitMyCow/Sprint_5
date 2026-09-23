from selenium.webdriver.common.by import By

class HomePageLocators:
    CABINET_BUTTON = [By.XPATH, "//a[@href='/account']"]
    ENTER_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    #найти div в котором есть class содержащий tab_tab__ и внутри этого элемента (.) найти span с текстом "Булки"
    BUNS_BUTTON = [By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Булки']]"]
    SAUCES_BUTTON = [By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Соусы']]"]
    FILLING_BUTTON = [By.XPATH, "//div[contains(@class, 'tab_tab__') and .//span[text()='Начинки']]"]
