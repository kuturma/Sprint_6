import allure

from pages.main_page import MainPage
from helpers.answers_text import Text
from locators.locators_main_page import PageHeaderLocators


class ChecksOnTheMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.page = MainPage(driver)

    ### ПРОВЕРКА ЧТО ВОПРОСУ СООТВЕТСТВУЕТ ПРАВИЛЬНЫЙ ОТВЕТ ###
    @allure.step('Проверка что полученный текст ответа соответствует тексту ответов определенного вопроса')
    def check_answer_and_question(self, question_locator, answer_locator):
        # переходим на главную страницу
        self.page.get_main_page()
        # прокрутка до элемента который мы предварительно находим
        self.page.scroll_find_element(question_locator)                                   
        # получаем текст вопроса, сохраняем его в переменную
        question_text = self.page.text_find_element(question_locator)                       
        # ждем пока элемент станет кликабельным, кликаем элемент на странице 
        self.page.wait_element_clickable(question_locator).click()
        # ждем пока элемент станет видимыи
        self.page.wait_element_visible(answer_locator)                                      
        # получаем текст ответа
        answer_text = self.page.text_find_element(answer_locator)                           
        # сравниваем переменную с текстом ответа из словаря
        assert answer_text == Text.questions_and_answers[question_text]


    ### ПЕРЕХОД НА ГЛАВНУЮ СТРАНИЦУ ПУТЕМ НАЖАТИЯ НА ЛОГОТИП "САМОКАТ" ###
    @allure.step('Переход на главную страницу путем нажатия на логотип "САМОКАТ"')
    def click_logo_samokat(self):
        # переходим на главную страницу
        self.page.get_main_page()
        # переход на страницу ввода данных для оформления заказа
        self.page.click_wait_element_visible(PageHeaderLocators.BUTTON_ORDER_SCOOTER_ON_TOP)
        # ждем пока логотип станет видимыи и кликаем
        self.page.click_wait_element_clickable(PageHeaderLocators.LOGO_SCOOTER)


    ### ПЕРЕХОД НА СТРАНИЦУ ДЗЕНА ПУТЕМ НАЖАТИЯ НА ЛОГОТИП "ЯНДЕКС" ###
    @allure.step('Переход на страницу "Дзен" путем нажатия на логотип "Яндекс"')
    def click_logo_yandex(self):
        # переходим на главную страницу
        self.page.get_main_page()
        # ждем пока логотип станет видимыи и кликаем
        self.page.click_wait_element_clickable(PageHeaderLocators.LOGO_YANDEX)
        # переключиться на вкладку "Дзен"
        self.page.switch_window()
        # ждем пока логотип станет видимыи
        self.page.wait_element_visible(PageHeaderLocators.LOGO_DZEN)