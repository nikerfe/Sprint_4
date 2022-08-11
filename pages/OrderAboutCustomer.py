
from selenium.webdriver.common.by import By
import allure

class OrderAboutCustomerPage:
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    subway_station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    subway_station_selected = [By.CSS_SELECTOR, '[class="select-search__select"]']
    phone_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    continue_button = [By.XPATH, "//button[text()='Далее']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поля в форме для кого самокат')
    def send_data_about_customer(self, name, surname, address, station, phone):
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.surname_field).send_keys(surname)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.subway_station_field).send_keys(station)
        self.driver.find_element(*self.subway_station_selected).click()
        self.driver.find_element(*self.phone_field).send_keys(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_button_continue(self):
        self.driver.find_element(*self.continue_button).click()
