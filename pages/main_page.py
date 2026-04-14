from .base_page import BasePage
from .locators import MainPageLocators
import allure
from utils.logger import log_method

class MainPage(BasePage):
    """Главная страница сайта"""
    @allure.step("Go to katalog")
    def go_to_katalog(self):
        """Переход на страницу каталога через верхнее меню"""
        log_method("Go to katalog")
        self.click(*MainPageLocators.CATALOG_LINK)
        

    @allure.step("Should be katalog word")
    def should_be_katalog_word(self):
        log_method("Should be katalog word")
        """Проверяем, что на странице отображается слово 'Каталог'"""
        self.should_be_text(*MainPageLocators.CATALOG_TITLE, "Каталог")
