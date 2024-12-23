import allure
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage

class TestRedirect:
    @allure.title('Проверка редиректов')
    @allure.description(
        'Проверка редиректа на главную страницу при клике на логотип "Самоката"')
    def test_redirect_on_main_page_scooter_by_clicking_on_logo_scooter(self, driver):
        main_page = MainPageSamokat(driver)
        order_page = OrderPage(driver)
        main_page.click_to_order_button_in_header()
        order_page.find_title_of_form_for_whom_is_scooter()
        order_page.click_to_logo_scooter_in_header()
        assert main_page.find_question_section()

    @allure.title('Проверка редиректов')
    @allure.description(
        'Проверка открытия в новом окне страницы Дзена при клике по лого "Яндекса')
    def test_redirect_on_main_page_dzen_by_clicking_on_logo_yandex(self, driver):
        main_page = MainPageSamokat(driver)
        dzen_page = DzenPage(driver)
        main_page.click_to_logo_yandex_in_header()
        main_page.switch_to_next_tab()
        assert dzen_page.find_header_dzen()