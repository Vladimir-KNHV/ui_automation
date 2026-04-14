from .base_page import BasePage
from .locators import SmartphonesPageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log_method

class SmartphonePage(BasePage):

    @allure.step("Select filter")
    def select_filter(self, locator):
        """
        Выбирает фильтр и ожидает обновления списка товаров.
        """
        log_method("Select filter")
        old_product = self.browser.find_element(*SmartphonesPageLocators.SELECT_PRODUCT_1)
        self.click(*locator)

        WebDriverWait(self.browser, 10).until(
            EC.staleness_of(old_product)
        )

    @allure.step("Go to product page")
    def go_to_product_page(self):
        """
        Переходит на страницу продукта из списка смартфонов.
        """
        log_method("Go to product page")
        self.wait_for_clickable(*SmartphonesPageLocators.SELECT_PRODUCT_1)
        self.click(*SmartphonesPageLocators.SELECT_PRODUCT_1)

    @allure.step("Should be description word")
    def should_be_description_word(self):
        """
        Проверяет, что на странице отображается слово 'ОПИСАНИЕ'.
        """
        log_method("Should be description word")
        self.should_be_text(*SmartphonesPageLocators.DESCRIPTION, "ОПИСАНИЕ")