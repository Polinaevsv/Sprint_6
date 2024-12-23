import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

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
        self.scroll_to_element(MainPageLocators.QUESTION_8)

    @allure.step('Клик по кнопке принятия кук')
    def click_to_cookie(self):
        self.click_to_element(MainPageLocators.BUTTON_COOKIE)

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_to_order_button_in_header(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Поиск секции "Вопросы о важном"')
    def find_question_section(self):
        return self.find_element_with_wait(MainPageLocators.QUESTIONS_SECTION)

    @allure.step('Клик по лого "Яндекса" в хэдере')
    def click_to_logo_yandex_in_header(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX_IN_HEADER)
