import pytest
import allure
from helpers.data_for_order import User1ForWho, User2ForWho
from pages.order_page import EnterDataUserForWho
from pages.main_page import MainPage
from locators.locators_order_page import WindowOrderMadeLocators


class TestEnterDataAndSuccessfulOrder:

    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" вверху главной страницы, c параметризацией, тестируется два пользователя')
    @pytest.mark.parametrize("user", [User1ForWho, User2ForWho])
    def test_sucess_order_by_top_button(self, driver, user):
        page = EnterDataUserForWho(driver)
        page.order_button_in_header()
        page.enter_user_data(user)
        page.confirm_user_data()
        made_order = WindowOrderMadeLocators()
        main_page = MainPage(driver)
        assert 'Заказ оформлен' in main_page.text_wait_element_visible(made_order.HEADER_ORDER_MADE)

    @allure.title('Тест успешного заказа самоката при нажатии кнопки "Заказать" в середине главной страницы, в конце появляется всплывающее окно "Заказ оформлен"')
    def test_sucess_order_by_center_button(self, driver):
        page = EnterDataUserForWho(driver)
        page.order_button_in_center_page()
        page.enter_user_data(User1ForWho)
        page.confirm_user_data()
        made_order = WindowOrderMadeLocators()
        main_page = MainPage(driver)
        assert 'Заказ оформлен' in main_page.text_wait_element_visible(made_order.HEADER_ORDER_MADE)
