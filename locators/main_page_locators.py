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







    #SECTION_IMPORTANT_QUESTIONS = [By.XPATH, "//div[text()='Вопросы о важном']"] #локатор для секции "Вопросы о важном"

    #локаторы для вопросов секции "Вопросы о важном"
    #QUESTION_ITEMS = {
        #1: (By.XPATH, "//div[@id='accordion__heading-0']"),
        #2: (By.XPATH, "//div[@id='accordion__heading-1']"),
        #3: (By.XPATH, "//div[@id='accordion__heading-2']"),
        #4: (By.XPATH, "//div[@id='accordion__heading-3']"),
        #5: (By.XPATH, "//div[@id='accordion__heading-4']"),
        #6: (By.XPATH, "//div[@id='accordion__heading-5']"),
       # 7: (By.XPATH, "//div[@id='accordion__heading-6']"),
       # 8: (By.XPATH, "//div[@id='accordion__heading-7']")
    #}

    # локаторы для ответов на вопросы секции "Вопросы о важном"
    #ANSWER_ITEMS = {
       # 1: (By.XPATH, "//div[@id='accordion__panel-0']"),
       # 2: (By.XPATH, "//div[@id='accordion__panel-1']"),
       # 3: (By.XPATH, "//div[@id='accordion__panel-2']"),
       # 4: (By.XPATH, "//div[@id='accordion__panel-3']"),
       # 5: (By.XPATH, "//div[@id='accordion__panel-4']"),
       # 6: (By.XPATH, "//div[@id='accordion__panel-5']"),
       # 7: (By.XPATH, "//div[@id='accordion__panel-6']"),
       # 8: (By.XPATH, "//div[@id='accordion__panel-7']")
   # }

   #ORDER_BUTTON_IN_HEADER = [By.XPATH, "(//button[text()='Заказать'])[1]"] #локатор для кнопки "Заказть" в хедэре на главной странице
   #ORDER_BUTTON_IN_SECTION_HOW_IT_WORKS = [By.XPATH, "(//button[text()='Заказать'])[2]"]  # локатор для кнопки "Заказть" в разделе "Как это работает" на главной странице

