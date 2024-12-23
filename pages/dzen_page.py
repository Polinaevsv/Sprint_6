import allure
from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage

class DzenPage(BasePage):
    @allure.step('Поиск хэдера "Дзена"')
    def find_header_dzen(self):
        return self.find_element_with_wait(DzenPageLocators.HEADER_DZEN)