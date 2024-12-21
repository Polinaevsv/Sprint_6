import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.dzen_page_locators import DzenPageLocators
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPage

class TestRedirect:
    @allure.title('Проверка редиректов')
    @allure.description(
        'Проверка редиректа на главную страницу при клике на логотип "Самоката"')
    def test_redirect_on_main_page_scooter_by_clicking_on_logo_scooter(self, driver):
        main_page = MainPageSamokat(driver)
        order_page = OrderPage(driver)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)
        order_page.find_element_with_wait(OrderPageLocators.ORDER_TITLE_OF_FORM_FOR_WHOM_IS_SCOOTER)
        order_page.click_to_element(MainPageLocators.LOGO_SCOOTER_IN_HEADER)
        assert main_page.find_element_with_wait(MainPageLocators.QUESTIONS_SECTION)

    @allure.title('Проверка редиректов')
    @allure.description(
        'Проверка открытия в новом окне страницы Дзена при клике по лого "Яндекса')
    def test_redirect_on_main_page_dzen_by_clicking_on_logo_yandex(self, driver):
        main_page = MainPageSamokat(driver)
        main_page.click_to_element(MainPageLocators.LOGO_YANDEX_IN_HEADER)
        main_page.switch_to_next_tab()
        assert main_page.find_element_with_wait(DzenPageLocators.HEADER_DZEN)