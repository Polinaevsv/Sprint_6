import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageSamokat
from data import TestData
class TestMainPageImportantQuestions:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description(
        'Проверка появления нужного текста ответа на соответствующий вопрос при клике по иконке развертывания')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions_and_answers(self, driver, num):
        main_page = MainPageSamokat(driver)
        main_page.click_to_element(MainPageLocators.BUTTON_COOKIE)
        main_page.scroll_to_element(MainPageLocators.QUESTION_8)
        main_page.click_to_question(num)
        main_page.get_answer_text(num)
        assert main_page.check_answer(num) == TestData.test_data_for_checking_answers_to_questions[num]
