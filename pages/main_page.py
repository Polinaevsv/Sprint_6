import allure
from locators.main_page_locators import MainPageLocators
from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPageSamokat(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_question_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_to_element(locator_question_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_answer_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_answer_formatted)

    @allure.step('Проверка ответа')
    def check_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Cкролл до последнего вопроса')
    def scroll_to_last_question(self):
        element = self.driver.find_element(*MainPageLocators.QUESTION_8)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Клик по кнопке принятия кук')
    def click_to_cookie(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.BUTTON_COOKIE))
        return self.driver.find_element(*MainPageLocators.BUTTON_COOKIE).click()

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_to_order_button_in_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_IN_HEADER))
        return self.driver.find_element(*MainPageLocators.ORDER_BUTTON_IN_HEADER).click()

    @allure.step('Поиск секции "Вопросы о важном"')
    def find_question_section(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.QUESTIONS_SECTION))
        return self.driver.find_element(*MainPageLocators.QUESTIONS_SECTION)

    @allure.step('Клик по лого "Яндекса" в хэдере')
    def click_to_logo_yandex_in_header(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.LOGO_YANDEX_IN_HEADER))
        return self.driver.find_element(*MainPageLocators.LOGO_YANDEX_IN_HEADER).click()

    @allure.step('Поиск хэдера "Дзена"')
    def find_header_dzen(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            DzenPageLocators.HEADER_DZEN))
        return self.driver.find_element(*DzenPageLocators.HEADER_DZEN)