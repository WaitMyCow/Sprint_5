from pages.home_page import HomePage

#Проверь, что работают переходы к разделам:
class TestConstructor:
    #«Булки»,
    def test_constructor_buns_button(driver):
        home_page = HomePage(driver)
        home_page.click_on_sauces_button()
        home_page.click_on_buns_button()
        assert home_page.is_buns_button_selected()

    #«Соусы»,
    def test_constructor_sauces_button(driver): 
        home_page = HomePage(driver)
        home_page.click_on_sauces_button()
        assert home_page.is_sauces_button_selected()

    #«Начинки».
    def test_constructor_filling_button(driver): 
        home_page = HomePage(driver)
        home_page.click_on_filling_button()
        assert home_page.is_filling_button_selected()