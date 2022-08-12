
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

class OrderAboutRentPage:
    date_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    duration_rent_field = [By.CLASS_NAME, 'Dropdown-placeholder']
    duration_rent_options = [By.CSS_SELECTOR, 'div.Dropdown-option:nth-child(1)']
    duration_rent_option = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    color = {
        "black": [By.ID, 'black'],
        "grey": [By.ID, 'grey']
            }
    comment_field = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    submit_button = [By.XPATH, "(//button[text()='Заказать'])[2]"]
    confirm_button = [By.XPATH, "//button[text()='Да']"]
    title_success_order = [By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"]
    look_status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поля в форме об аренде')
    def send_data_about_rent(self, date, duration_rent, color, comment):
        self.driver.find_element(*self.date_field).send_keys(date)
        self.driver.find_element(*self.date_field).send_keys(Keys.ENTER)
        self.driver.find_element(*self.duration_rent_field).click()
        self.driver.find_element(*self.duration_rent_option[duration_rent]).click()
        self.driver.find_element(*self.color[color]).click()
        self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_button_submit(self):
        self.driver.find_element(*self.submit_button).click()

    @allure.step('Нажимаем кнопку подтверждения заказа')
    def click_popup_button_confirm(self):
        self.driver.find_element(*self.confirm_button).click()

    @allure.step('Нажимаем кнопку Посмотреть статус')
    def click_look_status_button(self):
        self.driver.find_element(*self.look_status_button).click()


