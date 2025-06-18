import allure
from pages.main_page import MainPage
from locators.locators_main_page import PageHeaderLocators, ButtonOrderInCenterPageLocators
from locators.locators_order_page import ForWhoScooterPageLocators, AboutRentPageLocators, WindowWantOrderLocators, WindowOrderMadeLocators


for_who = ForWhoScooterPageLocators()
about_rent = AboutRentPageLocators()
confirm_order = WindowWantOrderLocators()
made_order = WindowOrderMadeLocators()


class EnterDataUserForWho:
    def __init__(self, driver):
        self.driver = driver
        self.page = MainPage(driver)

    @allure.step('Переход на страницу заказа самоката через кнопку "Заказать" вверху страницы')
    def order_button_in_header(self):
        self.page.click_wait_element_visible(PageHeaderLocators.BUTTON_ORDER_SCOOTER_ON_TOP)

    
    @allure.step('Переход на страницу заказа самоката через кнопку "Заказать" в середине страницы')
    def order_button_in_center_page(self):
        self.page.scroll_find_element(ButtonOrderInCenterPageLocators.BUTTON_ORDER_SCOOTER_ON_CENTER)
        self.page.click_wait_element_visible(ButtonOrderInCenterPageLocators.BUTTON_ORDER_SCOOTER_ON_CENTER)


    # Ввод данных для заказа самоката
    @allure.step('Ввод данных в поля для заказа самоката')
    def enter_user_data(self, user):      
        # Ввод имени
        self.page.send_keys_wait_element_visible(for_who.FIRST_NAME_FIELD, user.name)
        
        # Ввод фамилии
        self.page.send_keys_wait_element_visible(for_who.LAST_NAME_FIELD, user.last_name)
        
        # Ввод адреса
        self.page.send_keys_wait_element_visible(for_who.ADDRESS_FIELD, user.address)
        
        # Ждем когда элемент "Станция метро" станет видимым и кликаем на него
        self.page.click_wait_element_visible(for_who.STATION_METRO_FIELD)
        
        # Делаем скролл до нужной станции метро
        self.page.scroll_find_element(user.metro_station)
        
        # Ждем когда станция метро станет кликабельной и выбираем её
        self.page.click_wait_element_clickable(user.metro_station)
        
        # Ввод номера телефона
        self.page.send_keys_wait_element_visible(for_who.PHONE_FIELD, user.phone_number)
        
        # Клик по кнопке "Далее"
        self.page.click_wait_element_visible(for_who.BUTTON_NEXT)

        # Ввод даты аренды
        self.page.send_keys_wait_element_visible(about_rent.WHEN_DELIVERY_FIELD, user.date_order)
        
        # Клик по дате в календаре
        self.page.click_wait_element_clickable(user.coice_date)

        # Клик по полю срок аренды
        self.page.click_wait_element_visible(about_rent.RENTAL_PERIOD_FIELD)

        # Скролл до нужного срока аренды
        self.page.scroll_find_element(user.rental_period)

        # Клик по нужному сроку аренды
        self.page.click_wait_element_clickable(user.rental_period)
        
        # Клик по чекбоксу для выбора цвета самоката
        self.page.click_wait_element_visible(user.color)

        # Ввод комментария
        self.page.send_keys_wait_element_visible(about_rent.COMMENT_FIELD, user.comment)

    
    @allure.step('Подтверждение данных после заполнения полей и что появилось окно "Заказ оформлен"')
    def confirm_user_data(self):
        # Клик по кнопке "Заказать"
        self.page.click_wait_element_visible(about_rent.BUTTON_ORDER)

        # Клик по кнопке "Да" в окне "Хотите оформить заказ?"  
        self.page.click_wait_element_clickable(confirm_order.BUTTON_YES)
        