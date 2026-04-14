from .base_page import BasePage
from .locators import ProductPageLocators
from utils.logger import log_method
import allure


class ProductPage(BasePage):

    @allure.step('Get product name')
    def get_product_name(self):
        """
        Получает название товара на странице продукта.
        """
        log_method("Get product name")
        element = self.wait_for_element(*ProductPageLocators.PRODUCT_NAME)
        return element.text

    @allure.step('Get product price')
    def get_product_price(self):
        """
        Получает цену товара на странице продукта.
        """
        log_method("Get product price")
        element = self.wait_for_element(*ProductPageLocators.PRODUCT_PRICE)
        return element.text

    @allure.step('Add to basket')
    def add_to_basket(self):
        """
        Добавляет товар в корзину.
        """
        log_method("Add to basket")
        self.click(*ProductPageLocators.ADD_TO_BASKET)

    @allure.step('Go to basket')
    def go_to_basket(self):
        """
        Переходит в корзину.
        """
        log_method("Go to basket")
        self.click(*ProductPageLocators.OPEN_BASKET)

    @allure.step('Should be basket word')
    def should_be_basket_word(self):
        """
        Проверяет, что на странице отображается слово 'Корзина'.
        """
        log_method("Should be basket word")
        self.should_be_text(*ProductPageLocators.BASKET_WORD, 'Корзина')