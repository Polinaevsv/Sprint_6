import allure
import pytest
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPageSamokat
from data import TestData

class TestOrderPageCreateOrder:
    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Проверка функциональности оформления заказа из двух точек входа')
    @pytest.mark.parametrize(
        'locator_button_order, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_IN_HEADER, TestData.test_data_user1),
            (MainPageLocators.ORDER_BUTTON_IN_SECTION_HOW_IT_WORKS, TestData.test_data_user2)
        ]
    )
    def test_create_order(self, driver, locator_button_order, order_data):
        main_page = MainPageSamokat(driver)
        order_page = OrderPage(driver)
        main_page.click_to_element(MainPageLocators.BUTTON_COOKIE)
        main_page.click_to_element(locator_button_order)
        order_page.set_order(order_data)
        assert order_page.check_displaying_of_element(OrderPageLocators.ORDER_CHECK_STATUS_OF_ORDER)
