from selenium.webdriver.common.by import By

class ProfilePageLocators:
    EXIT_BUTTON = [By.XPATH, "//button[text()='Выход']"]
    CONSTRUCTION_BUTTON = [By.XPATH, "//a[p[text()='Конструктор']]"]
    #Ищем <a> с href="/", внутри которого нет <p> с текстом "Конструктор"
    LOGO_BUTTON = [By.XPATH, "//a[@href='/' and not(.//p[text()='Конструктор'])]"] 
   