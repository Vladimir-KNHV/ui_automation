from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from utils.logger import logger

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # ==================================================
    #                     NAVIGATION
    # ==================================================

    @allure.step('Open page')
    def open(self):
        """Открывает страницу по URL"""
        logger.info(f"OPEN page")
        self.browser.get(self.url)

    @allure.step('Refresh page')    
    def refresh_page(self):
        logger.info(f"REFRESH page")
        """Обновляет текущую страницу"""
        self.browser.refresh()

    # ==================================================
    #                     ASSERTIONS
    # ==================================================

    @allure.step('Should be text')
    def should_be_text(self, how, what, expected_text):
        """Проверяет, что текст элемента совпадает с ожидаемым"""
        logger.info(f"SHOULD be text")
        element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((how, what))
        )
        assert element.text == expected_text, (
            f"Ожидали текст '{expected_text}', но получили '{element.text}'"
        )

    @allure.step('Should be URL')
    def should_be_url(self, expected_url):
        """Проверяет, что текущий URL совпадает с ожидаемым"""
        logger.info(f"SHOULD be url")
        WebDriverWait(self.browser, 15).until(
            EC.url_to_be(expected_url)
        )
        current_url = self.browser.current_url

        assert current_url == expected_url, (
            f"Ожидали URL '{expected_url}', но получили '{current_url}'"
        )

    # ==================================================
    #                 WAITING HELPERS
    # ==================================================

    @allure.step('Wait for spinner')
    def wait_for_spinner(self, how, what, timeout=10):
        """Ждём появления и исчезновения спиннера"""
        logger.info(f"WAIT for spinner")
        spinner = (how, what)

        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(spinner)
        )

        WebDriverWait(self.browser, timeout).until(
            EC.invisibility_of_element_located(spinner)
        )

    @allure.step('Wait for element')
    def wait_for_element(self, how, what, timeout=15):
        """Ждём появления элемента на странице"""
        logger.info(f"WAIT for element: {what}")
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((how, what))
        )

    @allure.step('Wait for clickable')
    def wait_for_clickable(self, how, what, timeout=15):
        """Ждём, пока элемент станет кликабельным"""
        logger.info(f"WAIT for clickable: {what}")
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((how, what))
        )

    # ==================================================
    #                    ACTIONS
    # ==================================================

    @allure.step('Scroll to element')
    def scroll_to_element(self, element):
        """Скроллит страницу к элементу по центру экрана"""
        logger.info(f"SCROLL to element")
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    @allure.step('Send keys')
    def send_keys(self, how, what, value, clear_first=True):
        """Ввод текста в элемент"""
        logger.info(f"TYPE '{value}' into {what}")
        element = self.wait_for_clickable(how, what)

        if clear_first:
            element.clear()

        element.send_keys(value)

    @allure.step('Click')
    def click(self, how, what):
        """
        Клик по элементу:
        - ждём появления
        - скроллим
        - пробуем обычный клик
        - fallback на JS click
        """
        logger.info(f"MULTI-CLICK on element: {what}")
        element = self.wait_for_element(how, what)

        self.scroll_to_element(element)

        try:
            element.click()
            logger.info(f"CLICK on element: {what}")
        except Exception:
            self.browser.execute_script(
                "arguments[0].click();",
                element
            )
            logger.info(f"SCRIPT CLICK on element: {what}")