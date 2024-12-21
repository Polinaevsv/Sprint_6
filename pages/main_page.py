import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

@allure.title('Проверка содержимого ответов на вопросы')
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
