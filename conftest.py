import pytest
from selenium import webdriver
from curl.curl import main_page_url


# Открытие/закрытие главной страницы
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(main_page_url)

    yield driver

    driver.quit()


