from .base_page import BasePage
from .locators import MainPageLocators
from .locators import CatalogPageLocators
from utils.logger import log_method
import allure

class CatalogPage(BasePage):
    """Страница каталога товаров"""
    @allure.step('Go to smartphone page')
    def go_to_smartphone_page(self):
        """
        Переходит на страницу смартфонов, кликая по ссылке.
        """
        log_method("Go to smartphone page")
        self.click(*CatalogPageLocators.SMARTPHONE_LINK)

    @allure.step('Should be smartphone word')  
    def should_be_smartphone_word(self):
        """
        Проверяет, что на странице отображается слово 'Смартфоны' в заголовке каталога.
        """
        log_method("Should be smartphone word")
        self.should_be_text(*MainPageLocators.CATALOG_TITLE, "Смартфоны")