from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTIONS_SECTION = By.XPATH, "//div[text()='Вопросы о важном']" #локатор для заголовка раздела "Вопросы о важном"
    QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]' #локаторы для вопросов в разделе "Вопросы о важном"
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]' #локаторы для ответов в разделе "Вопросы о важном"
    QUESTION_8 = By.XPATH, '//div[@id="accordion__heading-7"]' #локатор для последнего вопроса в разделе "Вопросы о важном"

    ORDER_BUTTON_IN_HEADER = By.XPATH, "(//button[text()='Заказать'])[1]"  # локатор для кнопки "Заказть" в хедэре на главной странице
    ORDER_BUTTON_IN_SECTION_HOW_IT_WORKS = By.XPATH, "(//button[text()='Заказать'])[2]"  # локатор для кнопки "Заказть" в разделе "Как это работает" на главной странице

    BUTTON_COOKIE = By.XPATH, "(//button[text()='да все привыкли'])" #локатор для кнопки принятия кук

    LOGO_SCOOTER_IN_HEADER = By.XPATH, "//img[@alt='Scooter']" #локатор лого "Самоката" в хэдере
    LOGO_YANDEX_IN_HEADER = By.XPATH, "//img[@alt='Yandex']"  #локатор лого "Яндекса" в хэдере
