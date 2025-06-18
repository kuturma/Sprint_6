import pytest
import allure
from pages.main_page import MainPage
from pages.checks_on_the_main_page import ChecksOnTheMainPage
from curl.curl import main_page_url, dzen


class TestLogo:
    @allure.title('Тест перехода на главную страницу путем нажатия на логотип "Самокат"')
    def test_logo_samokat(self, driver):
        page = MainPage(driver)
        checks_main_page = ChecksOnTheMainPage(driver)
        checks_main_page.click_logo_samokat()
        assert page.get_url_page() == main_page_url


    @allure.title('Тест перехода на страницу "Дзена" путем нажатия на логотип "Яндекс"')
    def test_logo_yandex(self, driver):
        page = MainPage(driver)
        checks_main_page = ChecksOnTheMainPage(driver)
        checks_main_page.click_logo_yandex()
        assert page.get_url_page() == dzen