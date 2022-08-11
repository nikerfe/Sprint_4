from selenium import webdriver
from pages.Main import *
from pages.OrderAboutCustomer import *
from pages.OrderAboutRent import *
import data_for_test
import urls
import allure
import time


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()


    @allure.title('Позитивный сценарий заказа через кнопку в хедере')
    def test_success_order_one(self):
        main_page = MainPage(self.driver)
        order_about_customer_page = OrderAboutCustomerPage(self.driver)
        order_about_rent_page = OrderAboutRentPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.click_order_button_header()
        order_about_customer_page.send_data_about_customer(
            data_for_test.DATA_FOR_ORDER_ONE["name"],
            data_for_test.DATA_FOR_ORDER_ONE["surname"],
            data_for_test.DATA_FOR_ORDER_ONE["address"],
            data_for_test.DATA_FOR_ORDER_ONE["subway_station"],
            data_for_test.DATA_FOR_ORDER_ONE["phone"],
        )
        order_about_customer_page.click_button_continue()
        order_about_rent_page.send_data_about_rent(
            data_for_test.DATA_FOR_ORDER_ONE["date"],
            data_for_test.DATA_FOR_ORDER_ONE["duration_rent"],
            data_for_test.DATA_FOR_ORDER_ONE["color"],
            data_for_test.DATA_FOR_ORDER_ONE["comment"]
        )
        order_about_rent_page.click_button_submit()
        order_about_rent_page.click_popup_button_confirm()
        time.sleep(1)
        order_about_rent_page.click_look_status_button()
        main_page.click_logo_yandex_scooter()
        assert main_page.get_url("praktikum") == urls.BASE_URL
        main_page.click_logo_yandex(1)
        assert main_page.get_url("yandex") == urls.YANDEX_URL

    @allure.title('Позитивный сценарий заказа через блок Как это работает')
    def test_success_order_using_how_it_work_section(self):
        main_page = MainPage(self.driver)
        order_about_customer_page = OrderAboutCustomerPage(self.driver)
        order_about_rent_page = OrderAboutRentPage(self.driver)
        main_page.open_page(urls.BASE_URL)
        main_page.scroll_to_question_and_answers()
        main_page.click_order_button_how_it_work_section()
        order_about_customer_page.send_data_about_customer(
            data_for_test.DATA_FOR_ORDER_TWO["name"],
            data_for_test.DATA_FOR_ORDER_TWO["surname"],
            data_for_test.DATA_FOR_ORDER_TWO["address"],
            data_for_test.DATA_FOR_ORDER_TWO["subway_station"],
            data_for_test.DATA_FOR_ORDER_TWO["phone"],
        )
        order_about_customer_page.click_button_continue()
        order_about_rent_page.send_data_about_rent(
            data_for_test.DATA_FOR_ORDER_TWO["date"],
            data_for_test.DATA_FOR_ORDER_TWO["duration_rent"],
            data_for_test.DATA_FOR_ORDER_TWO["color"],
            data_for_test.DATA_FOR_ORDER_TWO["comment"]
        )
        order_about_rent_page.click_button_submit()
        order_about_rent_page.click_popup_button_confirm()
        time.sleep(1)
        order_about_rent_page.click_look_status_button()
        main_page.click_logo_yandex_scooter()
        assert main_page.get_url("praktikum") == urls.BASE_URL
        main_page.click_logo_yandex(2)
        assert main_page.get_url("yandex") == urls.YANDEX_URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


