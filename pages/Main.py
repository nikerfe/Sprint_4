from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

class MainPage:
    questions = {
        1: [By.ID, 'accordion__heading-0'],
        2: [By.ID, 'accordion__heading-1'],
        3: [By.ID, 'accordion__heading-2'],
        4: [By.ID, 'accordion__heading-3'],
        5: [By.ID, 'accordion__heading-4'],
        6: [By.ID, 'accordion__heading-5'],
        7: [By.ID, 'accordion__heading-6'],
        8: [By.ID, 'accordion__heading-7']
    }

    answers = {
        1: [By.ID, 'accordion__panel-0'],
        2: [By.ID, 'accordion__panel-1'],
        3: [By.ID, 'accordion__panel-2'],
        4: [By.ID, 'accordion__panel-3'],
        5: [By.ID, 'accordion__panel-4'],
        6: [By.ID, 'accordion__panel-5'],
        7: [By.ID, 'accordion__panel-6'],
        8: [By.ID, 'accordion__panel-7'],
    }

    order_button_header = [By.XPATH, "(//button[text()='Заказать'])[1]"]
    order_button_how_it_work_section = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    logo_yandex_scooter = [By.CSS_SELECTOR, '[alt = "Scooter"]']
    logo_yandex = [By.CSS_SELECTOR, '[alt = "Yandex"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по URL')
    def open_page(self, host):
        self.driver.get(host)

    @allure.step('Получаем значение URL')
    def get_url(self, url):
        WebDriverWait(self.driver, timeout=5).until(EC.url_contains(url))
        return self.driver.current_url

    @allure.step('Нажимаем на элемент с вопросом')
    def click_question_button(self, number_button):
        self.driver.find_element(*self.questions[number_button]).click()

    @allure.step('Получаем текст элемента с вопросом')
    def get_question_button_text(self, number_button):
        return self.driver.find_element(*self.questions[number_button]).text

    @allure.step('Получаем текст элемента с ответом')
    def get_answer_button_text(self, number_button):
        return self.driver.find_element(*self.answers[number_button]).text

    @allure.step('Скроллим страницу')
    def scroll_to_question_and_answers(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    @allure.step('Нажимаем кнопку Заказать в хедере')
    def click_order_button_header(self):
        self.driver.find_element(*self.order_button_header).click()

    @allure.step('Нажимаем кнопку Заказать в блоке Как это работает')
    def click_order_button_how_it_work_section(self):
        self.driver.find_element(*self.order_button_how_it_work_section).click()

    @allure.step('Нажимаем логотип Самокат')
    def click_logo_yandex_scooter(self):
        self.driver.find_element(*self.logo_yandex_scooter).click()


    @allure.step('Нажимаем логотип Yandex')
    def click_logo_yandex(self, tab):
        self.driver.find_element(*self.logo_yandex).click()
        window_after = self.driver.window_handles[tab]
        self.driver.switch_to.window(window_after)
