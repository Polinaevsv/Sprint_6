import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Оформление заказа')
    def set_order(self, order_data):
        self.click_to_element(OrderPageLocators.ORDER_INPUT_NAME)
        self.add_text_to_element(OrderPageLocators.ORDER_INPUT_NAME, order_data[0])
        self.click_to_element(OrderPageLocators.ORDER_INPUT_SURNAME)
        self.add_text_to_element(OrderPageLocators.ORDER_INPUT_SURNAME, order_data[1])
        self.click_to_element(OrderPageLocators.ORDER_INPUT_ADDRESS)
        self.add_text_to_element(OrderPageLocators.ORDER_INPUT_ADDRESS, order_data[2])
        self.click_to_element(OrderPageLocators.ORDER_INPUT_METRO_STATION)
        self.click_to_element(OrderPageLocators.ORDER_METRO_STATION_7)
        self.click_to_element(OrderPageLocators.ORDER_INPUT_PHONE_NUMBER)
        self.add_text_to_element(OrderPageLocators.ORDER_INPUT_PHONE_NUMBER, order_data[3])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_NEXT)
        self.click_to_element(OrderPageLocators.ORDER_INPUT_WHEN_TO_BRING)
        self.add_text_to_element(OrderPageLocators.ORDER_INPUT_WHEN_TO_BRING, order_data[4])
        self.click_to_element(OrderPageLocators.ORDER_DATE_DELIVERY)
        self.click_to_element(OrderPageLocators.ORDER_INPUT_RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.ORDER_RENTAL_PERIOD_THREES_DAY)
        self.click_to_element(OrderPageLocators.ORDER_CHECKBOX_COLOR_SCOOTER)
        self.click_to_element(OrderPageLocators.ORDER_INPUT_COMMENT_FOR_COURIER)
        self.add_text_to_element(OrderPageLocators.ORDER_INPUT_COMMENT_FOR_COURIER, order_data[5])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_ORDER)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_YES)
