from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_TITLE_OF_FORM_FOR_WHOM_IS_SCOOTER = [By.XPATH, "//div[text()='Для кого самокат']"] #наименование формы "Для кого самокат" на странице /order
    ORDER_INPUT_NAME = [By.XPATH, "//input[contains(@placeholder, '* Имя')]"] #поле ввода имени в форме "Для кого самокат" на странице /order
    ORDER_INPUT_SURNAME = [By.XPATH, "//input[contains(@placeholder, '* Фамилия')]"]  # поле ввода фамилии в форме "Для кого самокат" на странице /order
    ORDER_INPUT_ADDRESS = [By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]"]  # поле ввода адреса в форме "Для кого самокат" на странице /order
    ORDER_INPUT_METRO_STATION = [By.XPATH, "//input[contains(@placeholder, '* Станция метро')]"]  # поле выбора станции метро в форме "Для кого самокат" на странице /order
    ORDER_METRO_STATION_7 = [By.XPATH, "//button[@value='7']"]  # станция метро "Красные Ворота" в списке
    ORDER_INPUT_PHONE_NUMBER = [By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]"]  # поле ввода номера телефона в форме "Для кого самокат" на странице /order
    ORDER_BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"] #кнопка "Далее" в форме "Для кого самокат" на странице /order
    ORDER_INPUT_WHEN_TO_BRING = [By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]"]  # поле ввода или выбора даты доставки самоката в форме "Про аренду"
    ORDER_DATE_DELIVERY = [By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0') and text()]"]
    ORDER_INPUT_RENTAL_PERIOD = [By.XPATH, "//div[text()='* Срок аренды']"]  # поле выбора срока аренды формы "Про аренду"
    ORDER_RENTAL_PERIOD_THREES_DAY = [By.XPATH, "//div[text()='трое суток']"]  # срок аренды "трое суток" в дропдауне "Срок аренды" формы "Про аренду"
    ORDER_CHECKBOX_COLOR_SCOOTER = [By.XPATH, "//input[@id='grey']"]  # чек-бокс "серая безысходность" в поле "Цвет самоката" формы "Про аренду"
    ORDER_INPUT_COMMENT_FOR_COURIER = [By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]"]  #поле для ввода комментария для курьера формы "Про аренду"
    ORDER_BUTTON_ORDER = [By.XPATH, "//button[text()='Заказать' and position()=2]"]  #кнопка "Заказать" для оформления заказа, расположенная под формой "Про аренду"
    ORDER_BUTTON_YES = [By.XPATH, "//button[text()='Да']"]  #кнопка "Да" во всплывающем окне "Хотите оформить заказ?"
    ORDER_CHECK_STATUS_OF_ORDER = [By.XPATH, ".//*[text()='Посмотреть статус']"] # кнопка "Посмотреть статус" во всплывающем окне "Заказ оформлен"