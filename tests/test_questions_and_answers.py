
from selenium import webdriver
from pages.Main import MainPage
import data_for_test
import urls
import allure
import time

class TestQuestionsAndAnswers:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка контента Вопроса № 1')
    def test_first_quiestion(self):
        number_question = 1
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 2')
    def test_second_quiestion(self):
        number_question = 2
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 3')
    def test_third_quiestion(self):
        number_question = 3
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 4')
    def test_fourth_quiestion(self):
        number_question = 4
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 5')
    def test_fifth_quiestion(self):
        number_question = 5
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 6')
    def test_sixth_quiestion(self):
        number_question = 6
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 7')
    def test_seventh_quiestion(self):
        number_question = 7
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @allure.title('Проверка контента Вопроса № 8')
    def test_eighth_quiestion(self):
        number_question = 8
        main_page = MainPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        assert main_page.get_question_button_text(number_question) == data_for_test.QUESTIONS_TEXT[number_question]
        main_page.click_question_button(number_question)
        time.sleep(1)
        assert main_page.get_answer_button_text(number_question) == data_for_test.ANSWERS_TEXT[number_question]

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()