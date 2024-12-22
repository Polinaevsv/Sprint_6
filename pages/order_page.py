import allure
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

    @allure.step('Клик по кнопке принятия кук')
    def click_to_cookie(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.BUTTON_COOKIE))
        return self.driver.find_element(*MainPageLocators.BUTTON_COOKIE).click()

    @allure.step('Проверка отображения кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_view_status(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_CHECK_STATUS_OF_ORDER).is_displayed()

    @allure.step('Поиск заголовка формы "Для кого самокат"')
    def find_title_of_form_for_whom_is_scooter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            OrderPageLocators.ORDER_TITLE_OF_FORM_FOR_WHOM_IS_SCOOTER))
        return self.driver.find_element(*OrderPageLocators.ORDER_TITLE_OF_FORM_FOR_WHOM_IS_SCOOTER)

    @allure.step('Клик по лого "Самоката" в хэдере')
    def click_to_logo_scooter_in_header(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGO_SCOOTER_IN_HEADER))
        return self.driver.find_element(*MainPageLocators.LOGO_SCOOTER_IN_HEADER).click()