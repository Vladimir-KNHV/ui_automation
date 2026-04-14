from .base_page import BasePage
from .locators import BasketPageLocators
from utils.logger import log_method
import allure

class BasketPage(BasePage):
    """Страница корзины"""
    @allure.step('Submit offer')    
    def submit_offer(self):
        """
        Кликает по кнопке "Оформить заказ" на странице корзины.
        """
        log_method("Submit offer")
        self.click(*BasketPageLocators.SUBMIT_BUTTON)
        
