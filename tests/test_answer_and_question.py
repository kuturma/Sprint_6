import allure
import pytest
from pages.main_page import MainPage
from locators.locators_main_page import ImportantQuestionLocators


locator = ImportantQuestionLocators()
class TestAnswerAndQuestion:
    @allure.title("Проверка соответствия текста вопроса и ответа")
    @pytest.mark.parametrize("question_locator, answer_locator", [
        (locator.QWESTION_1, locator.ANSWER_1),
        (locator.QWESTION_2, locator.ANSWER_2),
        (locator.QWESTION_3, locator.ANSWER_3),
        (locator.QWESTION_4, locator.ANSWER_4),
        (locator.QWESTION_5, locator.ANSWER_5),
        (locator.QWESTION_6, locator.ANSWER_6),
        (locator.QWESTION_7, locator.ANSWER_7),
        (locator.QWESTION_8, locator.ANSWER_8)
])
    def test_check_text(self, driver, question_locator, answer_locator):
        main_page = MainPage(driver)
        main_page.check_answer_and_question(question_locator, answer_locator)