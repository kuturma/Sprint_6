import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl.curl import main_page_url



class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    ### GET_URL ###
    @allure.step('Открыть главную страницу')
    def get_main_page(self):
        return self.driver.get(main_page_url)


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


    ### CURRENT_URL ###
    @allure.step('Получить текущий адрес страницы')
    def get_url_page(self):
        return self.driver.current_url
    

    ### ПЕРЕКЛЮЧИТЬСЯ НА НОВУЮ ВКЛАДКУ ###
    @allure.step('Переключиться на новую вкладку')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Дождаться полной загрузки страницы')
    def wait_for_page_to_load(self):
       self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        




