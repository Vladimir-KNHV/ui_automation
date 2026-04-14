from .base_page import BasePage
from .locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure
from utils.retry import retry
import time
from selenium.webdriver.common.keys import Keys
from utils.logger import log_method


class OrderPage(BasePage):
    """Страница оформления заказа"""

    @allure.step("Get order product name")
    def get_order_product_name(self):
        """
        Получает название товара в заказе.
        """
        log_method("Get order product name")
        element = self.wait_for_element(*OrderPageLocators.ORDER_PRODUCT_NAME)
        return element.text

    @allure.step("Get total price")
    def get_total_price(self):
        """
        Получает итоговую сумму заказа.
        """
        log_method("Get total price")
        element = self.wait_for_clickable(*OrderPageLocators.ORDER_TOTAL_PRICE)
        return element.text

    @allure.step("Fill name")
    def fill_name(self, user):
        """
        Заполняет поле имени пользователя.
        """
        log_method("Fill name")
        self.send_keys(*OrderPageLocators.FIO, user.name)

    @allure.step("Fill phone")
    def fill_phone(self, user):
        """
        Заполняет поле телефона пользователя.
        """
        log_method("Fill phone")
        self.send_keys(*OrderPageLocators.PHONE, user.phone)

    @allure.step("Fill city")
    def fill_city(self, user):
        """
        Заполняет город и выбирает вариант из подсказок.
        """
        log_method("Fill city")
        element = self.wait_for_clickable(*OrderPageLocators.CITY)
        element.clear()
        element.send_keys(user.city)

        WebDriverWait(self.browser, 5).until(
            lambda d: len(
                d.find_elements(
                    By.CSS_SELECTOR, '[id="delivery_address"] .tt-suggestion'
                )
            )
            > 0
        )

        options = self.browser.find_elements(
            By.CSS_SELECTOR, '[id="delivery_address"] .tt-suggestion'
        )

        options[0].click()
        self.wait_for_spinner(*OrderPageLocators.SPINNER)

    @allure.step("Select delivery")
    def select_delivery(self):
        """
        Выбирает способ доставки.
        """
        log_method("Select delivery")
        self.click(*OrderPageLocators.DELIVERY)

    @allure.step("Fill address")
    def fill_address(self, user):
        """
        Заполняет адрес доставки.
        """
        log_method("Fill address")
        self.send_keys(*OrderPageLocators.ADDRESS, user.address)

    @allure.step("Fill comment")
    def fill_comment(self, user):
        """
        Заполняет комментарий к заказу.
        """
        log_method("Fill comment")
        self.send_keys(*OrderPageLocators.COMMENT, user.comment)

    @retry(times=3, step_name="Select date")
    def select_date(self):
        """
        Выбирает дату доставки в календаре.
        """
        log_method("Select date")
        calendar = self.wait_for_clickable(*OrderPageLocators.DATE)
        self.scroll_to_element(calendar)

        self.browser.execute_script("arguments[0].click();", calendar)

        day = self.wait_for_clickable(*OrderPageLocators.DAY)
        self.browser.execute_script("arguments[0].click();", day)

        WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".rd-container[style*='display: inline-block']")
            )
        )

    @allure.step("Select time")
    def select_time(self):
        """
        Выбирает время доставки.
        """
        log_method("Select time")
        element = self.wait_for_element(*OrderPageLocators.DELIVERY_TIME)
        element.click()
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        element.send_keys(Keys.ENTER)

    @allure.step("Fill email")
    def fill_email(self, user):
        """
        Заполняет email пользователя.
        """
        log_method("Fill email")
        self.send_keys(*OrderPageLocators.EMAIL, user.email)

    @allure.step("Select notifications")
    def select_notifications(self):
        """
        Включает уведомления для заказа.
        """
        log_method("Select notifications")
        self.click(*OrderPageLocators.NOTIFICATION_CHECKBOX)

    @allure.step("Fill full order form")
    def fill_order_form(self, user):
        """
        Заполняет всю форму заказа целиком.
        """
        log_method("Fill full order form")
        self.fill_name(user)
        self.fill_phone(user)
        self.fill_city(user)
        self.select_delivery()
        self.fill_address(user)
        self.fill_comment(user)
        self.select_date()
        self.select_time()
        self.fill_email(user)
        self.select_notifications()
