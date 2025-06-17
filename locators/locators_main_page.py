from selenium.webdriver.common.by import By

# Логотипы в шапке страницы
class PageHeaderLocators:
    # Логотип Яндекса вверху страницы
    LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    # Логотип Самокат вверху страницы
    LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR') 

    # Кнопка "Заказать" вверху страницы
    BUTTON_ORDER_SCOOTER_ON_TOP = (By.CLASS_NAME, 'Button_Button__ra12g')


class ImportantQuestionLocators:

    # Заголовок "Вопросы о важном"
    HEADER_IMPORTANT_QUESTION = (By.XPATH, ("//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']"))

    # 1. Вопрос 1: 'Сколько это стоит? И как оплатить?'
    QWESTION_1 = (By.ID, 'accordion__heading-0')

    # 1. Ответ на вопрос 1: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_1 = (By.ID, 'accordion__panel-0')

    # 2. Вопрос 2: 'Хочу сразу несколько самокатов! Так можно?'
    QWESTION_2 = (By.ID, 'accordion__heading-1')

    # 2. Ответ на вопрос 2: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_2 = (By.ID, 'accordion__panel-1')

    # 3.  Вопрос 3: 'Как рассчитывается время аренды?'
    QWESTION_3 = (By.ID, 'accordion__heading-2')

    # 3. Ответ на вопрос 3: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_3 = (By.ID, 'accordion__panel-2')

    # 4.  Вопрос 4: 'Можно ли заказать самокат прямо на сегодня?'
    QWESTION_4 = (By.ID, 'accordion__heading-3')

    # 4. Ответ на вопрос 4: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_4 = (By.ID, 'accordion__panel-3')

    # 5.  Вопрос 5: 'Можно ли продлить заказ или вернуть самокат раньше?'
    QWESTION_5 = (By.ID, 'accordion__heading-4')

    # 5. Ответ на вопрос 5: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_5 = (By.ID, 'accordion__panel-4')

    # 6.  Вопрос 6: 'Вы привозите зарядку вместе с самокатом?'
    QWESTION_6 = (By.ID, 'accordion__heading-5')

    # 6. Ответ на вопрос 6: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится'
    ANSWER_6 = (By.ID, 'accordion__panel-5')

    # 7.  Вопрос 7: 'Можно ли отменить заказ?'
    QWESTION_7 = (By.ID, 'accordion__heading-6')

    # 7. Ответ на вопрос 7: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_7 = (By.ID, 'accordion__panel-6')

    # 8.  Вопрос 8: 'Я жизу за МКАДом, привезёте?'
    QWESTION_8 = (By.ID, 'accordion__heading-7')

    # 8. Ответ на вопрос 8: 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ANSWER_8 = (By.ID, 'accordion__panel-7')


class ButtonOrderInCenterPageLocators:

    # Кнопка "Заказать" в центре страницы
    BUTTON_ORDER_SCOOTER_ON_CENTER = (By.XPATH, '//div[contains(@class, "Home_FinishButton__1")]/button[text()="Заказать"]')
