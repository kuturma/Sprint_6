import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl.curl import main_page_url
from helpers.answers_text import Text
from locators.locators_main_page import PageHeaderLocators
import time


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    ### FIND_ELEMENT ###
    @allure.step('Найти элемент на странице')
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    
    @allure.step('Кликнуть по найденому элементу на странице')
    def click_element(self, locator):
        return self.find_element(locator).click()
    

    @allure.step('Заполнить данные найденного элемента на странице')
    def send_keys_find_element(self, locator, data):
        self.find_element(locator).send_keys(data)
    
    
    @allure.step('Получить текст найденного элемента на странице')
    def text_find_element(self, locator):
        return self.find_element(locator).text


    ### VISIBILITY_OF_ELEMENT_LOCATED ###
    @allure.step('Явное ожидание элемента что он виден на странице')
    def wait_element_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    
   
    @allure.step('Кликнуть по найденому элементу на странице с явным ожиданием что он виден на странице')
    def click_wait_element_visible(self, locator):
        return self.wait_element_visible(locator).click()
    
    
    @allure.step('Заполнить данные найденного элемента на странице с явным ожиданием что он виден на странице')
    def send_keys_wait_element_visible(self, locator, data):
        self.wait_element_visible(locator).send_keys(data)


    @allure.step('Получить текст найденного элемента на странице с явным ожиданием что он виден на странице')
    def text_wait_element_visible(self, locator):
        return self.wait_element_visible(locator).text



    ### ELEMENT_TO_BE_CLICKABLE ###
    @allure.step('Явное ожидание элемента что он кликабелен на странице')
    def wait_element_clickable(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))
            
    
    @allure.step('Кликнуть по найденому элементу на странице с явным ожиданием что он кликабелен на странице')
    def click_wait_element_clickable(self, locator):
        return self.wait_element_clickable(locator).click()
    
   
    @allure.step('Заполнить данные найденного элемента на странице с явным ожиданием что он кликабелен на странице')
    def send_keys_wait_element_clicable(self, locator, data):
        return self.wait_element_clickable(locator).send_keys(data)
    
   
    @allure.step('Получить текст найденного элемента на странице с явным ожиданием что он кликабелен на странице')
    def text_wait_element_clicable(self, locator):
        return self.wait_element_clickable(locator).text


 
    ### SCROLLINTOVIEW ###
    @allure.step('Прокрутка до найденого элемента на странице')
    def scroll_find_element(self, locator):  
        element=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    ### ПРОВЕРКА ЧТО ВОПРОСУ СООТВЕТСТВУЕТ ПРАВИЛЬНЫЙ ОТВЕТ ###
    @allure.step('Проверка что полученный текст ответа соответствует тексту ответов определенного вопроса')
    def check_answer_and_question(self, question_locator, answer_locator):
        # переходим на главную страницу
        self.driver.get(main_page_url)
        # прокрутка до элемента который мы предварительно находим
        self.scroll_find_element(question_locator)
        # получаем текст вопроса, сохраняем его в переменную
        question_text = self.text_find_element(question_locator)
        # ждем пока элемент станет кликабельным, кликаем элемент на странице
        self.wait_element_clickable(question_locator).click()
        # ждем пока элемент станет видимыи
        self.wait_element_visible(answer_locator)
        # получаем текст ответа
        answer_text = self.text_find_element(answer_locator)
        # сравниваем переменную с текстом ответа из словаря
        assert answer_text == Text.questions_and_answers[question_text]


    ### CURRENT_URL ###
    @allure.step('Получить текущий адрес страницы')
    def get_url_page(self):
        return self.driver.current_url

    ### ПЕРЕКЛЮЧИТЬСЯ НА НОВУЮ ВКЛАДКУ ###
    @allure.step('Переключиться на новую вкладку')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])


    ### ПЕРЕХОД НА ГЛАВНУЮ СТРАНИЦУ ПУТЕМ НАЖАТИЯ НА ЛОГОТИП "САМОКАТ" ###
    @allure.step('Переход на главную страницу путем нажатия на логотип "САМОКАТ"')
    def click_logo_samokat(self):
        # переходим на главную страницу
        self.driver.get(main_page_url)
        # переход на страницу ввода данных для оформления заказа
        self.click_wait_element_visible(PageHeaderLocators.BUTTON_ORDER_SCOOTER_ON_TOP)
        # ждем пока логотип станет видимыи и кликаем
        self.click_wait_element_clickable(PageHeaderLocators.LOGO_SCOOTER)
        

    ### ПЕРЕХОД НА СТРАНИЦУ ДЗЕНА ПУТЕМ НАЖАТИЯ НА ЛОГОТИП "ЯНДЕКС" ###
    @allure.step('Переход на страницу "Дзен" путем нажатия на логотип "Яндекс"')
    def click_logo_yandex(self):
        # переходим на главную страницу
        self.driver.get(main_page_url)
        # ждем пока логотип станет видимыи и кликаем
        self.click_wait_element_clickable(PageHeaderLocators.LOGO_YANDEX)
        time.sleep(2)
        # переключиться на вкладку "Дзен"
        self.switch_window()
        time.sleep(2)

