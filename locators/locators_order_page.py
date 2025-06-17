from selenium.webdriver.common.by import By

#Страница: Для кого самокат
class ForWhoScooterPageLocators:

    # Поле ввода: Имя
    FIRST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')

    # Поле ввода: Фамилия
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')

    # Поле ввода: Адрес
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')

    # Поле выбора: Станции метро
    STATION_METRO_FIELD = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # Выбор: метро Таганская
    CHOICE_METRO_STATION_TAGANSKAYA = (By.XPATH, '//li[@class = "select-search__row"]//div[text()="Таганская"]')
    # Выбор: метро Комсомольская
    CHOICE_METRO_STATION_KOMSOMOLSKAYA = (By.XPATH, '//li[@class = "select-search__row"]//div[text() = "Комсомольская"]')    

    # Поле ввода: Телефон
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    
    # Кнопка: Далее
    BUTTON_NEXT = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
 


# Страница: Про аренду
class AboutRentPageLocators:
    # Поле: Когда привезти самокат
    WHEN_DELIVERY_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    # Выбор: дата 16.06.2025
    CHOICE_DATE_16_06_2025 = (By.XPATH, "//div[text()='16' and contains(@aria-label, '16-е июня 2025')]")
    # Выбор: дата 17.06.2025
    CHOICE_DATE_17_06_2025 = (By.XPATH, "//div[text()='17' and contains(@aria-label, '17-е июня 2025')]")

    # Поле выбора: Срок аренды
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')
    # Выбор: сутки
    CHOICE_DAY = (By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]')
    # Выбор: двое суток
    CHOICE_TWO_DAY = (By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]')

    # Поле выбора: Цвет самоката:
    # Чекбокс: - Чёрный жемчуг
    COLOR_FIELD_BLACK_SWAN = (By.ID, 'black')
    # Чекбокс: - Cерая безысходность
    COLOR_FIELD_SILVER_DESPAIR = (By.ID, 'grey')

    # Поле: Комментарий для курьера
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Кнопка: Заказать
    BUTTON_ORDER = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # Кнопка: Назад
    BUTTON_BACK = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]')  ### НЕ ИСПОЛЬЗОВАЛСЯ

    
# Всплывающее окно: Хотите оформить заказ?
class WindowWantOrderLocators:
    #WINDOW = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    # Поле: ДА
    BUTTON_YES = (By.XPATH, '//button[text()="Да"]')

    # Поле: НЕТ
    BUTTON_NO = (By.XPATH, '//button[text()="Нет"]')  ### НЕ ИСПОЛЬЗОВАЛСЯ

# Всплывающее окно: Заказ оформлен
class WindowOrderMadeLocators:

    # Заголовок окна: Заказ оформлен
    HEADER_ORDER_MADE = (By.XPATH, '//div[text()="Заказ оформлен"]')
    # Поле: Кнопка "Посмотреть статус"
    BUTTON_CHECK_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]') ### НЕ ИСПОЛЬЗОВАЛСЯ


